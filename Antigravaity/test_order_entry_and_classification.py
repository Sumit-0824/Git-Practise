"""
End-to-End Test: Order Creation & Classification Status Tracking
Executes:
1. test_order_entry.py -> Creates Order with Freedom, Post closing product, freedom pcr, dynamic Order #, package upload.
2. test_classification.py -> Filters by Order # in Transactions, extracts STACX ID, waits for 'Ready for manual classification'.
"""
import sys
import time
from test_order_entry import test_create_order
from test_classification import test_monitor_order_classification
from auth_helper import log

def run_full_pipeline():
    log("\n" + "#" * 65)
    log("### STARTING END-TO-END PIPELINE: ORDER ENTRY + CLASSIFICATION ###")
    log("#" * 65)
    
    # Step 1: Create Order
    log("\n>>> PHASE 1: CREATE ORDER <<<")
    test_create_order()
    
    # Pause between phases
    log("\n>>> ORDER CREATED SUCCESSFULLY. MOVING TO TRANSACTIONS IN 3 SECONDS... <<<")
    time.sleep(3)
    
    # Step 2: Track Classification Status in Transactions
    log("\n>>> PHASE 2: TRACK TRANSACTIONS & CLASSIFICATION STATUS <<<")
    test_monitor_order_classification()
    
    log("\n" + "#" * 65)
    log("### END-TO-END PIPELINE COMPLETE ###")
    log("#" * 65)


if __name__ == "__main__":
    run_full_pipeline()
