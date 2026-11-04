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
    page.wait_for_timeout(4000)
    
    # Switch to Classification tab & filter
    page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first.click()
    page.wait_for_timeout(2500)
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(2500)

    # Open action menu & click Classification
    row = page.locator("#table_allloans tbody tr, table.dataTable tbody tr").first
    row.locator("td").last.locator("a.btn-icon, .dropdown-toggle, a").first.click()
    page.wait_for_timeout(1000)
    page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first.click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(7000)

    res = page.evaluate("""() => {
        const unclassHeading = Array.from(document.querySelectorAll('h5')).find(e => e.innerText && e.innerText.trim() === 'Unclassified');
        const card = unclassHeading ? unclassHeading.closest('.card') : null;
        if (!card) return 'Card not found';
        
        // Print all child elements inside the card
        const childrenInfo = Array.from(card.querySelectorAll('*')).map(el => ({
            tag: el.tagName,
            cls: el.className,
            id: el.id,
            text: el.children.length === 0 ? el.innerText.trim() : ''
        })).filter(x => x.text !== '' || x.id !== '' || x.cls.includes('page') || x.cls.includes('check'));
        
        return {
            totalElements: childrenInfo.length,
            elements: childrenInfo.slice(0, 30)
        };
    }""")

    import pprint
    pprint.pprint(res)

    browser.close()
