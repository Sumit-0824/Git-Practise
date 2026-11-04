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

    page.wait_for_selector("#unclassifiedPageContainerId li", timeout=20000)
    page.wait_for_timeout(3000)

    # Listen to toast messages and network
    def handle_toast(msg):
        print(f" [Console]: {msg.text}", flush=True)
    page.on("console", handle_toast)

    # Check the click handlers on .Questionlist_Document_type and .AddInstance
    handlers = page.evaluate("""() => {
        const el = document.querySelector('.Questionlist_Document_type');
        const plus = document.querySelector('.AddInstance.doc_type_plus');
        
        // Find what function is called when clicking doc type
        const elClick = el ? el.onclick ? el.onclick.toString() : 'no inline onclick' : 'none';
        const plusClick = plus ? plus.onclick ? plus.onclick.toString() : 'no inline onclick' : 'none';
        
        return {
            elClick,
            plusClick
        };
    }""")
    print("Inline click handlers:", handlers, flush=True)

    # Let's inspect delegated click handlers matching 'documenttypechoose' or 'doc_type'
    delegated = page.evaluate("""() => {
        const events = window.$ ? window.$._data(document, 'events') : null;
        if (!events || !events.click) return [];
        return events.click.map(h => ({ selector: h.selector, fn: h.handler.toString().slice(0, 300) }))
            .filter(h => h.selector && (h.selector.includes('documenttype') || h.selector.includes('doc_type') || h.selector.includes('AddInstance') || h.selector.includes('Questionlist')));
    }""")
    print("Delegated doc type handlers:", delegated, flush=True)

    browser.close()
