import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, ensure_authenticated_page, load_test_data

test_data = load_test_data()
order_number = test_data.get("order_number", "TestloanA211026001")

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = ensure_authenticated_page(browser, context, test_data, target_url="https://laravel.stacxuat.com/Transactions")
    page.wait_for_timeout(2500)

    # Click Doc Check-In tab
    doc_tab = page.locator(".TransactionWorkflowTab li:has-text('Doc Check-In'), .TransactionWorkflowTab a:has-text('Doc Check-In')").first
    doc_tab.click()
    page.wait_for_timeout(2500)

    search_box = page.locator("#custom_search_value")
    search_box.fill(order_number)
    search_box.press("Enter")
    page.wait_for_timeout(3000)

    row = page.locator(f"#table_allloans tbody tr:has-text('{order_number}')").first
    action_btn = row.locator("td").last.locator("a, button, i.fa-ellipsis-v, .dropdown-toggle").first
    action_btn.click()
    page.wait_for_timeout(1000)

    # Click Doc Check-In menu item
    doc_link = page.locator(".dropdown-menu.show a:has-text('Doc Check-In'), .dropdown-menu:visible a:has-text('Doc Check-In')").first
    doc_link.click()

    page.wait_for_timeout(6000)
    print("Active URL:", page.url, flush=True)
    page.screenshot(path="scratch/doc_checklist_screen.png")

    info = page.evaluate("""() => {
        return {
            title: document.title,
            headings: Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, .title')).map(h => h.innerText.trim()).filter(t => t.length > 0),
            buttons: Array.from(document.querySelectorAll('button, a.btn, input[type=\"button\"]')).map(b => ({
                id: b.id,
                text: b.innerText.trim(),
                className: b.className
            })).filter(b => b.text.length > 0 || b.id.length > 0)
        };
    }""")
    print("Title:", info['title'], flush=True)
    print("Headings:", info['headings'], flush=True)
    print("Buttons:", info['buttons'], flush=True)

    browser.close()
