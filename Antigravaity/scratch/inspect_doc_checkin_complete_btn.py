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

    btn_info = page.evaluate("""() => {
        const btns = Array.from(document.querySelectorAll('button, a.btn')).map(b => ({
            id: b.id,
            text: b.innerText.trim(),
            className: b.className,
            onclick: b.getAttribute('onclick')
        }));
        return btns;
    }""")
    for b in btn_info:
        if 'check' in b['text'].lower() or 'complete' in b['text'].lower():
            print("Target Button:", b, flush=True)

    browser.close()
