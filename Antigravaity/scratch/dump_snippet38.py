import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, ensure_authenticated_page, load_test_data

test_data = load_test_data()
stacx_id = test_data.get('stacx_id', 'MCL72626122406')

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = ensure_authenticated_page(browser, context, test_data, target_url="https://laravel.stacxuat.com/Transactions")
    page.wait_for_timeout(3000)

    # Click Classification workflow tab
    page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first.click()
    page.wait_for_timeout(2000)

    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(3500)

    row = page.locator(f"#table_allloans tbody tr:has-text('{stacx_id}')").first
    row.locator("td").last.locator("a, button, i.fa-ellipsis-v").first.click()
    page.wait_for_timeout(1000)

    page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first.click()
    page.wait_for_url("**/Indexing/**", timeout=30000)

    edit_btn = page.locator("button:has-text('Open in Edit Mode'), .btn:has-text('Open in Edit Mode')").first
    try:
        edit_btn.wait_for(state="visible", timeout=6000)
        edit_btn.click()
    except:
        pass

    page.wait_for_function(
        "() => document.querySelector('#Total_Count') && document.querySelector('#Total_Count').innerText.trim() !== ''",
        timeout=40000
    )

    script_content = page.evaluate("""() => {
        const scripts = Array.from(document.querySelectorAll('script')).map(s => s.innerText).filter(t => t.length > 0);
        const s38 = scripts[38];
        const lines = s38.split('\\n');
        return lines.slice(480, 720).join('\\n');
    }""")

    with open("scratch/script38_snippet.js", "w", encoding="utf-8") as f:
        f.write(script_content)

    print("Saved script 38 snippet! Length:", len(script_content), flush=True)

    browser.close()
