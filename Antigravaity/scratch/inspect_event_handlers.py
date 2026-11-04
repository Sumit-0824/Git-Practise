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

    # Inspect jQuery event listeners and functions
    res = page.evaluate("""() => {
        // Find all script URLs loaded on this page
        const scripts = Array.from(document.querySelectorAll('script[src]')).map(s => s.src);
        
        // Check functions defined on window
        const windowFuncs = Object.keys(window).filter(k => 
            typeof window[k] === 'function' && 
            (k.toLowerCase().includes('index') || k.toLowerCase().includes('classif') || k.toLowerCase().includes('doc') || k.toLowerCase().includes('stack'))
        );

        // Check unclassified table rows
        const allBox = document.querySelector('#AllBoxSelect');
        const unclassTable = allBox ? allBox.closest('table') : null;
        let tableRows = [];
        if (unclassTable) {
            tableRows = Array.from(unclassTable.querySelectorAll('tbody tr')).slice(0, 5).map(tr => ({
                text: tr.innerText.trim().replace(/\\s+/g, ' '),
                html: tr.innerHTML.slice(0, 200)
            }));
        }

        // Check 1st doc type click action
        const firstDocType = document.querySelector('.Questionlist_Document_type');
        let docTypeAttrs = {};
        if (firstDocType) {
            Array.from(firstDocType.attributes).forEach(a => {
                docTypeAttrs[a.name] = a.value;
            });
        }

        return {
            windowFuncs,
            tableRows,
            docTypeAttrs,
            relevantScripts: scripts.filter(s => s.includes('stacx') || s.includes('custom') || s.includes('index'))
        };
    }""")

    import pprint
    pprint.pprint(res)

    browser.close()
