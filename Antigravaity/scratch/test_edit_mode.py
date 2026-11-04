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

    # Click Classification
    page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first.click()
    page.wait_for_url("**/Indexing/**", timeout=30000)
    print("Navigated to Indexing!", flush=True)

    # Handle 'Open in Edit Mode' popup if present
    edit_mode_btn = page.locator("button:has-text('Open in Edit Mode'), .swal2-confirm:has-text('Edit'), .btn:has-text('Open in Edit Mode')").first
    try:
        edit_mode_btn.wait_for(state="visible", timeout=6000)
        print("Detected 'Open in Edit Mode' popup! Clicking it...", flush=True)
        edit_mode_btn.click()
    except Exception as e:
        print("No edit mode popup appeared (or already dismissed).", flush=True)

    # Now wait for the unclassified container to populate
    print("Waiting for classification data to populate...", flush=True)
    page.wait_for_timeout(7000)
    page.screenshot(path="scratch/after_edit_mode.png")

    # Inspect total count, classified count, unclassified container
    res = page.evaluate("""() => {
        const total = document.querySelector('#Total_Count')?.innerText?.trim() || '';
        const classi = document.querySelector('#Classi_Count')?.innerText?.trim() || '';
        const ol = document.querySelector('#unclassifiedPageContainerId');
        const liList = ol ? Array.from(ol.querySelectorAll('li')).map(li => ({
            id: li.id,
            cls: li.className,
            text: li.innerText.trim().replace(/\\s+/g, ' '),
            html: li.outerHTML.slice(0, 300)
        })) : [];

        const badges = Array.from(document.querySelectorAll('.page-cofidence-legends-range button, .filter-extraction')).map(b => b.innerText.trim().replace(/\\s+/g, ' '));

        return {
            total,
            classi,
            unclassifiedCount: liList.length,
            badges,
            sampleLi: liList.slice(0, 5)
        };
    }""")

    import pprint
    pprint.pprint(res)

    browser.close()
