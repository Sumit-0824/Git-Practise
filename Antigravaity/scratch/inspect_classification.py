import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, load_test_data

test_data = load_test_data()
stacx_id = test_data.get('stacx_id', 'MCL72626122406')
print(f"Testing with STACX ID: {stacx_id}", flush=True)

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = context.new_page()
    page.goto('https://laravel.stacxuat.com/Transactions', wait_until='domcontentloaded')
    page.wait_for_timeout(4000)
    
    # Click Classification workflow tab
    cls_tab = page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first
    print("Clicking on Classification tab...", flush=True)
    cls_tab.click()
    page.wait_for_timeout(3000)

    # Filter by STACX ID
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(3000)

    # Match row & Click action
    row = page.locator("#table_allloans tbody tr, table.dataTable tbody tr").first
    action_trigger = row.locator("td").last.locator("a.btn-icon, .dropdown-toggle, i.fa-ellipsis-v, a").first
    print("Opening Action menu...", flush=True)
    action_trigger.click()
    page.wait_for_timeout(1000)

    # Click 'Classification'
    cls_item = page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first
    print("Clicking Classification menu item...", flush=True)
    cls_item.click()
    
    # Wait for classification screen to load
    print("Waiting for Classification screen to load...", flush=True)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(6000)
    print("Current URL:", page.url, flush=True)

    # Save screenshot of classification screen
    page.screenshot(path="classification_screen.png")
    print("Screenshot saved to: classification_screen.png", flush=True)

    # Inspect metrics / counts on the classification page
    # Look for page count, OCR confidence, classified/unclassified counts
    text_content = page.locator("body").inner_text()
    for line in text_content.splitlines():
        line_s = line.strip()
        if any(kw in line_s.lower() for kw in ["page", "ocr", "confidence", "classified", "unclassified", "total"]):
            if len(line_s) < 100:
                print(f"  [Metric Line]: {line_s}", flush=True)

    # Look for buttons like "Classification Complete", "Complete", etc.
    buttons = page.locator("button, a.btn").all()
    print("\nButtons on Classification page:", flush=True)
    for b in buttons:
        try:
            if b.is_visible():
                txt = b.inner_text().strip().replace('\n', ' ')
                bid = b.get_attribute("id") or ""
                bcls = b.get_attribute("class") or ""
                if len(txt) > 0 and len(txt) < 50:
                    print(f"  Button: id='{bid}', class='{bcls[:30]}', text='{txt}'", flush=True)
        except:
            pass

    browser.close()
