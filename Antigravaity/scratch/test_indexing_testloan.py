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
    page.wait_for_timeout(4000)

    print("Active URL:", page.url, flush=True)

    # Check for Edit Mode modal
    edit_mode_btn = page.locator("button:has-text('Open in Edit Mode'), .btn-success:has-text('Edit'), .btn:has-text('Open in Edit Mode')").first
    try:
        if edit_mode_btn.is_visible(timeout=5000):
            print("Clicking Open in Edit Mode...", flush=True)
            edit_mode_btn.click()
            page.wait_for_timeout(2000)
    except:
        pass

    page.wait_for_timeout(5000)
    page.screenshot(path="scratch/indexing_testloan.png")

    metrics = page.evaluate("""() => {
        return {
            title: document.title,
            total: document.querySelector('#Total_Count')?.innerText?.trim() || '',
            classi: document.querySelector('#Classi_Count')?.innerText?.trim() || '',
            unclass: document.querySelectorAll('#unclassifiedPageContainerId li').length,
            bodySnippet: document.body.innerText.substring(0, 300)
        };
    }""")
    print("Metrics:", metrics, flush=True)

    browser.close()
