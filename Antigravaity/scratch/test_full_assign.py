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

    search_box = page.locator("#custom_search_value")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    page.wait_for_timeout(4000)

    row = page.locator(f"#table_allloans tbody tr:has-text('{stacx_id}')").first
    row.locator("td").last.locator("a, button, i.fa-ellipsis-v, .dropdown-toggle").first.click()
    page.wait_for_timeout(1000)

    page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first.click()
    page.wait_for_url("**/Indexing/**", timeout=30000)

    edit_btn = page.locator("button:has-text('Open in Edit Mode'), .btn:has-text('Open in Edit Mode')").first
    try:
        edit_btn.wait_for(state="visible", timeout=6000)
        edit_btn.click()
    except:
        pass

    # Wait for page metrics to populate
    page.wait_for_function(
        "() => document.querySelector('#Total_Count') && document.querySelector('#Total_Count').innerText.trim() !== ''",
        timeout=40000
    )
    page.wait_for_timeout(3000)

    # Execute selection of all unclassified pages & assign to 1st doc type
    result = page.evaluate("""() => {
        // 1. Check all unclassified checkboxes
        const cbs = Array.from(document.querySelectorAll('#unclassifiedPageContainerId .checkbox_unsorted'));
        cbs.forEach(cb => { cb.checked = true; });
        
        // 2. Select 1st doc type in stackdropdown
        const firstDocLi = document.querySelector('.Questionlist_Document_type')?.closest('li');
        if (firstDocLi) {
            const docType = firstDocLi.getAttribute('data-documenttype');
            const parentCat = firstDocLi.getAttribute('data-parentcategory');
            
            const options = document.querySelectorAll('.stackdropdown option');
            options.forEach(opt => {
                if (opt.getAttribute('data-mastercategory') === parentCat && opt.getAttribute('data-mastersubcategory') === docType) {
                    opt.selected = true;
                }
            });
            document.querySelectorAll('.categoryhighlight').forEach(el => el.classList.remove('categoryhighlight'));
            firstDocLi.querySelector('div')?.classList.add('categoryhighlight');
        }

        // 3. Call sortpages()
        if (typeof window.sortpages === 'function') {
            window.sortpages();
        }

        const newClassi = document.querySelector('#Classi_Count')?.innerText?.trim();
        const newTotal = document.querySelector('#Total_Count')?.innerText?.trim();
        const remainingUnclass = document.querySelectorAll('#unclassifiedPageContainerId li').length;

        return {
            checkedCount: cbs.length,
            newClassi,
            newTotal,
            remainingUnclass
        };
    }""")

    print("Assignment result:", result, flush=True)

    # Click Save to trigger indexing successful
    page.locator("#toArray").click()
    page.wait_for_timeout(3000)

    # Check for toast
    toast_text = page.evaluate("() => document.querySelector('.toast:visible, .toast.show, [class*=\"toast\"]:visible')?.innerText || 'no visible toast'")
    print("Toast message:", toast_text, flush=True)

    page.screenshot(path="scratch/after_classify.png")

    browser.close()
