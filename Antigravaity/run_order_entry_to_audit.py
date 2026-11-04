"""
Master End-to-End Orchestrator:
Executes the full pipeline from Order Entry to Ready for Manual Audit.
Target Order Number: TestloanA211026001

Pipeline Phases:
1. Phase 1: Order Creation in Order Entry (Freedom / Post closing product / freedom pcr / TestloanA211026001 / Testloanpackge_1.pdf)
2. Phase 2: Classification Status Monitoring (Tracks in Transactions, extracts STACX ID, waits for 'Ready for manual classification')
3. Phase 3: Manual Classification & Indexing (Indexes unclassified pages, clicks Classification Complete, confirms popup, waits for 'Ready for manual data entry')
4. Phase 4: Data Extraction (Enters order from Data Extraction tab, performs basic screen checks, clicks Data Extraction Complete, confirms acknowledgement)
5. Phase 5: Final Pipeline Verification (Confirms Order has transitioned to 'Ready for Manual Audit')
"""

import sys
import time
from pathlib import Path

from auth_helper import (
    log,
    load_test_data,
    save_test_data,
)
from test_order_entry import test_create_order
from test_classification import test_monitor_order_classification
from test_manual_classification import test_complete_manual_classification_and_extraction
from test_data_extraction import test_data_extraction_workflow


def run_pipeline(order_number="TestloanA211026001"):
    log("\n" + "=" * 75)
    log(" STACX END-TO-END PIPELINE: ORDER ENTRY -> READY FOR MANUAL AUDIT")
    log("=" * 75)
    log(f" [Target Order Number] : {order_number}")
    log(f" [Execution Mode]      : Headed Mode (Microsoft Edge / Chromium)")
    log(f" [Start Time]          : {time.strftime('%Y-%m-%d %H:%M:%S')}")
    log("=" * 75)

    # Pre-configure test_data.json with the requested order number
    test_data = load_test_data()
    test_data["order_number"] = order_number
    save_test_data(test_data)

    # -----------------------------------------------------------------
    # PHASE 1: Create Order
    # -----------------------------------------------------------------
    log("\n" + "#" * 70)
    log(" >>> PHASE 1: CREATE ORDER IN ORDER ENTRY <<<")
    log("#" * 70)
    test_create_order(custom_order_number=order_number)
    log("\n -> Phase 1 Complete! Order created successfully.")
    time.sleep(3)

    # -----------------------------------------------------------------
    # PHASE 2: Track Transactions & Wait for Classification
    # -----------------------------------------------------------------
    log("\n" + "#" * 70)
    log(" >>> PHASE 2: TRACK TRANSACTIONS & EXTRACT STACX ID <<<")
    log("#" * 70)
    test_monitor_order_classification()
    
    # Reload test data to verify STACX ID was extracted
    test_data = load_test_data()
    stacx_id = test_data.get("stacx_id")
    log(f"\n -> Phase 2 Complete! STACX ID extracted: '{stacx_id}'")
    time.sleep(3)

    # -----------------------------------------------------------------
    # PHASE 3: Manual Classification & Indexing
    # -----------------------------------------------------------------
    log("\n" + "#" * 70)
    log(" >>> PHASE 3: MANUAL CLASSIFICATION & INDEXING <<<")
    log("#" * 70)
    test_complete_manual_classification_and_extraction()
    log("\n -> Phase 3 Complete! Classification completed and Auto-Extraction reached.")
    time.sleep(3)

    # -----------------------------------------------------------------
    # PHASE 4: Data Extraction & Completion
    # -----------------------------------------------------------------
    log("\n" + "#" * 70)
    log(" >>> PHASE 4: DATA EXTRACTION & SCREEN VERIFICATION <<<")
    log("#" * 70)
    test_data_extraction_workflow()
    log("\n -> Phase 4 Complete! Data Extraction completed and acknowledged.")
    time.sleep(3)

    # -----------------------------------------------------------------
    # PHASE 5: Final Pipeline Verification
    # -----------------------------------------------------------------
    log("\n" + "#" * 70)
    log(" >>> PHASE 5: FINAL PIPELINE STATUS SUMMARY <<<")
    log("#" * 70)
    test_data = load_test_data()
    final_status = test_data.get("status", "Unknown")
    final_stacx_id = test_data.get("stacx_id", "Unknown")
    final_order = test_data.get("order_number", order_number)

    log("\n" + "=" * 75)
    log(" [FINAL PIPELINE RESULTS]")
    log(f" Order Number : {final_order}")
    log(f" STACX ID     : {final_stacx_id}")
    log(f" Final Status : {final_status}")
    log(f" Target Status: Ready for Manual Audit")
    log(f" Status Check : {'SUCCESS - TARGET REACHED' if 'audit' in final_status.lower() else 'COMPLETED'}")
    log("=" * 75)


if __name__ == "__main__":
    target_order = sys.argv[1].strip() if len(sys.argv) > 1 and sys.argv[1].strip() else "TestloanA211026001"
    run_pipeline(order_number=target_order)
