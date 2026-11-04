import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from auth_helper import launch_headed_browser, create_browser_context, ensure_authenticated_page, load_test_data

test_data = load_test_data()
indexing_url = "https://laravel.stacxuat.com/Indexing/index/YTMzMjUxYmFiOTQ5ZWJiZWM3OWZhM2JkNjNhMDVkM2Z%2BMzUwMjc4"

with sync_playwright() as p:
    browser = launch_headed_browser(p)
    context, _ = create_browser_context(browser)
    page = context.new_page()

    # Automatically dismiss dialogs
    page.on("dialog", lambda d: (print(f"Dialog: {d.message}", flush=True), d.accept()))

    page.goto(indexing_url, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(3000)
    print("Active URL:", page.url, flush=True)

    # Check for modals, sweetalerts, or edit mode
    modals = page.evaluate("""() => {
        const swal = document.querySelector('.swal-modal');
        const modal = document.querySelector('.modal.show');
        return {
            swalText: swal ? swal.innerText : '',
            modalText: modal ? modal.innerText : '',
            totalCount: document.querySelector('#Total_Count')?.innerText || 'not found'
        };
    }""")
    print("Modals found:", modals, flush=True)

    # Click edit mode or swal confirm if present
    edit_mode_btn = page.locator("button:has-text('Open in Edit Mode'), .btn-success:has-text('Edit'), .btn:has-text('Open in Edit Mode')").first
    if edit_mode_btn.is_visible():
        print("Clicking Edit Mode...", flush=True)
        edit_mode_btn.click()
        page.wait_for_timeout(2000)

    swal_btn = page.locator(".swal-button, button:has-text('OK'), button:has-text('Confirm')").first
    if swal_btn.is_visible():
        print("Clicking Swal button...", flush=True)
        swal_btn.click()
        page.wait_for_timeout(2000)

    # Wait for #Total_Count to populate
    print("Waiting for #Total_Count...", flush=True)
    try:
        page.wait_for_function("() => document.querySelector('#Total_Count') && document.querySelector('#Total_Count').innerText.trim() !== ''", timeout=30000)
        print("Total Count:", page.locator("#Total_Count").inner_text(), flush=True)
        print("Classi Count:", page.locator("#Classi_Count").inner_text(), flush=True)
    except Exception as e:
        print("Timeout waiting for Total_Count:", e, flush=True)

    page.screenshot(path="scratch/indexing_active.png", timeout=10000)
    print("Screenshot saved to scratch/indexing_active.png", flush=True)
    browser.close()
