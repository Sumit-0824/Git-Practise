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

    # Classification tab
    cls_tab = page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first
    cls_tab.click()
    page.wait_for_timeout(2500)

    # Filter STACX ID
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(2500)

    # Row Action -> Classification
    row = page.locator("#table_allloans tbody tr, table.dataTable tbody tr").first
    action_trigger = row.locator("td").last.locator("a.btn-icon, .dropdown-toggle, i.fa-ellipsis-v, a").first
    action_trigger.click()
    page.wait_for_timeout(1000)

    cls_item = page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first
    cls_item.click()

    # Wait for classification screen
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector("#stackingcomplete", state="visible", timeout=30000)
    page.wait_for_timeout(4000)

    # Check AllBoxSelect element details and unclassified pages
    details = page.evaluate("""() => {
        const allBox = document.querySelector('#AllBoxSelect');
        const allBoxParent = allBox ? allBox.parentElement.outerHTML : 'none';

        // Find unclassified container
        const unclassContainer = document.querySelector('#unclassifiedPageContainerId, [id*="unclassified"], [class*="unclassified"]');
        const unclassHtml = unclassContainer ? unclassContainer.innerHTML.slice(0, 1000) : 'none';

        // Look for items with "Page 1", "Page 2" in right side
        const pageEls = Array.from(document.querySelectorAll('*')).filter(el => {
            return el.children.length === 0 && /^Page\\s*\\d+$/i.test(el.innerText && el.innerText.trim());
        }).map(el => ({
            tag: el.tagName,
            cls: el.className,
            id: el.id,
            text: el.innerText.trim(),
            parentHtml: el.parentElement ? el.parentElement.outerHTML.slice(0, 200) : ''
        }));

        // First doc type elements and icons
        const firstDocType = document.querySelector('.Questionlist_Document_type');
        let docTypeContext = '';
        if (firstDocType && firstDocType.parentElement) {
            docTypeContext = firstDocType.parentElement.outerHTML.slice(0, 500);
        }

        // Green plus icons
        const addIcons = Array.from(document.querySelectorAll('.AddInstance, [class*="AddInstance"], [class*="add-instance"], .bi-plus-circle, .fa-plus-circle, i[class*="plus"], svg[class*="plus"]')).slice(0, 5).map(el => ({
            tag: el.tagName,
            cls: el.className,
            outer: el.outerHTML
        }));

        return {
            allBoxParent,
            unclassHtml,
            pageElsCount: pageEls.length,
            pageElsSample: pageEls.slice(0, 5),
            docTypeContext,
            addIcons
        };
    }""")

    import pprint
    pprint.pprint(details)

    browser.close()
