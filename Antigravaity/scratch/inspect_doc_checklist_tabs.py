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

    tabs = page.evaluate("""() => {
        return Array.from(document.querySelectorAll('a, button')).filter(el => {
            const txt = el.innerText.trim();
            return ['Classification', 'Data Extraction', 'Track Info', 'Doc Check-In'].includes(txt);
        }).map(el => ({
            text: el.innerText.trim(),
            href: el.getAttribute('href'),
            onclick: el.getAttribute('onclick'),
            className: el.className
        }));
    }""")
    print("Tabs on DocCheckList:", tabs, flush=True)

    # Also check Transactions to see what status MCL72926122422 has now
    page.goto("https://laravel.stacxuat.com/Transactions", wait_until="domcontentloaded")
    page.wait_for_timeout(3000)
    search_box = page.locator("#custom_search_value")
    search_box.fill("TestloanA211026001")
    search_box.press("Enter")
    page.wait_for_timeout(3000)
    rows = page.locator("#table_allloans tbody tr").all()
    for r in rows:
        print("Transactions Row:", r.inner_text().strip().replace('\n', ' | '), flush=True)

    browser.close()
