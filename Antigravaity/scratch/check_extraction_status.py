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

    # Click Data Extraction tab
    page.locator(".TransactionWorkflowTab li:has-text('Data Extraction'), .TransactionWorkflowTab a:has-text('Data Extraction')").first.click()
    page.wait_for_timeout(2500)

    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(4000)

    rows = page.locator("#table_allloans tbody tr").all()
    for r in rows:
        print("Data Extraction Row:", r.inner_text().strip().replace('\n', ' | '), flush=True)

    page.screenshot(path="data_extraction_ready.png")
    browser.close()
