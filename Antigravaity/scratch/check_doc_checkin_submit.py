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

    # Scroll down to bottom
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1500)
    page.screenshot(path="scratch/doc_checkin_bottom.png")

    # Find the update/submit button
    btn = page.locator("button.single_submit, button:has-text('Update')").first
    print("Update Button Visible:", btn.is_visible(), "Text:", btn.inner_text(), flush=True)

    browser.close()
