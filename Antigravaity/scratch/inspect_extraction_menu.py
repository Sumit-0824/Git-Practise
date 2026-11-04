import sys
import time
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
    page.wait_for_timeout(3000)

    # Click Data Extraction workflow tab
    log("\n[Step 1] Switching to 'Data Extraction' Workflow Tab...")
    ext_tab = page.locator(".TransactionWorkflowTab li:has-text('Data Extraction'), .TransactionWorkflowTab a:has-text('Data Extraction')").first
    ext_tab.wait_for(state="visible", timeout=20000)
    ext_tab.click()
    page.wait_for_timeout(3000)
    log(" -> Clicked 'Data Extraction' tab.")

    # Filter STACX ID
    log(f"\n[Step 2] Filtering table for STACX ID: '{stacx_id}'...")
    search_box = page.locator("#custom_search_value")
    search_box.fill("")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(3500)
    try:
        page.locator("#table_allloans_processing, .dataTables_processing, .processingCard").wait_for(state="hidden", timeout=15000)
    except Exception:
        pass
    page.wait_for_timeout(1500)

    # Locate target row
    target_row = page.locator(f"#table_allloans tbody tr:has-text('{stacx_id}')").first
    target_row.wait_for(state="visible", timeout=15000)
    log(f" -> Found row: {target_row.inner_text().strip().replace(chr(10), ' | ')}")

    # Check 3-dots action button
    action_btn = target_row.locator("td").last.locator("a, button, i.fa-ellipsis-v, .dropdown-toggle").first
    log(" -> Clicking 3-dots action button...")
    action_btn.click()
    page.wait_for_timeout(1500)

    # Read dropdown menu items
    menu_items = page.locator(".dropdown-menu.show a, .dropdown-menu:visible a, .dropdown-menu.show button, .dropdown-menu:visible button").all()
    items_info = []
    for m in menu_items:
        items_info.append({
            "text": m.inner_text().strip(),
            "href": m.get_attribute("href") or "",
            "onclick": m.get_attribute("onclick") or "",
            "class": m.get_attribute("class") or ""
        })
    log(f" -> Dropdown menu items: {items_info}")

    # Also check if clicking on the order / loan number directly does anything or if dropdown has extraction
    # Find item matching Extraction
    ext_menu_item = page.locator(".dropdown-menu.show a:has-text('Extraction'), .dropdown-menu:visible a:has-text('Extraction'), .dropdown-menu.show a:has-text('Data Extraction'), .dropdown-menu:visible a:has-text('Data Extraction')").first
    if ext_menu_item.is_visible():
        log(f" -> Found extraction menu item: '{ext_menu_item.inner_text().strip()}', clicking...")
        ext_menu_item.click()
    else:
        log(" -> No 'Extraction' text in dropdown! Checking all items...")
        for info in items_info:
            log(f"    Item: {info}")
        if menu_items:
            log(f" -> Clicking first menu item: '{items_info[0]}'")
            menu_items[0].click()

    page.wait_for_timeout(5000)
    log(f" -> Current URL after click: {page.url}")
    page.screenshot(path="scratch/inside_extraction.png")

    # Inspect current page content and buttons
    dom_summary = page.evaluate("""() => {
        return {
            title: document.title,
            url: window.location.href,
            buttons: Array.from(document.querySelectorAll('button, a.btn, input[type=\"button\"], input[type=\"submit\"]')).map(b => ({
                id: b.id,
                text: b.innerText.trim(),
                className: b.className,
                onclick: b.getAttribute('onclick') || ''
            })).filter(b => b.text.length > 0 || b.id.length > 0),
            headings: Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, .title, .card-title')).map(h => h.innerText.trim()).filter(t => t.length > 0)
        };
    }""")
    log(f" -> Title: {dom_summary['title']}")
    log(f" -> Headings: {dom_summary['headings']}")
    log(f" -> Buttons found: {len(dom_summary['buttons'])}")
    for b in dom_summary['buttons']:
        log(f"    Button: id='{b['id']}' text='{b['text']}' class='{b['className']}' onclick='{b['onclick']}'")

    browser.close()
