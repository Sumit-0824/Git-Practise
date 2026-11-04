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
    
    # Wait for unclassifiedPageContainerId to have li items or wait 8 seconds
    print("Waiting for #unclassifiedPageContainerId...", flush=True)
    page.wait_for_timeout(8000)

    data = page.evaluate("""() => {
        const classiCount = document.querySelector('#Classi_Count')?.innerText?.trim() || '';
        const totalCount = document.querySelector('#Total_Count')?.innerText?.trim() || '';
        
        const ol = document.querySelector('#unclassifiedPageContainerId');
        const items = ol ? Array.from(ol.querySelectorAll('li')).map(li => ({
            id: li.id,
            cls: li.className,
            text: li.innerText.trim().replace(/\\s+/g, ' '),
            html: li.innerHTML.slice(0, 300)
        })) : [];

        // Check if there are checkboxes or select all
        const olCheckboxes = ol ? Array.from(ol.querySelectorAll('input[type="checkbox"]')).map(cb => ({
            id: cb.id,
            cls: cb.className,
            checked: cb.checked
        })) : [];

        // Also check if there's any select all button or icon in the unclassified card
        const card = ol ? ol.closest('.card') || ol.parentElement : null;

        return {
            classiCount,
            totalCount,
            itemsCount: items.length,
            itemsSample: items.slice(0, 5),
            olCheckboxesSample: olCheckboxes.slice(0, 5)
        };
    }""")

    import pprint
    pprint.pprint(data)

    browser.close()
