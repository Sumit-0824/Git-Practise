import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, load_test_data

test_data = load_test_data()
stacx_id = test_data.get('stacx_id', 'MCL72626122406')

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = context.new_page()
    page.goto('https://laravel.stacxuat.com/Transactions', wait_until='domcontentloaded')
    page.wait_for_timeout(3500)

    # Classification tab
    page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first.click()
    page.wait_for_timeout(2000)

    # Filter STACX ID
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(2000)

    # Row Action -> Classification
    row = page.locator("#table_allloans tbody tr, table.dataTable tbody tr").first
    row.locator("td").last.locator("a.btn-icon, .dropdown-toggle, i.fa-ellipsis-v, a").first.click()
    page.wait_for_timeout(1000)

    page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first.click()
    page.wait_for_selector("#stackingcomplete", state="visible", timeout=30000)
    page.wait_for_timeout(4000)

    # Look for the container of Unclassified
    unclass_info = page.evaluate("""() => {
        // Find heading with Unclassified
        const headings = Array.from(document.querySelectorAll('*')).filter(el => 
            el.innerText && el.innerText.trim().startsWith('Unclassified') && el.children.length <= 4
        );
        
        let containerHtml = '';
        if (headings.length > 0) {
            const h = headings[0];
            const parent = h.closest('.card, .card-body, div[class*="unclass"], div[id*="unclass"]') || h.parentElement.parentElement;
            containerHtml = parent ? parent.outerHTML.slice(0, 3000) : h.outerHTML;
        }

        return {
            headingsCount: headings.length,
            headings: headings.map(h => ({ tag: h.tagName, cls: h.className, text: h.innerText.trim() })),
            containerHtml
        };
    }""")

    import pprint
    pprint.pprint(unclass_info)

    browser.close()
