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
    print("Clicking Classification workflow tab...", flush=True)
    page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first.click()
    page.wait_for_timeout(2500)

    # Filter STACX ID
    search_box = page.locator("#custom_search_value")
    search_box.fill("")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    
    # Wait for table reload spinner to finish
    print("Waiting for datatable to update...", flush=True)
    page.wait_for_timeout(4000)
    try:
        page.locator(".dataTables_processing, .processingCard").wait_for(state="hidden", timeout=10000)
    except:
        pass

    # Find the target row
    row = page.locator(f"#table_allloans tbody tr:has-text('{stacx_id}')").first
    print("Target row text:", row.inner_text().strip().replace('\n', ' | '), flush=True)

    # Click 3 dots action button
    action_btn = row.locator("td").last.locator("a, button, i.fa-ellipsis-v").first
    print("Clicking action 3 dots...", flush=True)
    action_btn.click()
    page.wait_for_timeout(1500)

    # Check dropdown menu items
    menu_items = page.locator(".dropdown-menu.show a, .dropdown-menu:visible a").all()
    print("Dropdown items:", [item.inner_text().strip() for item in menu_items], flush=True)

    cls_item = page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first
    cls_item.click()
    print("Clicked Classification menu item. Waiting for navigation...", flush=True)

    # Wait for navigation to /Indexing/
    page.wait_for_url("**/Indexing/**", timeout=30000)
    print(f"Successfully reached Indexing page! URL: {page.url}", flush=True)

    # Wait for #stackingcomplete to be visible
    page.wait_for_selector("#stackingcomplete", state="visible", timeout=30000)
    page.wait_for_timeout(5000)

    # Capture screenshot
    page.screenshot(path="scratch/inside_indexing.png")
    print("Saved scratch/inside_indexing.png", flush=True)

    browser.close()
