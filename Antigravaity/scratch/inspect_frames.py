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
    page.wait_for_timeout(3500)

    # Classification tab
    page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first.click()
    page.wait_for_timeout(2000)

    # Filter STACX ID
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(2000)

    # Row Action -> Classification
    row = page.locator("#table_allloans tbody tr, table.dataTable tbody tr").first
    row.locator("td").last.locator("a.btn-icon, .dropdown-toggle, i.fa-ellipsis-v, a").first.click()
    page.wait_for_timeout(1000)

    page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first.click()
    page.wait_for_selector("#stackingcomplete", state="visible", timeout=30000)
    page.wait_for_timeout(4000)

    print("Frames count:", len(page.frames), flush=True)
    for idx, f in enumerate(page.frames):
        print(f"Frame {idx}: name='{f.name}', url='{f.url}'", flush=True)
        try:
            body_txt = f.locator("body").inner_text()
            for line in body_txt.splitlines():
                if "unclassified" in line.lower() or "page 1" in line.lower() or "confidence" in line.lower():
                    print(f"   [Frame {idx} text]: {line.strip()}", flush=True)
        except Exception as e:
            print(f"   [Frame {idx} err]: {e}", flush=True)

    browser.close()
