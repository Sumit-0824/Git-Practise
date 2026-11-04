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

    # Test clicking #AllBoxSelect or finding unclassified checkboxes
    info = page.evaluate("""() => {
        const allBox = document.querySelector('#AllBoxSelect');
        const isAllBoxVisible = allBox ? (allBox.offsetWidth > 0 && allBox.offsetHeight > 0) : false;
        
        // Find all checkboxes on the entire page
        const cbs = Array.from(document.querySelectorAll('input[type="checkbox"]')).map(cb => ({
            id: cb.id,
            className: cb.className,
            name: cb.name,
            visible: cb.offsetWidth > 0 && cb.offsetHeight > 0,
            checked: cb.checked,
            parentHtml: cb.parentElement ? cb.parentElement.outerHTML.slice(0, 150) : ''
        }));

        // Find elements with text 'Page 1', 'Page 2', etc.
        const page1 = Array.from(document.querySelectorAll('*')).find(el => el.innerText && el.innerText.trim() === 'Page 1');
        const page1Info = page1 ? {
            tag: page1.tagName,
            cls: page1.className,
            parent: page1.parentElement ? page1.parentElement.outerHTML.slice(0, 300) : ''
        } : null;

        return {
            allBoxExists: !!allBox,
            isAllBoxVisible,
            cbs,
            page1Info
        };
    }""")

    import pprint
    pprint.pprint(info)

    # Now let's try clicking AllBoxSelect if visible, or checkboxes
    all_box = page.locator("#AllBoxSelect")
    if all_box.is_visible():
        print("Clicking #AllBoxSelect...", flush=True)
        all_box.click()
        page.wait_for_timeout(1500)
        checked_count = page.evaluate("() => document.querySelectorAll('input[type=\"checkbox\"]:checked').length")
        print(f"Total checked checkboxes after clicking #AllBoxSelect: {checked_count}", flush=True)

    browser.close()
