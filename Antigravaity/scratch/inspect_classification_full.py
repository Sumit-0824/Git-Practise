import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, load_test_data

test_data = load_test_data()
stacx_id = test_data.get('stacx_id', 'MCL72626122406')
print(f"Inspecting Classification for STACX ID: {stacx_id}", flush=True)

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = context.new_page()
    page.goto('https://laravel.stacxuat.com/Transactions', wait_until='domcontentloaded')
    page.wait_for_timeout(4000)

    # 1. Click on Classification workflow tab
    cls_tab = page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first
    print("Clicking Classification workflow tab...", flush=True)
    cls_tab.click()
    page.wait_for_timeout(2500)

    # 2. Filter STACX ID
    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(2500)

    # 3. Action button -> Classification
    row = page.locator("#table_allloans tbody tr, table.dataTable tbody tr").first
    action_trigger = row.locator("td").last.locator("a.btn-icon, .dropdown-toggle, i.fa-ellipsis-v, a").first
    print("Clicking action dropdown...", flush=True)
    action_trigger.click()
    page.wait_for_timeout(1000)

    cls_item = page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first
    print("Clicking Classification action item...", flush=True)
    cls_item.click()

    # Wait for classification screen
    print("Waiting for Classification screen...", flush=True)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector("#stackingcomplete", state="visible", timeout=30000)
    page.wait_for_timeout(5000)
    print("Classification screen loaded! URL:", page.url, flush=True)

    # Inspect right side unclassified container and elements
    info = page.evaluate("""() => {
        // Page counts & confidence
        const bodyText = document.body.innerText;
        
        // Find confidence badges
        const badges = Array.from(document.querySelectorAll('.badge, [class*="badge"], [class*="legend"]'))
            .map(b => b.innerText.trim()).filter(t => t.includes('%') || t.includes('|'));
            
        // Progress text
        const progressEl = document.querySelector('.progress-bar, [class*="progress"]');
        
        // Unclassified items
        const checkboxes = Array.from(document.querySelectorAll('input[type="checkbox"]')).map(cb => ({
            id: cb.id,
            name: cb.name,
            className: cb.className,
            checked: cb.checked,
            parentText: cb.parentElement ? cb.parentElement.innerText.trim().replace(/\\s+/g, ' ') : ''
        }));
        
        // Find doc types on left side
        const docTypes = Array.from(document.querySelectorAll('.doc_type, [class*="doctype"], [class*="doc-type"], [class*="tree"] li, [id*="tree"] li')).slice(0, 15).map(dt => ({
            tag: dt.tagName,
            cls: dt.className,
            id: dt.id,
            text: dt.innerText.trim().slice(0, 50)
        }));

        // Icons near unclassified
        const unclassH5 = Array.from(document.querySelectorAll('h5, h6, .card-title')).find(h => h.innerText && h.innerText.includes('Unclassified'));
        let unclassHeaderIcons = [];
        if (unclassH5 && unclassH5.parentElement) {
            unclassHeaderIcons = Array.from(unclassH5.parentElement.querySelectorAll('a, button, i, svg')).map(el => ({
                tag: el.tagName,
                cls: el.className,
                title: el.getAttribute('title') || '',
                id: el.id
            }));
        }

        return {
            badges,
            checkboxCount: checkboxes.length,
            checkboxesSample: checkboxes.slice(0, 20),
            unclassHeaderIcons,
            docTypesSample: docTypes
        };
    }""")

    import pprint
    pprint.pprint(info)

    browser.close()
