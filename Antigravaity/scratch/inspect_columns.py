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

    cols_info = page.evaluate("""() => {
        // Find all main columns
        const cols = Array.from(document.querySelectorAll('[class*="col-"]')).filter(c => {
            return c.parentElement && c.parentElement.classList.contains('row');
        }).map(c => ({
            cls: c.className,
            id: c.id,
            textSnippet: c.innerText ? c.innerText.trim().slice(0, 80).replace(/\\s+/g, ' ') : ''
        }));

        // Search specifically for the right panel: "Page Confidence Legends"
        const legendHeading = Array.from(document.querySelectorAll('*')).find(el => 
            el.innerText && el.innerText.trim() === 'Page Confidence Legends'
        );
        let rightPanelHtml = '';
        if (legendHeading) {
            const panel = legendHeading.closest('.card') || legendHeading.parentElement.parentElement;
            rightPanelHtml = panel ? panel.outerHTML.slice(0, 1000) : '';
        }

        return {
            cols,
            legendFound: !!legendHeading,
            rightPanelHtml
        };
    }""")

    import pprint
    pprint.pprint(cols_info)

    browser.close()
