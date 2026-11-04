import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import (
    launch_headed_browser,
    create_browser_context,
    ensure_authenticated_page,
    load_test_data,
    log,
)

test_data = load_test_data()
stacx_id = test_data.get("stacx_id", "MCL72626122406")

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = ensure_authenticated_page(browser, context, test_data, target_url="https://laravel.stacxuat.com/Transactions")
    page.wait_for_timeout(2500)

    # Click Data Extraction tab
    log("[Step 1] Switching to 'Data Extraction' Workflow Tab...")
    page.locator(".TransactionWorkflowTab li:has-text('Data Extraction'), .TransactionWorkflowTab a:has-text('Data Extraction')").first.click()
    page.wait_for_timeout(2500)

    # Filter by stacx_id
    log(f"[Step 2] Filtering by STACX ID '{stacx_id}'...")
    search_box = page.locator("#custom_search_value")
    search_box.fill("")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(3000)

    # Locate row and action button
    target_row = page.locator(f"#table_allloans tbody tr:has-text('{stacx_id}')").first
    target_row.wait_for(state="visible", timeout=15000)
    log(f" -> Found row: {target_row.inner_text().strip().replace(chr(10), ' | ')}")

    action_btn = target_row.locator("td").last.locator("a, button, i.fa-ellipsis-v, .dropdown-toggle").first
    log(" -> Clicking action 3-dots...")
    action_btn.click()
    page.wait_for_timeout(1000)

    ext_link = page.locator(".dropdown-menu.show a:has-text('Data Extraction'), .dropdown-menu:visible a:has-text('Data Extraction')").first
    ext_link.wait_for(state="visible", timeout=10000)
    log(" -> Clicking 'Data Extraction' menu item...")
    ext_link.click()

    # Wait for navigation to /DataEntry/
    log(" -> Waiting for URL to match **/DataEntry/** ...")
    page.wait_for_url("**/DataEntry/**", timeout=35000)
    log(f" -> Reached Extraction Screen! URL: {page.url}")
    page.wait_for_timeout(4000)

    # Check for Edit Mode modal if present (similar to Indexing screen)
    edit_mode_btn = page.locator("button:has-text('Open in Edit Mode'), .btn-success:has-text('Edit'), .btn:has-text('Open in Edit Mode')").first
    try:
        if edit_mode_btn.is_visible(timeout=5000):
            log(" -> 'Open in Edit Mode' modal detected! Clicking...")
            edit_mode_btn.click()
            page.wait_for_timeout(2000)
    except Exception:
        pass

    # Save screenshot of the loaded extraction screen
    screenshot_path = "scratch/extraction_screen_loaded.png"
    page.screenshot(path=screenshot_path)
    log(f" -> Screenshot saved to: {screenshot_path}")

    # Inspect the DOM of the extraction screen
    info = page.evaluate("""() => {
        return {
            title: document.title,
            url: window.location.href,
            buttons: Array.from(document.querySelectorAll('button, a.btn, input[type=\"button\"], input[type=\"submit\"]')).map(b => ({
                id: b.id,
                text: b.innerText.trim(),
                className: b.className,
                onclick: b.getAttribute('onclick') || ''
            })).filter(b => b.text.length > 0 || b.id.length > 0),
            headings: Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, .title, .card-title, .header-title')).map(h => h.innerText.trim()).filter(t => t.length > 0),
            forms: Array.from(document.querySelectorAll('form')).map(f => ({ id: f.id, name: f.name, action: f.action })),
            completeButtons: Array.from(document.querySelectorAll('*')).filter(el => {
                const txt = (el.innerText || '').toLowerCase();
                const id = (el.id || '').toLowerCase();
                return (txt.includes('complete') || id.includes('complete')) && (el.tagName === 'BUTTON' || el.tagName === 'A' || el.tagName === 'INPUT');
            }).map(el => ({ tag: el.tagName, id: el.id, text: el.innerText.trim(), className: el.className }))
        };
    }""")
    log(f" -> Title: {info['title']}")
    log(f" -> Headings: {info['headings']}")
    log(f" -> Extraction Complete Candidate Buttons: {info['completeButtons']}")
    log(f" -> All Buttons Count: {len(info['buttons'])}")
    for b in info['buttons']:
        log(f"    Button: id='{b['id']}' text='{b['text']}' class='{b['className']}' onclick='{b['onclick']}'")

    browser.close()
