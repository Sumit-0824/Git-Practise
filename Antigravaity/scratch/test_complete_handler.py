import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import (
    launch_headed_browser,
    create_browser_context,
    ensure_authenticated_page,
    load_test_data,
    log,
)

test_data = load_test_data()
stacx_id = test_data.get("stacx_id", "MCL72626122406")

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = ensure_authenticated_page(browser, context, test_data, target_url="https://laravel.stacxuat.com/Transactions")
    page.wait_for_timeout(2500)

    # Click Data Extraction tab
    page.locator(".TransactionWorkflowTab li:has-text('Data Extraction'), .TransactionWorkflowTab a:has-text('Data Extraction')").first.click()
    page.wait_for_timeout(2500)

    # Filter by stacx_id
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(3000)

    # Click action -> Data Extraction
    target_row = page.locator(f"#table_allloans tbody tr:has-text('{stacx_id}')").first
    action_btn = target_row.locator("td").last.locator("a, button, i.fa-ellipsis-v, .dropdown-toggle").first
    action_btn.click()
    page.wait_for_timeout(1000)

    page.locator(".dropdown-menu.show a:has-text('Data Extraction'), .dropdown-menu:visible a:has-text('Data Extraction')").first.click()
    page.wait_for_url("**/DataEntry/**", timeout=35000)
    page.wait_for_timeout(4000)

    # Click #DataEntryComplete
    log("Clicking #DataEntryComplete...")
    complete_btn = page.locator("#DataEntryComplete").first
    complete_btn.click()
    page.wait_for_timeout(3000)

    page.screenshot(path="scratch/after_extraction_complete_click.png")
    log("Screenshot saved to scratch/after_extraction_complete_click.png")

    popup_info = page.evaluate("""() => {
        const swalModal = document.querySelector('.swal-modal');
        const modal = document.querySelector('.modal.show');
        return {
            swalTitle: document.querySelector('.swal-title')?.innerText || '',
            swalText: document.querySelector('.swal-text')?.innerText || '',
            swalButtons: Array.from(document.querySelectorAll('.swal-button')).map(b => ({
                text: b.innerText,
                className: b.className
            })),
            modalTitle: modal?.querySelector('.modal-title')?.innerText || '',
            modalBody: modal?.querySelector('.modal-body')?.innerText || '',
            modalButtons: Array.from(modal?.querySelectorAll('button') || []).map(b => b.innerText)
        };
    }""")
    log(f"Popup info: {popup_info}")

    browser.close()
