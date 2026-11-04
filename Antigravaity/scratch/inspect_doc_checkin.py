import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, ensure_authenticated_page, load_test_data

test_data = load_test_data()
stacx_id = test_data.get("stacx_id", "MCL72926122422")
order_number = test_data.get("order_number", "TestloanA211026001")

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = ensure_authenticated_page(browser, context, test_data, target_url="https://laravel.stacxuat.com/Transactions")
    page.wait_for_timeout(3000)

    # Click Doc Check-In tab
    doc_tab = page.locator(".TransactionWorkflowTab li:has-text('Doc Check-In'), .TransactionWorkflowTab a:has-text('Doc Check-In')").first
    doc_tab.click()
    page.wait_for_timeout(2500)

    search_box = page.locator("#custom_search_value")
    search_box.fill(order_number)
    search_box.press("Enter")
    page.wait_for_timeout(3000)

    row = page.locator(f"#table_allloans tbody tr:has-text('{order_number}')").first
    print("Doc Check-In Row Text:", row.inner_text().strip().replace('\n', ' | '), flush=True)

    # Click action 3-dots
    action_btn = row.locator("td").last.locator("a, button, i.fa-ellipsis-v, .dropdown-toggle").first
    action_btn.click()
    page.wait_for_timeout(1500)

    menu_items = page.locator(".dropdown-menu.show a, .dropdown-menu:visible a, .dropdown-menu.show button, .dropdown-menu:visible button").all()
    for m in menu_items:
        print(f"Menu Item: text='{m.inner_text().strip()}' href='{m.get_attribute('href')}' class='{m.get_attribute('class')}'", flush=True)

    page.screenshot(path="scratch/doc_checkin_menu.png")
    browser.close()
