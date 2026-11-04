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

    tabs = ["All Pending Track(s)", "Doc Check-In", "Classification", "Data Extraction"]
    for tab_name in tabs:
        print(f"\n--- Checking Tab: '{tab_name}' ---", flush=True)
        tab_loc = page.locator(f".TransactionWorkflowTab li:has-text('{tab_name}'), .TransactionWorkflowTab a:has-text('{tab_name}')").first
        try:
            tab_loc.click()
            page.wait_for_timeout(2500)
            search_box = page.locator("#custom_search_value")
            search_box.fill("")
            search_box.fill(order_number)
            search_box.press("Enter")
            page.wait_for_timeout(3000)
            rows = page.locator("#table_allloans tbody tr").all()
            for r in rows:
                txt = r.inner_text().strip().replace('\n', ' | ')
                if "no matching records" not in txt.lower():
                    print(f"[{tab_name}] Row:", txt, flush=True)
        except Exception as e:
            print(f"Error checking {tab_name}: {e}", flush=True)

    page.screenshot(path="scratch/check_tabs_current.png")
    browser.close()
