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

    # Classification tab
    page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first.click()
    page.wait_for_timeout(2000)

    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(2000)

    # Listen to responses
    def handle_response(response):
        if "ajax" in response.url.lower() or "indexing" in response.url.lower() or "get" in response.url.lower():
            if not any(ext in response.url.lower() for ext in ['.png', '.jpg', '.css', '.js', '.woff']):
                print(f" [Response] {response.status} {response.url[:90]}", flush=True)

    page.on("response", handle_response)

    # Click action -> Classification
    row = page.locator("#table_allloans tbody tr, table.dataTable tbody tr").first
    row.locator("td").last.locator("a.btn-icon, .dropdown-toggle, i.fa-ellipsis-v, a").first.click()
    page.wait_for_timeout(1000)

    page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first.click()
    print("Navigated to Indexing. Waiting 12 seconds...", flush=True)
    page.wait_for_timeout(12000)

    # Take screenshot of indexing page
    page.screenshot(path="scratch/live_indexing.png")
    print(f"Current URL: {page.url}", flush=True)

    # Inspect #unclassifiedPageContainerId innerHTML
    ol_html = page.evaluate("() => document.querySelector('#unclassifiedPageContainerId')?.innerHTML || 'null'")
    print(f"#unclassifiedPageContainerId HTML length: {len(ol_html)}", flush=True)
    if len(ol_html) > 50:
        print(f"Sample HTML:\n{ol_html[:500]}", flush=True)

    browser.close()
