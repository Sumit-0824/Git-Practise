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
    page.wait_for_timeout(2500)

    # Filter STACX ID
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(2500)

    # Click action -> Classification
    row = page.locator("#table_allloans tbody tr, table.dataTable tbody tr").first
    row.locator("td").last.locator("a.btn-icon, .dropdown-toggle, i.fa-ellipsis-v, a").first.click()
    page.wait_for_timeout(1000)

    page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first.click()
    page.wait_for_selector("#stackingcomplete", state="visible", timeout=30000)
    page.wait_for_timeout(5000)

    # Inspect the exact HTML of the unclassified section and list
    res = page.evaluate("""() => {
        // Find element containing text 'Unclassified'
        const h5 = Array.from(document.querySelectorAll('h5')).find(e => e.innerText && e.innerText.trim() === 'Unclassified');
        if (!h5) return { error: 'h5 Unclassified not found' };

        const card = h5.closest('.card') || h5.parentElement.parentElement;
        
        // Find all elements inside card
        const allItems = Array.from(card.querySelectorAll('*')).map(el => ({
            tag: el.tagName,
            id: el.id,
            cls: el.className,
            text: el.innerText ? el.innerText.trim() : ''
        }));

        // Find list items or divs that have 'Page '
        const pageItems = Array.from(card.querySelectorAll('li, div, p, span, tr')).filter(el => 
            el.innerText && /Page\\s*\\d+/i.test(el.innerText) && el.innerText.length < 50
        ).slice(0, 10).map(el => ({
            tag: el.tagName,
            cls: el.className,
            html: el.outerHTML
        }));

        return {
            cardTag: card.tagName,
            cardClass: card.className,
            totalChildren: allItems.length,
            pageItemsCount: pageItems.length,
            pageItemsSample: pageItems
        };
    }""")

    import pprint
    pprint.pprint(res)

    browser.close()
