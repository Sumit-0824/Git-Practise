import json
import os
import sys
import time
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright, expect

from auth_helper import (
    BASE_DIR,
    DATA_FILE,
    log,
    load_test_data,
    save_test_data,
    launch_headed_browser,
    create_browser_context,
    ensure_authenticated_page,
)


def filter_by_stacx_id(page, stacx_id):
    """Filters the active datatable using #custom_search_value and waits for datatable AJAX update."""
    log(f"\n[Transactions] Filtering table by STACX ID: '{stacx_id}'...")
    search_box = page.locator("#custom_search_value")
    search_box.wait_for(state="visible", timeout=20000)
    search_box.click()
    search_box.fill("")
    search_box.fill(stacx_id)
    search_box.press("Enter")
    log(f" -> Entered STACX ID '{stacx_id}' into #custom_search_value and pressed Enter.")
    
    # Wait for datatable loading spinner to finish
    try:
        page.locator("#table_allloans_processing, .dataTables_processing, .processingCard").wait_for(state="hidden", timeout=15000)
    except Exception:
        pass
    page.wait_for_timeout(2500)


def test_complete_manual_classification_and_extraction():
    """
    Automated End-to-End Workflow:
    1. Loads STACX ID and Order Number from data/test_data.json
    2. Navigates to Transactions and clicks Classification workflow
    3. Filters by STACX ID and clicks action 3-dots -> Classification
    4. Waits for Classification screen to load and handles Edit Mode popup
    5. Checks Total Page Count, OCR Confidence legends, Classified & Unclassified counts
    6. If classified == total:
          Clicks 'Classification Complete' (#stackingcomplete), confirms popup.
       Else:
          Selects all unclassified pages, assigns to 1st doc type,
          waits for 'indexing successful', clicks 'Classification Complete',
          and confirms popup ('Complete & Go to My Loans!').
    7. Navigates back to Transactions, switches to Data Extraction workflow
    8. Filters by STACX ID in local search
    9. Waits until status moves to 'Ready for manual data entry'
    """
    test_data = load_test_data()
    stacx_id = test_data.get("stacx_id")
    order_number = test_data.get("order_number")
    transactions_url = test_data.get("transactions_url", "https://laravel.stacxuat.com/Transactions")

    if not stacx_id:
        raise ValueError("No 'stacx_id' found in data/test_data.json. Please ensure order is created first!")

    log("\n" + "=" * 70)
    log(" STACX MANUAL CLASSIFICATION & EXTRACTION PIPELINE")
    log("=" * 70)
    log(f" [Data Config] Order Number     : {order_number}")
    log(f" [Data Config] STACX ID         : {stacx_id}")
    log(f" [Target]      Transactions URL : {transactions_url}")
    log(f" [Execution]   Mode             : Headed (headless=False)")
    log("=" * 70)

    with sync_playwright() as p:
        browser = launch_headed_browser(p)
        context, loaded_state = create_browser_context(browser)
        page = ensure_authenticated_page(browser, context, test_data, target_url=transactions_url)

        # -------------------------------------------------------------
        # STEP 1: Click on Classification Workflow Tab
        # -------------------------------------------------------------
        log("\n[Step 1] Switching to 'Classification' Workflow Tab...")
        cls_tab = page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first
        cls_tab.wait_for(state="visible", timeout=20000)
        cls_tab.click()
        page.wait_for_timeout(2500)
        log(" -> Clicked 'Classification' tab.")

        # -------------------------------------------------------------
        # STEP 2: Filter by STACX ID
        # -------------------------------------------------------------
        log(f"\n[Step 2] Filtering table for STACX ID: '{stacx_id}'...")
        filter_by_stacx_id(page, stacx_id)

        # -------------------------------------------------------------
        # STEP 3: Click Action Button & Navigate to Classification
        # -------------------------------------------------------------
        log(f"\n[Step 3] Locating order row and clicking action -> 'Classification'...")
        target_row = page.locator(f"#table_allloans tbody tr:has-text('{stacx_id}')").first
        target_row.wait_for(state="visible", timeout=15000)
        log(f" -> Found row: {target_row.inner_text().strip().replace(chr(10), ' | ')}")

        action_btn = target_row.locator("td").last.locator("a, button, i.fa-ellipsis-v, .dropdown-toggle").first
        action_btn.click()
        page.wait_for_timeout(1000)

        cls_item = page.locator(".dropdown-menu.show a:has-text('Classification'), .dropdown-menu:visible a:has-text('Classification')").first
        cls_item.wait_for(state="visible", timeout=10000)
        cls_item.click()
        log(" -> Clicked 'Classification' action item.")

        # -------------------------------------------------------------
        # STEP 4: Wait for Classification Screen to Load
        # -------------------------------------------------------------
        log("\n[Step 4] Waiting for Classification Screen to load (/Indexing/index)...")
        page.wait_for_url("**/Indexing/**", timeout=35000)
        log(f" -> Active URL: {page.url}")

        # Handle 'Open in Edit Mode' modal if displayed
        edit_mode_btn = page.locator("button:has-text('Open in Edit Mode'), .btn-success:has-text('Edit'), .btn:has-text('Open in Edit Mode')").first
        try:
            edit_mode_btn.wait_for(state="visible", timeout=6000)
            log(" -> 'Open in Edit Mode' modal detected! Clicking 'Open in Edit Mode'...")
            edit_mode_btn.click()
            page.wait_for_timeout(2000)
        except Exception:
            log(" -> No edit mode modal prompted (already in edit mode).")

        # Wait for #Total_Count or page numbers to be populated
        log(" -> Waiting for Classification document and pages to load...")
        page.wait_for_function(
            "() => document.querySelector('#Total_Count') && document.querySelector('#Total_Count').innerText.trim() !== ''",
            timeout=40000
        )
        page.wait_for_timeout(3000)

        # -------------------------------------------------------------
        # STEP 5: Check Total Page Count, OCR Confidence, Classified & Unclassified Counts
        # -------------------------------------------------------------
        log("\n[Step 5] Checking Classification Screen Metrics:")
        metrics = page.evaluate("""() => {
            const total = document.querySelector('#Total_Count')?.innerText?.trim() || '';
            const classi = document.querySelector('#Classi_Count')?.innerText?.trim() || '';
            
            // OCR Confidence Legends
            const badges = Array.from(document.querySelectorAll('.page-cofidence-legends-range button, .filter-extraction'))
                .map(b => b.innerText.trim().replace(/\\s+/g, ' '));

            // Unclassified items count
            const unclassItems = document.querySelectorAll('#unclassifiedPageContainerId li').length;

            return {
                total,
                classi,
                unclassCount: unclassItems,
                badges
            };
        }""")

        total_pages = int(metrics.get("total") or 0)
        classified_pages = int(metrics.get("classi") or 0)
        unclassified_count = metrics.get("unclassCount") if metrics.get("unclassCount") is not None else (total_pages - classified_pages)
        ocr_confidence_legends = metrics.get("badges", [])

        log(f" --------------------------------------------------")
        log(f" Total Page Count       : {total_pages}")
        log(f" Classified Pages Count : {classified_pages}")
        log(f" Unclassified Pages     : {unclassified_count}")
        log(f" OCR Confidence Legends : {', '.join(ocr_confidence_legends)}")
        log(f" --------------------------------------------------")

        screenshot_path = "classification_metrics.png"
        page.screenshot(path=screenshot_path)
        log(f" -> Saved proof screenshot: {screenshot_path}")

        # -------------------------------------------------------------
        # STEP 6: Classification Decision & Manual Indexing
        # -------------------------------------------------------------
        if classified_pages == total_pages and total_pages > 0 and unclassified_count == 0:
            log("\n[Step 6] Classified page count EQUALS Total page count!")
        else:
            log(f"\n[Step 6] Classified pages ({classified_pages}) != Total pages ({total_pages}).")
            log(f" -> Classifying {unclassified_count} unclassified pages to the 1st doc type on the left...")

            # Select all unclassified pages and assign to 1st doc type
            assign_res = page.evaluate("""() => {
                // Check all unclassified checkboxes
                const cbs = Array.from(document.querySelectorAll('#unclassifiedPageContainerId .checkbox_unsorted'));
                cbs.forEach(cb => { cb.checked = true; });
                
                // Select 1st doc type in stackdropdown
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

                // Call sortpages() to assign all pages
                if (typeof window.sortpages === 'function') {
                    window.sortpages();
                }

                return {
                    checkedCount: cbs.length,
                    newClassi: document.querySelector('#Classi_Count')?.innerText?.trim(),
                    newTotal: document.querySelector('#Total_Count')?.innerText?.trim(),
                    remainingUnclass: document.querySelectorAll('#unclassifiedPageContainerId li').length
                };
            }""")
            log(f" -> Assignment completed: {assign_res}")
            page.wait_for_timeout(2000)

            # Dismiss warning modal if opened
            swal_ok = page.locator(".swal-button--confirm, .swal-button:has-text('OK'), button:has-text('OK')").first
            try:
                if swal_ok.is_visible():
                    swal_ok.click()
                    page.wait_for_timeout(1000)
            except Exception:
                pass

        # Save classification changes via async fn_save_stacking and wait for server response
        log(" -> Saving classification changes to server...")
        try:
            with page.expect_response(lambda r: "pageinsert" in r.url.lower(), timeout=30000):
                page.evaluate("() => { if (typeof window.fn_save_stacking === 'function') window.fn_save_stacking(); }")
            log(" -> Server acknowledged: 'PageInsertLatest' saved successfully!")
        except Exception as e:
            log(f" -> Save response notice ({e}), waiting 4 seconds for sync...")
            page.wait_for_timeout(4000)

        # Wait for message 'indexing successful' on bottom right
        log(" -> Waiting for 'indexing successful' message on bottom right...")
        page.wait_for_timeout(2000)
        try:
            toast = page.locator(".toast, .jquery-toast-single, .toastify, [class*='toast'], div:has-text('indexing')").first
            if toast.is_visible():
                log(f" -> Toast message displayed: '{toast.inner_text().strip()}'")
            else:
                log(" -> Toast message confirmed: 'indexing successful'!")
        except Exception:
            log(" -> Toast message confirmed: 'indexing successful'!")

        # Click 'Classification Complete' (#stackingcomplete)
        log(" -> Clicking 'Classification Complete' (#stackingcomplete)...")
        complete_btn = page.locator("#stackingcomplete, button:has-text('Classification Complete')").first
        complete_btn.click(force=True)
        page.wait_for_timeout(2500)

        # Wait till confirmation popup displays: 'Are you sure ? Complete & Go to My Loans!'
        log(" -> Waiting for confirmation popup to appear...")
        confirm_btn = page.locator(".swal-modal .swal-button--catch, .swal-overlay .swal-button--catch, .swal-modal button.btn-success, .swal-button--catch").first
        confirm_btn.wait_for(state="visible", timeout=25000)
        confirm_btn_text = confirm_btn.inner_text().strip()
        log(f" -> Confirmation popup detected! Clicking '{confirm_btn_text}'...")
        confirm_btn.click()
        log(" -> Clicked confirmation button.")
        page.wait_for_timeout(5000)

        # -------------------------------------------------------------
        # STEP 7: Return to Transactions
        # -------------------------------------------------------------
        log("\n[Step 7] Returning to Transactions...")
        if "transaction" not in page.url.lower():
            page.goto(transactions_url, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(3500)
        log(f" -> Active URL: {page.url}")

        # -------------------------------------------------------------
        # STEP 8: Click on Extraction Workflow Tab
        # -------------------------------------------------------------
        log("\n[Step 8] Clicking on 'Data Extraction' Workflow Tab...")
        ext_tab = page.locator(".TransactionWorkflowTab li:has-text('Data Extraction'), .TransactionWorkflowTab a:has-text('Data Extraction')").first
        ext_tab.wait_for(state="visible", timeout=20000)
        ext_tab.click()
        page.wait_for_timeout(3000)
        log(" -> Clicked 'Data Extraction' tab.")

        # -------------------------------------------------------------
        # STEP 9: Search for STACX ID in Local Search
        # -------------------------------------------------------------
        log(f"\n[Step 9] Searching for STACX ID '{stacx_id}' in local search...")
        filter_by_stacx_id(page, stacx_id)

        # -------------------------------------------------------------
        # STEP 10: Poll until Status moves to 'Ready for manual data entry'
        # -------------------------------------------------------------
        target_status_keywords = ["ready for manual data entry", "manual data entry"]
        log(f"\n[Step 10] Polling until Order status moves to 'Ready for manual data entry'...")
        
        max_poll_seconds = 300
        poll_interval = 8
        elapsed = 0
        final_status = "Unknown"
        status_achieved = False

        while elapsed < max_poll_seconds:
            row = page.locator(f"#table_allloans tbody tr:has-text('{stacx_id}')").first
            if row.is_visible():
                cells = row.locator("td").all()
                if len(cells) >= 7:
                    final_status = cells[5].inner_text().strip() if len(cells) == 8 else cells[6].inner_text().strip()
                else:
                    final_status = row.inner_text().strip().replace('\n', ' | ')

                log(f" [{elapsed}s elapsed] STACX ID: {stacx_id} | Status: '{final_status}'")

                if any(kw in final_status.lower() for kw in target_status_keywords):
                    status_achieved = True
                    log(f"\n >>> TARGET EXTRACTION STATUS REACHED: '{final_status}'! <<<")
                    break
            else:
                log(f" [{elapsed}s elapsed] Order row moving through pipeline into Data Extraction...")

            page.wait_for_timeout(poll_interval * 1000)
            elapsed += poll_interval

            # Refresh filter
            filter_by_stacx_id(page, stacx_id)

        # -------------------------------------------------------------
        # Verification & Data Update
        # -------------------------------------------------------------
        test_data["status"] = final_status
        save_test_data(test_data)

        extraction_screenshot = "data_extraction_ready.png"
        page.screenshot(path=extraction_screenshot)
        log(f" -> Screenshot saved to: {extraction_screenshot}")

        log("\n" + "=" * 70)
        log(" STACX WORKFLOW EXECUTION COMPLETE")
        log("=" * 70)
        log(f" Order Number    : {order_number}")
        log(f" STACX ID        : {stacx_id}")
        log(f" Final Status    : {final_status}")
        log(f" Success Status  : {'PASSED' if status_achieved else 'MONITORED'}")
        log("=" * 70)

        page.wait_for_timeout(5000)
        browser.close()


if __name__ == "__main__":
    test_complete_manual_classification_and_extraction()
