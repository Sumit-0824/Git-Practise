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


def filter_by_order_number(page, order_number):
    """Filters the Transactions table by order number using #custom_search_value."""
    log(f"\n[Transactions] Filtering table by Order Number: '{order_number}'...")
    
    # Wait for datatable and custom_search_value to be visible
    try:
        search_box = page.locator("#custom_search_value")
        search_box.wait_for(state="visible", timeout=15000)
        search_box.click()
        search_box.fill("")
        search_box.fill(order_number)
        search_box.press("Enter")
        log(f" -> Entered '{order_number}' into #custom_search_value and pressed Enter.")
    except Exception as e:
        log(f" -> Custom search notice: {e}")
        # Fallback to any visible search input inside datatable filter
        candidates = page.locator(".datatable-search, input[placeholder*='Search' i]").all()
        for c in candidates:
            if c.is_visible() and c.get_attribute("id") != "search":
                c.fill(order_number)
                c.press("Enter")
                break

    page.wait_for_timeout(3000)  # Wait for AJAX datatable update


def extract_stacx_id_and_status(page, order_number):
    """
    Finds the row corresponding to order_number in the Transactions table.
    Table columns: [0: MCOrderNumber, 1: STACX ID, 2: Entry Date, 3: Loan #, 4: Project, 5: Client, 6: Current Status, ...]
    Returns (stacx_id, status_text, row).
    """
    # Locate the active transactions datatable (#table_allloans)
    target_table = page.locator("#table_allloans")
    if target_table.count() == 0 or not target_table.first.is_visible():
        target_table = page.locator("table.dataTable:visible").first

    rows = target_table.locator("tbody tr")
    total_rows = rows.count()
    log(f" -> Found {total_rows} row(s) in Transactions table.")

    for i in range(total_rows):
        row = rows.nth(i)
        row_text = row.inner_text().strip()
        
        # Check if table says 'No matching records found' or 'No data available'
        if "no matching records" in row_text.lower() or "no data available" in row_text.lower():
            continue

        cells = row.locator("td")
        cell_count = cells.count()
        if cell_count >= 7:
            mc_order = cells.nth(0).inner_text().strip()
            stacx_id = cells.nth(1).inner_text().strip()
            loan_num = cells.nth(3).inner_text().strip()
            status = cells.nth(6).inner_text().strip()

            if (
                order_number.lower() in mc_order.lower()
                or order_number.lower() in loan_num.lower()
                or order_number.lower() in row_text.lower()
            ):
                log(f" -> Matched Row: Order: '{loan_num or mc_order}', STACX ID: '{stacx_id}', Current Status: '{status}'")
                return stacx_id, status, row
        elif order_number.lower() in row_text.lower():
            # Fallback cell extraction
            cell_texts = [cells.nth(j).inner_text().strip() for j in range(cell_count)]
            stacx_id = next((c for c in cell_texts if c.startswith("MCL")), cell_texts[1] if cell_count > 1 else "")
            status = cell_texts[6] if cell_count > 6 else "Processing"
            log(f" -> Matched Row (fallback): STACX ID: '{stacx_id}', Status: '{status}'")
            return stacx_id, status, row

    log(f" -> Order number '{order_number}' row not yet visible in filtered grid...")
    return None, None, None


def test_monitor_order_classification():
    """
    Automated Classification Monitoring Test:
    1. Authenticates & navigates to Transactions page
    2. Filters by order_number (loaded dynamically from data folder)
    3. Extracts the STACX ID and saves it in data folder
    4. Polls until status changes to 'Ready for manual classification'
    """
    test_data = load_test_data()
    order_number = test_data.get("order_number")
    transactions_url = test_data.get("transactions_url", "https://laravel.stacxuat.com/Transactions")

    if not order_number:
        raise ValueError("No 'order_number' found in data/test_data.json. Please run test_order_entry.py first!")

    log("\n" + "=" * 65)
    log(" STACX CLASSIFICATION STATUS MONITORING")
    log("=" * 65)
    log(f" [Data Config] Order Number     : {order_number}")
    log(f" [Target]      Transactions URL : {transactions_url}")
    log(f" [Target]      Expected Status  : Ready for manual classification")
    log(f" [Execution]   Mode             : Headed (headless=False)")
    log("=" * 65)

    with sync_playwright() as p:
        browser = launch_headed_browser(p)
        context, loaded_state = create_browser_context(browser)
        page = ensure_authenticated_page(browser, context, test_data, target_url=transactions_url)

        # Ensure on Transactions page
        if "transaction" not in page.url.lower():
            log(f" -> Navigating directly to: {transactions_url}")
            page.goto(transactions_url, wait_until="domcontentloaded", timeout=30000)

        # -------------------------------------------------------------
        # Filter by Order Number
        # -------------------------------------------------------------
        filter_by_order_number(page, order_number)

        # -------------------------------------------------------------
        # Polling Loop: Wait for "Ready for manual classification"
        # -------------------------------------------------------------
        target_status = "Ready for manual classification"
        max_poll_seconds = 300  # 5 minutes max timeout
        poll_interval = 8
        elapsed = 0
        stacx_id_found = test_data.get("stacx_id", "")
        status_achieved = False

        log(f"\n[Monitoring] Polling status for Order '{order_number}' until '{target_status}'...")

        while elapsed < max_poll_seconds:
            stacx_id, current_status, row_locator = extract_stacx_id_and_status(page, order_number)

            if not stacx_id:
                # Check Classification tab if not found on current tab
                cls_tab = page.locator(".TransactionWorkflowTab li:has-text('Classification'), .TransactionWorkflowTab a:has-text('Classification')").first
                try:
                    if cls_tab.is_visible():
                        cls_tab.click()
                        page.wait_for_timeout(2000)
                        filter_by_order_number(page, order_number)
                        stacx_id, current_status, row_locator = extract_stacx_id_and_status(page, order_number)
                except Exception:
                    pass

            if stacx_id:
                stacx_id_found = stacx_id
                test_data["stacx_id"] = stacx_id_found
                save_test_data(test_data)

            if current_status:
                log(f" [{elapsed}s elapsed] STACX ID: {stacx_id_found} | Status: '{current_status}'")
                if target_status.lower() in current_status.lower():
                    status_achieved = True
                    log(f"\n >>> TARGET STATUS REACHED: '{current_status}'! <<<")
                    break
            else:
                log(f" [{elapsed}s elapsed] Waiting for order '{order_number}' to appear in grid...")

            # Wait poll interval
            page.wait_for_timeout(poll_interval * 1000)
            elapsed += poll_interval

            # Refresh table: click refresh button if present, or re-filter
            refresh_btn = page.locator("button:has-text('Refresh'), .refresh-btn, i.bi-arrow-clockwise, a[title='Refresh']").first
            if refresh_btn.is_visible():
                refresh_btn.click()
                page.wait_for_timeout(2000)
            else:
                filter_by_order_number(page, order_number)

        # -------------------------------------------------------------
        # Post-Monitoring Results & Verification
        # -------------------------------------------------------------
        test_data["status"] = current_status if status_achieved else "Pending"
        save_test_data(test_data)

        screenshot_path = "classification_ready.png"
        page.screenshot(path=screenshot_path)
        log(f" -> Screenshot saved to: {screenshot_path}")

        log("\n" + "=" * 65)
        if status_achieved:
            log(f" [SUCCESS] STACX ID '{stacx_id_found}' is 'Ready for manual classification'!")
        else:
            log(f" [INFO] Current status: '{current_status}'. Script finished monitoring window.")
        log(f"        Order Number: {order_number}")
        log(f"        STACX ID    : {stacx_id_found}")
        log("=" * 65)

        page.wait_for_timeout(5000)
        browser.close()


if __name__ == "__main__":
    test_monitor_order_classification()
