import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, ensure_authenticated_page, load_test_data

test_data = load_test_data()
indexing_url = "https://laravel.stacxuat.com/Indexing/index/YTMzMjUxYmFiOTQ5ZWJiZWM3OWZhM2JkNjNhMDVkM2Z%2BMzUwMjc4"

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = ensure_authenticated_page(browser, context, test_data, target_url=indexing_url)
    page.wait_for_timeout(3000)

    btn = page.locator("#DocumentCheckIncomplete").first
    print("Clicking #DocumentCheckIncomplete...", flush=True)
    btn.click()
    page.wait_for_timeout(2500)

    # Check for sweetalert
    swal_btn = page.locator(".swal-modal .swal-button--catch, .swal-button:has-text('Complete'), .swal-button:has-text('OK'), .swal-button").first
    if swal_btn.is_visible():
        print("Swal visible! Title/Text:", page.locator(".swal-title, .swal-text").all_text_contents(), flush=True)
        print("Clicking confirm button:", swal_btn.inner_text(), flush=True)
        swal_btn.click()
        page.wait_for_timeout(4000)

    print("URL after click:", page.url, flush=True)
    page.screenshot(path="scratch/after_doc_checkin_complete.png")

    # Check Transactions status
    page.goto("https://laravel.stacxuat.com/Transactions", wait_until="domcontentloaded")
    page.wait_for_timeout(3000)
    search_box = page.locator("#custom_search_value")
    search_box.fill("TestloanA211026001")
    search_box.press("Enter")
    page.wait_for_timeout(3000)
    rows = page.locator("#table_allloans tbody tr").all()
    for r in rows:
        print("Updated Row in Transactions:", r.inner_text().strip().replace('\n', ' | '), flush=True)

    browser.close()
