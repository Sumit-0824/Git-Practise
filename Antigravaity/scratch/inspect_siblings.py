import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, ensure_authenticated_page, load_test_data

test_data = load_test_data()
stacx_id = test_data.get('stacx_id', 'MCL72626122406')

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = ensure_authenticated_page(browser, context, test_data, target_url="https://laravel.stacxuat.com/Transactions")
    page.wait_for_timeout(3000)

    # Click Classification workflow tab
    page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first.click()
    page.wait_for_timeout(2000)

    # Filter STACX ID
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(2000)

    # Click action -> Classification
    row = page.locator("#table_allloans tbody tr, table.dataTable tbody tr").first
    row.locator("td").last.locator("a.btn-icon, .dropdown-toggle, i.fa-ellipsis-v, a").first.click()
    page.wait_for_timeout(1000)

    page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first.click()
    page.wait_for_selector("#stackingcomplete", state="visible", timeout=30000)
    page.wait_for_timeout(4000)

    res = page.evaluate("""() => {
        const h5 = document.querySelector('h5.pd-l');
        const card = h5 ? h5.closest('.card') : null;
        if (!card) return 'no card';

        const parent = card.parentElement;
        const siblings = Array.from(parent.children).map(c => ({
            tag: c.tagName,
            cls: c.className,
            id: c.id,
            textSample: c.innerText ? c.innerText.trim().slice(0, 100).replace(/\\s+/g, ' ') : ''
        }));

        // Search for element with text containing 'Page 1' or 'Page 2' anywhere in document
        const allEls = Array.from(document.querySelectorAll('*')).filter(el => {
            const t = el.innerText || '';
            return el.children.length === 0 && (t.trim() === 'Page 1' || t.trim() === 'Page 2');
        }).map(el => ({
            tag: el.tagName,
            cls: el.className,
            id: el.id,
            text: el.innerText.trim(),
            parentChain: [el.parentElement ? el.parentElement.tagName + '.' + el.parentElement.className : '']
        }));

        return {
            parentTag: parent.tagName,
            parentCls: parent.className,
            siblings,
            allEls
        };
    }""")

    import pprint
    pprint.pprint(res)

    browser.close()
