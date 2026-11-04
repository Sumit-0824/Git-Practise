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
    page.wait_for_timeout(3500)

    # Target row
    row = page.locator(f"#table_allloans tbody tr:has-text('{stacx_id}')").first
    row.locator("td").last.locator("a, button, i.fa-ellipsis-v").first.click()
    page.wait_for_timeout(1000)

    page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first.click()
    page.wait_for_url("**/Indexing/**", timeout=30000)

    # Handle Edit mode
    edit_btn = page.locator("button:has-text('Open in Edit Mode'), .btn:has-text('Open in Edit Mode')").first
    try:
        edit_btn.wait_for(state="visible", timeout=6000)
        edit_btn.click()
    except:
        pass

    # Wait for unclassifiedPageContainerId li to exist
    print("Waiting for #unclassifiedPageContainerId li...", flush=True)
    page.wait_for_selector("#unclassifiedPageContainerId li", timeout=20000)
    print("Found unclassified li items!", flush=True)

    details = page.evaluate("""() => {
        const li = document.querySelector('#unclassifiedPageContainerId li');
        
        // Find all checkboxes in the unclassified list
        const cbs = Array.from(document.querySelectorAll('#unclassifiedPageContainerId input[type="checkbox"]')).map(cb => ({
            id: cb.id,
            cls: cb.className,
            name: cb.name,
            value: cb.value,
            checked: cb.checked
        }));

        // Find icons/arrows in first li
        const icons = li ? Array.from(li.querySelectorAll('i, svg, a, span, button')).map(el => ({
            tag: el.tagName,
            cls: el.className,
            title: el.getAttribute('title') || '',
            id: el.id
        })) : [];

        // Check jQuery click handlers on firstDocType
        const firstDocType = document.querySelector('.Questionlist_Document_type');
        const dtEvents = window.$ ? window.$._data(firstDocType, 'events') : null;

        // Check document-level click handlers or delegated handlers
        const docEvents = window.$ ? window.$._data(document, 'events') : null;
        let delegatedClicks = [];
        if (docEvents && docEvents.click) {
            delegatedClicks = docEvents.click.map(h => ({
                selector: h.selector,
                namespace: h.namespace
            })).filter(h => h.selector);
        }

        return {
            liHtml: li ? li.outerHTML : '',
            checkboxCount: cbs.length,
            checkboxSample: cbs.slice(0, 5),
            iconsInLi: icons,
            delegatedClicks: delegatedClicks.slice(0, 20)
        };
    }""")

    import pprint
    pprint.pprint(details)

    browser.close()
