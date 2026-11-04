import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, ensure_authenticated_page, load_test_data

test_data = load_test_data()

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = ensure_authenticated_page(browser, context, test_data, target_url="https://laravel.stacxuat.com/LandingPage")
    page.wait_for_timeout(3000)
    print("Active URL:", page.url, flush=True)
    print("Page Title:", page.title(), flush=True)
    
    # Check all visible links and buttons
    elements = page.evaluate("""() => {
        return Array.from(document.querySelectorAll('a, button, [role="button"], .card, .tile, .nav-link')).map(el => ({
            tag: el.tagName,
            text: el.innerText.trim(),
            href: el.getAttribute('href') || '',
            id: el.id,
            className: el.className
        })).filter(x => x.text.length > 0);
    }""")
    for el in elements:
        print(f"[{el['tag']}] text='{el['text']}' href='{el['href']}' id='{el['id']}'", flush=True)
    
    page.screenshot(path="scratch/landing_page.png")
    browser.close()
