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

    # 1. Search under All Pending Orders
    print("\n--- Checking All Pending Orders ---", flush=True)
    all_tab = page.locator(".TransactionWorkflowTab li, .TransactionWorkflowTab a").first
    all_tab.click()
    page.wait_for_timeout(2000)
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(3000)
    rows_all = page.locator("#table_allloans tbody tr").all()
    for r in rows_all:
        print("All Tab Row:", r.inner_text().strip().replace('\n', ' | '), flush=True)

    # 2. Search under Classification
    print("\n--- Checking Classification Tab ---", flush=True)
    cls_tab = page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first
    cls_tab.click()
    page.wait_for_timeout(2000)
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(3000)
    rows_cls = page.locator("#table_allloans tbody tr").all()
    for r in rows_cls:
        print("Cls Tab Row:", r.inner_text().strip().replace('\n', ' | '), flush=True)

    # 3. Search under Data Extraction
    print("\n--- Checking Data Extraction Tab ---", flush=True)
    ext_tab = page.locator(".TransactionWorkflowTab li:has-text('Data Extraction'), .TransactionWorkflowTab a:has-text('Data Extraction')").first
    ext_tab.click()
    page.wait_for_timeout(2000)
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(3000)
    rows_ext = page.locator("#table_allloans tbody tr").all()
    for r in rows_ext:
        print("Ext Tab Row:", r.inner_text().strip().replace('\n', ' | '), flush=True)

    page.screenshot(path="scratch/check_all_tabs.png")
    browser.close()
