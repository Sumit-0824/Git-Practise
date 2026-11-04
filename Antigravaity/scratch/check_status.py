import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import json
from auth_helper import load_test_data, launch_headed_browser, create_browser_context, ensure_authenticated_page
from playwright.sync_api import sync_playwright

test_data = load_test_data()
stacx_id = test_data.get('stacx_id')
print(f"Checking current status for STACX ID: {stacx_id}")

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = ensure_authenticated_page(browser, context, test_data, target_url='https://laravel.stacxuat.com/Transactions')
    
    # Click Data Extraction tab
    ext_tab = page.locator(".TransactionWorkflowTab li:has-text('Data Extraction'), .TransactionWorkflowTab a:has-text('Data Extraction')").first
    ext_tab.click()
    page.wait_for_timeout(2500)
    
    # Filter by stacx_id
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    
    # Wait for processing indicator to hide
    try:
        page.locator("#table_allloans_processing, .dataTables_processing").wait_for(state="hidden", timeout=15000)
    except Exception:
        pass
    page.wait_for_timeout(3000)
    
    row = page.locator(f"#table_allloans tbody tr:has-text('{stacx_id}')").first
    if row.is_visible():
        text = row.inner_text().strip().replace('\n', ' | ')
        print(f"Row text: {text}")
        cells = row.locator("td").all()
        for idx, cell in enumerate(cells):
            print(f"Col {idx}: {cell.inner_text().strip()}")
    else:
        print("Row not found on Data Extraction tab! Checking all rows...")
        rows = page.locator("#table_allloans tbody tr").all()
        for r in rows[:5]:
            print("Row:", r.inner_text().strip().replace('\n', ' | '))
        
    page.screenshot(path="current_data_extraction_check.png")
    browser.close()
