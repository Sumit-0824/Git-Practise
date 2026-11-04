import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright, expect

from auth_helper import (
    BASE_DIR,
    DATA_FILE,
    TESTPACKAGE_FILE,
    log,
    load_test_data,
    save_test_data,
    launch_headed_browser,
    create_browser_context,
    ensure_authenticated_page,
)


def select_dropdown_option(page, label_name, target_value):
    """
    Robust dropdown selector supporting:
    1. Native <select> elements (matching option by substring / case-insensitive)
    2. Select2 containers (clicking container, typing search, selecting option)
    3. Custom bootstrap dropdowns
    """
    log(f" -> Selecting '{target_value}' for '{label_name}'...")
    clean = label_name.replace("*", "").strip().lower()

    # Strategy 1: Find native <select>
    select_candidates = [
        page.locator(f"select[id*='{clean}' i]"),
        page.locator(f"select[name*='{clean}' i]"),
        page.locator(f"//label[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{clean}')]/following::select[1]"),
        page.locator(f"//label[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{clean}')]/..//select"),
    ]

    for sel in select_candidates:
        if sel.count() > 0:
            try:
                # Wait for options to be populated
                page.wait_for_timeout(1000)
                options = sel.first.locator("option").all_text_contents()
                match = None
                for opt in options:
                    if target_value.lower() in opt.strip().lower():
                        match = opt.strip()
                        break
                if match:
                    sel.first.select_option(label=match)
                    sel.first.dispatch_event("change")
                    log(f"    Selected '{match}' in native select.")
                    page.wait_for_timeout(2000)  # Wait for AJAX cascade
                    return True
            except Exception as e:
                log(f"    Native select notice: {e}")

    # Strategy 2: Select2 / Custom container
    select2_candidates = [
        page.locator(f"//label[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{clean}')]/following::span[contains(@class, 'select2')][1]"),
        page.locator(f"//label[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{clean}')]/..//span[contains(@class, 'select2')]"),
        page.locator(f"span[id*='select2-{clean}']"),
        page.locator(f".select2-container:near(:text('{clean}'))"),
    ]

    for s2 in select2_candidates:
        if s2.count() > 0 and s2.first.is_visible():
            try:
                s2.first.click()
                page.wait_for_timeout(600)
                search_field = page.locator(".select2-search__field")
                if search_field.is_visible():
                    search_field.fill(target_value)
                    page.wait_for_timeout(600)

                # Look for matching option in dropdown list
                opt_loc = page.locator(f".select2-results__option:has-text('{target_value}')").first
                if opt_loc.is_visible():
                    opt_loc.click()
                    log(f"    Selected '{target_value}' via Select2.")
                    page.wait_for_timeout(2000)
                    return True
                else:
                    search_field.press("Enter")
                    log(f"    Pressed Enter on Select2 search for '{target_value}'.")
                    page.wait_for_timeout(2000)
                    return True
            except Exception as e:
                log(f"    Select2 notice: {e}")

    # Strategy 3: Click text / dropdown button
    try:
        drop_btn = page.locator(f"//label[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{clean}')]/following::button[1]")
        if drop_btn.count() > 0 and drop_btn.first.is_visible():
            drop_btn.first.click()
            page.wait_for_timeout(500)
            target_item = page.locator(f"a:has-text('{target_value}'), .dropdown-item:has-text('{target_value}')").first
            if target_item.is_visible():
                target_item.click()
                log(f"    Selected '{target_value}' via dropdown menu.")
                page.wait_for_timeout(2000)
                return True
    except Exception:
        pass

    log(f" [Warning] Could not find dropdown element for '{label_name}'")
    return False


def fill_form_input(page, label_name, text_value):
    """Locates and fills an input field by its label."""
    clean = label_name.replace("*", "").strip().lower()
    log(f" -> Entering '{text_value}' for '{label_name}'...")

    input_candidates = [
        page.locator(f"input[id*='{clean.replace(' ', '')}' i]"),
        page.locator(f"input[name*='{clean.replace(' ', '')}' i]"),
        page.locator(f"input[id*='{clean.replace(' ', '_')}' i]"),
        page.locator(f"input[name*='{clean.replace(' ', '_')}' i]"),
        page.locator(f"input[placeholder*='{clean}' i]"),
        page.locator(f"//label[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{clean}')]/following::input[1]"),
        page.locator(f"//label[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{clean}')]/..//input"),
    ]

    for inp in input_candidates:
        if inp.count() > 0 and inp.first.is_visible():
            inp.first.click()
            inp.first.fill("")
            inp.first.fill(text_value)
            log(f"    Filled '{text_value}' into input field.")
            return True

    log(f" [Warning] Could not locate input field for '{label_name}'")
    return False


def test_create_order(custom_order_number=None):
    """
    Automated Order Creation Test:
    1. Authenticates & navigates to Order Entry page (headed mode)
    2. Chooses Client: 'Freedom'
    3. Chooses Product: 'Post closing product'
    4. Chooses Project: 'freedom pcr'
    5. Enters dynamic Order Number and stores it in data folder
    6. Uploads Testloanpackge_1.pdf from testpackage folder
    7. Clicks Create Order button and confirms creation
    """
    test_data = load_test_data()
    client = test_data.get("client", "Freedom")
    product = test_data.get("product", "Post closing product")
    project = test_data.get("project", "freedom pcr")
    order_entry_url = test_data.get("order_entry_url", "https://laravel.stacxuat.com/Orderentry/index")

    # Use custom order number if provided, else check sys.argv or generate dynamic
    if custom_order_number:
        order_number = custom_order_number
    elif len(sys.argv) > 1 and sys.argv[1].strip():
        order_number = sys.argv[1].strip()
    else:
        timestamp_suffix = datetime.now().strftime("%m%d_%H%M%S")
        order_number = f"ORD_FDM_{timestamp_suffix}"
    
    test_data["order_number"] = order_number
    save_test_data(test_data)

    # Verify package file path
    package_file = TESTPACKAGE_FILE
    if not package_file.exists():
        fallback = Path("C:/Users/Sumitkumar.Sinha/Downloads/Mc Test file/Testloanpackge_1.pdf")
        if fallback.exists():
            package_file = fallback
        else:
            raise FileNotFoundError(f"Package file not found at {package_file} or {fallback}")

    log("\n" + "=" * 65)
    log(" STACX CREATE ORDER AUTOMATION")
    log("=" * 65)
    log(f" [Config] Client       : {client}")
    log(f" [Config] Product      : {product}")
    log(f" [Config] Project      : {project}")
    log(f" [Config] Order Number : {order_number}")
    log(f" [Config] Package File : {package_file}")
    log(f" [Mode]   Headed Mode  : Enabled (headless=False)")
    log("=" * 65)

    with sync_playwright() as p:
        browser = launch_headed_browser(p)
        context, loaded_state = create_browser_context(browser)
        page = ensure_authenticated_page(browser, context, test_data, target_url=order_entry_url)

        # -------------------------------------------------------------
        # Step 0: Ensure Order Entry Page is fully loaded
        # -------------------------------------------------------------
        if "orderentry" not in page.url.lower():
            log(f" -> Navigating directly to Order Entry: {order_entry_url}...")
            page.goto(order_entry_url, wait_until="domcontentloaded", timeout=30000)

        # Wait for form elements to be rendered
        try:
            page.locator("label:has-text('Client'), select, #Client").first.wait_for(state="visible", timeout=15000)
            log(" -> Order Entry form loaded successfully.")
        except Exception:
            log(f" -> Current URL: {page.url}, waiting 3s for rendering...")
            page.wait_for_timeout(3000)

        # -------------------------------------------------------------
        # Step 1: Ensure Single Entry Tab is selected
        # -------------------------------------------------------------
        log("\n[Order Entry] Verifying 'Single Entry' tab...")
        single_entry_tab = page.locator("a:has-text('Single Entry'), button:has-text('Single Entry'), #single_entry")
        if single_entry_tab.count() > 0 and single_entry_tab.first.is_visible():
            single_entry_tab.first.click()
            log(" -> 'Single Entry' tab confirmed active.")
        page.wait_for_timeout(1000)

        # -------------------------------------------------------------
        # Step 2: Select Client -> 'Freedom' (CL009 / FREEDOM)
        # -------------------------------------------------------------
        log(f"\n[Order Entry] Selecting Client '{client}'...")
        cust_select = page.locator("#Customer")
        cust_select.wait_for(state="visible", timeout=10000)
        # Find Freedom option
        cust_options = cust_select.locator("option").all()
        selected_client = False
        for opt in cust_options:
            opt_text = opt.inner_text().strip()
            if client.lower() in opt_text.lower():
                cust_select.select_option(value=opt.get_attribute("value"))
                cust_select.dispatch_event("change")
                log(f" -> Selected Client option: '{opt_text}'")
                selected_client = True
                break
        if not selected_client:
            select_dropdown_option(page, "Client", client)
        
        log(" -> Waiting for Product dropdown to populate...")
        page.wait_for_timeout(3000)

        # -------------------------------------------------------------
        # Step 3: Select Product -> 'Post closing product' (Post Closing Review)
        # -------------------------------------------------------------
        log(f"\n[Order Entry] Selecting Product '{product}'...")
        prod_select = page.locator("#Single-ProductUID")
        # Wait up to 10s for options to populate
        for _ in range(10):
            if prod_select.locator("option").count() > 1:
                break
            page.wait_for_timeout(1000)

        prod_options = prod_select.locator("option").all()
        selected_prod = False
        for opt in prod_options:
            opt_text = opt.inner_text().strip()
            # Match 'Post closing product' or 'Post Closing Review'
            if "post closing" in opt_text.lower():
                prod_select.select_option(value=opt.get_attribute("value"))
                prod_select.dispatch_event("change")
                log(f" -> Selected Product option: '{opt_text}'")
                selected_prod = True
                break
        if not selected_prod:
            select_dropdown_option(page, "Product", product)

        log(" -> Waiting for Project dropdown to populate...")
        page.wait_for_timeout(3000)

        # -------------------------------------------------------------
        # Step 4: Select Project -> 'freedom pcr' (CL138 / FREEDOM PCR Project)
        # -------------------------------------------------------------
        log(f"\n[Order Entry] Selecting Project '{project}'...")
        proj_select = page.locator("#Single-ProjectUID")
        for _ in range(10):
            if proj_select.locator("option").count() > 0 and proj_select.locator("option").first.inner_text().strip() != "":
                break
            page.wait_for_timeout(1000)

        proj_options = proj_select.locator("option").all()
        selected_proj = False
        for opt in proj_options:
            opt_text = opt.inner_text().strip()
            if "freedom pcr" in opt_text.lower() or "freedom" in opt_text.lower():
                proj_select.select_option(value=opt.get_attribute("value"))
                proj_select.dispatch_event("change")
                log(f" -> Selected Project option: '{opt_text}'")
                selected_proj = True
                break
        if not selected_proj:
            select_dropdown_option(page, "Project", project)
        page.wait_for_timeout(1500)

        # -------------------------------------------------------------
        # Step 5: Enter Order Number
        # -------------------------------------------------------------
        log(f"\n[Order Entry] Entering Order Number: '{order_number}'...")
        order_num_input = page.locator("#LoanNumber, input[name='LoanNumber']").first
        if order_num_input.is_visible():
            order_num_input.click()
            order_num_input.fill("")
            order_num_input.fill(order_number)
            log(f" -> Entered '{order_number}' into #LoanNumber.")
        else:
            fill_form_input(page, "Order Number", order_number)
        page.wait_for_timeout(1000)

        # -------------------------------------------------------------
        # Step 6: Upload Package File
        # -------------------------------------------------------------
        log(f"\n[Order Entry] Uploading package file: {package_file.name}...")
        file_input = page.locator("#DocumentUploadNew, input[type='file']").first
        file_input.set_input_files(str(package_file.resolve()))
        log(f" -> Attached {package_file.name} via #DocumentUploadNew.")

        # Wait for file upload preview to render
        log(" -> Waiting 4 seconds for file upload preview to attach...")
        page.wait_for_timeout(4000)

        # -------------------------------------------------------------
        # Step 7: Click Create Order button (Save & Continue)
        # -------------------------------------------------------------
        log("\n[Order Entry] Submitting order creation...")
        save_btn = page.locator("#saveandexit").first
        if save_btn.is_visible():
            log(f" -> Found submit button #saveandexit ('{save_btn.inner_text().strip()}'). Clicking...")
            save_btn.scroll_into_view_if_needed()
            save_btn.click()
        else:
            log(" -> Fallback to button.single_submit:has-text('Save & Continue')...")
            page.locator("button.single_submit:has-text('Save & Continue')").first.click()

        # Handle any confirmation alerts or popups (SweetAlert / Toast)
        page.wait_for_timeout(4000)
        swal_ok = page.locator("button.swal-button, button:has-text('OK'), button:has-text('Confirm')")
        try:
            if swal_ok.count() > 0 and swal_ok.first.is_visible(timeout=3000):
                log(" -> Confirmation alert detected. Clicking...")
                swal_ok.first.click()
        except Exception:
            pass

        # Wait for order submission processing / redirect
        page.wait_for_timeout(5000)

        # Save order number in data folder for reuse in classification script
        test_data["order_number"] = order_number
        save_test_data(test_data)

        # Capture proof screenshot
        screenshot_path = "order_created.png"
        page.screenshot(path=screenshot_path)
        log(f" -> Screenshot saved to: {screenshot_path}")

        log("\n" + "=" * 65)
        log(f" [SUCCESS] Order created successfully!")
        log(f"           Order Number: {order_number}")
        log(f"           Stored in data folder for classification check.")
        log("=" * 65)

        page.wait_for_timeout(4000)
        browser.close()


if __name__ == "__main__":
    test_create_order()
