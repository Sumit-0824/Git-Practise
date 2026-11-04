import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, ensure_authenticated_page, load_test_data

test_data = load_test_data()

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = ensure_authenticated_page(browser, context, test_data, target_url="https://laravel.stacxuat.com/DocumentCheckList/index/NmZjMTRkNzgwMGU0MTc3YTlkY2I4Y2IwMzEyZjM5MmF%2BMzUwMjc4")
    page.wait_for_timeout(3000)

    # Click Update button
    print("Clicking Update button...", flush=True)
    update_btn = page.locator("button.single_submit:has-text('Update')").first
    update_btn.click()
    page.wait_for_timeout(4000)

    # Check for confirmation popup or redirect
    swal_btn = page.locator(".swal-button, button:has-text('OK')").first
    if swal_btn.is_visible():
        print("Swal popup:", page.locator(".swal-title, .swal-text").all_text_contents(), flush=True)
        swal_btn.click()
        page.wait_for_timeout(3000)

    print("URL after update:", page.url, flush=True)
    page.screenshot(path="scratch/after_doc_checkin_update.png")
    browser.close()
