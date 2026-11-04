import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, load_test_data

test_data = load_test_data()
stacx_id = test_data.get('stacx_id', 'MCL72626122406')

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = context.new_page()
    page.goto('https://laravel.stacxuat.com/Transactions', wait_until='domcontentloaded')
    page.wait_for_timeout(4000)
    
    # Switch to Classification tab & filter
    page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first.click()
    page.wait_for_timeout(2500)
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(3000)

    # Click action -> Classification
    target_row = page.locator(f"#table_allloans tbody tr:has-text('{stacx_id}')").first
    target_row.locator("td").last.locator(".dropdown-toggle, a.btn-icon, a").first.click()
    page.wait_for_timeout(1000)
    page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first.click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(8000)

    # Take screenshot and save HTML
    page.screenshot(path="scratch/current_indexing.png")
    with open("scratch/current_indexing.html", "w", encoding="utf-8") as f:
        f.write(page.content())
    print("Saved current_indexing.png and current_indexing.html", flush=True)

    browser.close()
