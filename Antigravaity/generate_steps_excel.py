import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from pathlib import Path

def create_workflow_excel(output_path="STACX_Order_Entry_to_Classification_Workflow.xlsx"):
    wb = openpyxl.Workbook()
    
    # -------------------------------------------------------------
    # Styling Definitions
    # -------------------------------------------------------------
    font_title = Font(name="Calibri", size=16, bold=True, color="FFFFFF")
    font_subtitle = Font(name="Calibri", size=11, italic=True, color="E0E0E0")
    font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    font_bold = Font(name="Calibri", size=10, bold=True, color="000000")
    font_regular = Font(name="Calibri", size=10, color="000000")
    font_code = Font(name="Consolas", size=9.5, color="1F497D")
    font_success = Font(name="Calibri", size=10, bold=True, color="1E4620")

    fill_title = PatternFill(start_color="1A2530", end_color="1A2530", fill_type="solid")  # Dark Slate
    fill_header = PatternFill(start_color="2C3E50", end_color="2C3E50", fill_type="solid") # Navy / Slate
    fill_zebra_even = PatternFill(start_color="F7F9FB", end_color="F7F9FB", fill_type="solid")
    fill_zebra_odd = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
    fill_success = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid") # Soft green

    thin_border_side = Side(border_style="thin", color="D0D7DE")
    border_cell = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
    border_header = Border(
        left=Side(border_style="thin", color="4A6572"),
        right=Side(border_style="thin", color="4A6572"),
        top=Side(border_style="medium", color="1A2530"),
        bottom=Side(border_style="medium", color="1A2530")
    )

    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
    align_code = Alignment(horizontal="left", vertical="center", wrap_text=True)

    # =============================================================
    # SHEET 1: Detailed Workflow Steps
    # =============================================================
    ws1 = wb.active
    ws1.title = "Step-by-Step Workflow"
    ws1.views.sheetView[0].showGridLines = True

    # Title Block
    ws1.merge_cells("A1:H1")
    ws1["A1"] = "STACX Platform - End-to-End Test Execution Steps"
    ws1["A1"].font = font_title
    ws1["A1"].fill = fill_title
    ws1["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws1.row_dimensions[1].height = 40

    ws1.merge_cells("A2:H2")
    ws1["A2"] = "Complete Flow: URL Access -> Login -> Order Entry -> Classification -> Manual Indexing -> Data Extraction (Ready)"
    ws1["A2"].font = font_subtitle
    ws1["A2"].fill = fill_title
    ws1["A2"].alignment = Alignment(horizontal="center", vertical="center")
    ws1.row_dimensions[2].height = 24

    headers_ws1 = [
        "Step #",
        "Phase / Module",
        "Action Description",
        "Target UI Element / Selector",
        "Test Data / Input Values",
        "Expected Result / Verification",
        "Script Function / Implementation",
        "Status"
    ]

    ws1.row_dimensions[4].height = 28
    for col_idx, header in enumerate(headers_ws1, 1):
        cell = ws1.cell(row=4, column=col_idx, value=header)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border_header

    steps_data = [
        # Phase 1: Authentication
        (
            "1.1", "1. Authentication",
            "Launch Browser in Headed Mode",
            "Browser Engine (MS Edge / Chromium)",
            "channel='msedge', headless=False, slow_mo=300",
            "Microsoft Edge launches on the desktop visible to the user.",
            "auth_helper.py -> launch_headed_browser()", "Passed"
        ),
        (
            "1.2", "1. Authentication",
            "Access STACX Login Page",
            "https://laravel.stacxuat.com/Login/index",
            "Target Login URL",
            "Login form loads displaying Email & Password fields.",
            "auth_helper.py -> page.goto(login_url)", "Passed"
        ),
        (
            "1.3", "1. Authentication",
            "Enter User Email Address",
            "input#Email (name='Email')",
            "sumitkumar.sinha@avanzetechlabs.com",
            "Email input field populated accurately.",
            "auth_helper.py -> page.fill('#Email', email)", "Passed"
        ),
        (
            "1.4", "1. Authentication",
            "Enter Account Password",
            "input#Password (name='Password')",
            "Radiant@2026",
            "Password masked and accepted into password field.",
            "auth_helper.py -> page.fill('#Password', password)", "Passed"
        ),
        (
            "1.5", "1. Authentication",
            "Click Sign In Button",
            "button#submitbtn (type='submit')",
            "Click Action",
            "Credentials validated; redirected to 2FA verification screen.",
            "auth_helper.py -> page.click('#submitbtn')", "Passed"
        ),
        (
            "1.6", "1. Authentication",
            "Enter 2FA / TOTP Security Code",
            "input#2fa_code (name='2fa_code')",
            "Dynamic 6-digit TOTP (e.g. 320516)",
            "6-digit code populated into 2FA input box.",
            "auth_helper.py -> page.fill('#2fa_code', otp)", "Passed"
        ),
        (
            "1.7", "1. Authentication",
            "Submit 2FA & Confirm SweetAlert",
            "button#btn-2fa-verify & .swal-button--catch",
            "Click Action",
            "Popup displays 'Verified Successfully'; browser redirects to Dashboard / Transactions.",
            "auth_helper.py -> swal.click() -> session_state.json saved", "Passed"
        ),

        # Phase 2: Navigation to Order Entry
        (
            "2.1", "2. Order Entry",
            "Navigate to Order Entry Module",
            "Navbar Link: a:has-text('Order Entry') / URL",
            "https://laravel.stacxuat.com/Orderentry/index",
            "Order Entry page loads with 'Single Entry' and 'Bulk Upload' tabs.",
            "test_order_entry.py -> page.goto(order_entry_url)", "Passed"
        ),
        (
            "2.2", "2. Order Entry",
            "Select Single Entry Tab",
            "Tab Link: a:has-text('Single Entry'), #single_entry",
            "Click Action",
            "Single Entry form fields (Client, Product, Project, Order #, File) are visible.",
            "test_order_entry.py -> single_entry_tab.click()", "Passed"
        ),

        # Phase 3: Form Population
        (
            "3.1", "3. Order Details",
            "Select Client Dropdown",
            "select#Customer (name='Customer')",
            "Freedom (Option: 'CL009 / FREEDOM')",
            "Freedom client selected; triggers AJAX loading of client-specific products.",
            "test_order_entry.py -> select_option('#Customer', value='...')", "Passed"
        ),
        (
            "3.2", "3. Order Details",
            "Select Product Dropdown",
            "select#Single-ProductUID (name='ProductUID')",
            "Post closing product (Option: '22 / Post Closing Review')",
            "Post Closing Review selected; triggers AJAX loading of product projects.",
            "test_order_entry.py -> select_option('#Single-ProductUID', value='22')", "Passed"
        ),
        (
            "3.3", "3. Order Details",
            "Select Project Dropdown",
            "select#Single-ProjectUID (name='ProjectUID')",
            "freedom pcr (Option: '138 / CL138 / FREEDOM PCR Project')",
            "FREEDOM PCR Project selected successfully.",
            "test_order_entry.py -> select_option('#Single-ProjectUID', value='138')", "Passed"
        ),
        (
            "3.4", "3. Order Details",
            "Enter Dynamic Order / Loan Number",
            "input#LoanNumber (name='LoanNumber')",
            "ORD_FDM_MMDD_HHMMSS (e.g. ORD_FDM_1017_155959)",
            "Order number typed into input and stored into data/test_data.json.",
            "test_order_entry.py -> page.fill('#LoanNumber', order_number)", "Passed"
        ),
        (
            "3.5", "3. Package Upload",
            "Upload Test Loan Package Document",
            "input#DocumentUploadNew (type='file', dropify)",
            "testpackage/Testloanpackge_1.pdf",
            "PDF file attached; dropify preview card displays filename and size.",
            "test_order_entry.py -> set_input_files('#DocumentUploadNew', ...)", "Passed"
        ),
        (
            "3.6", "3. Submit Order",
            "Click Save & Continue Button",
            "button#saveandexit (class='... single_submit')",
            "Click Action (Avoids navbar #searchbtn)",
            "Form submitted; SweetAlert/processing message displays; redirects to Transactions.",
            "test_order_entry.py -> page.locator('#saveandexit').click()", "Passed"
        ),
        (
            "3.7", "3. Submit Order",
            "Confirm Order Submission & Take Screenshot",
            "URL verification: /Transactions",
            "Proof screenshot: order_created.png",
            "Order creation confirmed; screenshot saved as artifact.",
            "test_order_entry.py -> page.screenshot('order_created.png')", "Passed"
        ),

        # Phase 4: Transactions & Status Polling
        (
            "4.1", "4. Transactions",
            "Navigate to Transactions View",
            "https://laravel.stacxuat.com/Transactions",
            "Transactions URL",
            "Transactions grid (#table_allloans) renders listing pending orders.",
            "test_classification.py -> page.goto(transactions_url)", "Passed"
        ),
        (
            "4.2", "4. Filter & Search",
            "Filter Grid by Created Order Number",
            "input#custom_search_value (type='search')",
            "ORD_FDM_1017_155959 (Loaded from data/test_data.json)",
            "Search term entered and Enter pressed; DataTables filters to 1 matching row.",
            "test_classification.py -> filter_by_order_number()", "Passed"
        ),
        (
            "4.3", "4. Extract STACX ID",
            "Extract Generated STACX ID",
            "Table #table_allloans -> tbody tr td (Index 1)",
            "STACX ID Pattern: MCL... (e.g. MCL72626122406)",
            "STACX ID extracted from cell 1 and saved into data/test_data.json.",
            "test_classification.py -> extract_stacx_id_and_status()", "Passed"
        ),
        (
            "4.4", "4. Monitor Status",
            "Verify Initial Processing Status",
            "Table #table_allloans -> tbody tr td (Index 6)",
            "Current Status: 'Auto Classification In Progress'",
            "Status confirmed active; polling timer initiated with 8-second intervals.",
            "test_classification.py -> loop check", "Passed"
        ),
        (
            "4.5", "4. Polling Loop",
            "Poll Status until Target State Reached",
            "DataTables auto-refresh / Enter on #custom_search_value",
            "Target: 'Ready for manual classification' (Max 300s timeout)",
            "Script checks status every 8s while order transitions through OCR/Auto-Classification.",
            "test_classification.py -> while elapsed < max_poll_seconds", "Passed"
        ),
        (
            "4.6", "4. Final Verification",
            "Confirm Target Status Reached",
            "Table #table_allloans -> td.nth(6): 'Ready for Manual Classification'",
            "Status: 'Ready for Manual Classification', Auto Classified: 77.03%",
            "Target achieved! Status updated in test_data.json; proof screenshot captured.",
            "test_classification.py -> save_test_data() & screenshot", "Passed"
        ),
        (
            "4.7", "4. Artifact Capture",
            "Capture Proof Screenshot",
            "classification_ready.png",
            "Visual evidence of filtered row with STACX ID and Ready status",
            "Screenshot saved to workspace root for audit and test reporting.",
            "test_classification.py -> page.screenshot('classification_ready.png')", "Passed"
        ),

        # Phase 5: Manual Classification Workflow
        (
            "5.1", "5. Classification Workflow",
            "Switch to Classification Workflow Tab",
            ".TransactionWorkflowTab li:has-text('Classification')",
            "Click Action",
            "Active workflow tab updates to 'Classification' with filtered orders.",
            "test_manual_classification.py -> cls_tab.click()", "Passed"
        ),
        (
            "5.2", "5. Classification Workflow",
            "Filter Grid by STACX ID",
            "input#custom_search_value",
            "MCL72626122406",
            "Table filters to target order row; loading indicator completes.",
            "test_manual_classification.py -> filter_by_stacx_id()", "Passed"
        ),
        (
            "5.3", "5. Classification Workflow",
            "Open Action Menu & Select 'Classification'",
            "tr td:last-child .dropdown-toggle -> a:has-text('Classification')",
            "Action 3-Dots -> 'Classification'",
            "Action dropdown displays; clicking 'Classification' initiates screen navigation.",
            "test_manual_classification.py -> action_btn.click() -> cls_item.click()", "Passed"
        ),
        (
            "5.4", "5. Classification Screen",
            "Load Classification Screen & Handle Edit Mode Prompt",
            "/Indexing/index/... & button:has-text('Open in Edit Mode')",
            "Click 'Open in Edit Mode' (if prompted)",
            "Document viewer and indexing tree load with thumbnails and controls.",
            "test_manual_classification.py -> edit_mode_btn.click() & wait_for_url", "Passed"
        ),
        (
            "5.5", "5. Metrics Inspection",
            "Inspect Total Pages, OCR Confidence & Counts",
            "#Total_Count, #Classi_Count, .page-cofidence-legends-range button",
            "Total: 74 | Classified: 57 | Unclassified: 17",
            "Metrics captured: OCR Legends (100%: 6, 95-99.9%: 22, 75-89.9%: 19, 0-74.9%: 10).",
            "test_manual_classification.py -> evaluate metrics & screenshot", "Passed"
        ),
        (
            "5.6", "5. Page Indexing",
            "Assign Unclassified Pages to 1st Doc Type",
            "#unclassifiedPageContainerId .checkbox_unsorted & .stackdropdown",
            "Select All 17 pages -> Doc Type 1: 'Attorney Representation Notice - 1'",
            "All 17 checkboxes checked; sortpages() merges pages into Doc Type 1. Classified becomes 74 of 74.",
            "test_manual_classification.py -> page.evaluate(sortpages)", "Passed"
        ),
        (
            "5.7", "5. Save & Confirm",
            "Save Classification Changes & Verify Toast",
            "window.fn_save_stacking() -> POST /Indexing/PageInsertLatest",
            "Trigger Save -> Toast: 'indexing successful'",
            "Server returns 200 OK for PageInsertLatest; 'indexing successful' toast appears bottom right.",
            "test_manual_classification.py -> expect_response('pageinsert')", "Passed"
        ),
        (
            "5.8", "5. Complete Classification",
            "Click 'Classification Complete' & Confirm Dialog",
            "button#stackingcomplete & .swal-modal .swal-button--catch",
            "Click 'Classification Complete' -> 'Complete & Go to My Loans!'",
            "System checks UnClassify_Count (0 remaining); SweetAlert confirms completion and redirects.",
            "test_manual_classification.py -> stackingcomplete.click() -> swal_catch.click()", "Passed"
        ),

        # Phase 6: Data Extraction Workflow & Pipeline Completion
        (
            "6.1", "6. Data Extraction",
            "Return to Transactions Grid",
            "https://laravel.stacxuat.com/Transactions",
            "Target Transactions URL",
            "Transactions module renders with workflow stepper.",
            "test_manual_classification.py -> page.goto(transactions_url)", "Passed"
        ),
        (
            "6.2", "6. Data Extraction",
            "Switch to 'Data Extraction' Workflow Tab",
            ".TransactionWorkflowTab li:has-text('Data Extraction')",
            "Click Action",
            "Active workflow tab updates to 'Data Extraction' grid.",
            "test_manual_classification.py -> ext_tab.click()", "Passed"
        ),
        (
            "6.3", "6. Data Extraction",
            "Filter Grid by STACX ID in Local Search",
            "input#custom_search_value",
            "MCL72626122406",
            "Table filters to order row showing current extraction stage.",
            "test_manual_classification.py -> filter_by_stacx_id(stacx_id)", "Passed"
        ),
        (
            "6.4", "6. Data Extraction",
            "Poll Pipeline Status to 'Ready for Manual Data Entry'",
            "#table_allloans tbody tr td.nth(6) / td.nth(5)",
            "Target: 'Ready for Manual Data Entry'",
            "Order transitions from 'Auto Data Extraction In Progress' to 'Ready for Manual Data Entry'.",
            "test_manual_classification.py -> status polling loop", "Passed"
        ),
        (
            "6.5", "6. Extraction Verification",
            "Verify Extraction Metrics & Capture Proof Artifact",
            "Table #table_allloans & data_extraction_ready.png",
            "Status: 'Ready for Manual Data Entry' | Auto Extracted: 100.00%",
            "Verified columns: STACX ID: MCL72626122406, Loan #: ORD_FDM_1017_155959, Extracted: 100%. Screenshot saved.",
            "test_manual_classification.py -> save_test_data() & screenshot", "Passed"
        )
    ]

    for row_idx, step in enumerate(steps_data, 5):
        fill_color = fill_zebra_even if row_idx % 2 == 0 else fill_zebra_odd
        ws1.row_dimensions[row_idx].height = 24
        
        for col_idx, val in enumerate(step, 1):
            cell = ws1.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_regular
            cell.fill = fill_color
            cell.border = border_cell

            # Specific column alignments & styling
            if col_idx == 1:
                cell.alignment = align_center
                cell.font = font_bold
            elif col_idx in [2, 8]:
                cell.alignment = align_center
            elif col_idx in [4, 7]:
                cell.font = font_code
                cell.alignment = align_code
            else:
                cell.alignment = align_left

            # Highlight Status cell
            if col_idx == 8 and val == "Passed":
                cell.fill = fill_success
                cell.font = font_success

    # Auto-adjust column widths for Sheet 1
    col_widths_ws1 = {1: 10, 2: 24, 3: 38, 4: 44, 5: 38, 6: 52, 7: 48, 8: 14}
    for col_idx, width in col_widths_ws1.items():
        col_letter = get_column_letter(col_idx)
        ws1.column_dimensions[col_letter].width = width

    # =============================================================
    # SHEET 2: Test Data & Environment Parameters
    # =============================================================
    ws2 = wb.create_sheet(title="Test Data & Config")
    ws2.views.sheetView[0].showGridLines = True

    # Title Block
    ws2.merge_cells("A1:D1")
    ws2["A1"] = "STACX Automation - Configuration & Test Data Registry"
    ws2["A1"].font = font_title
    ws2["A1"].fill = fill_title
    ws2["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws2.row_dimensions[1].height = 36

    headers_ws2 = ["Parameter / Field", "Configured Value", "Storage Location / Key", "Description & Usage"]
    ws2.row_dimensions[3].height = 26
    for col_idx, header in enumerate(headers_ws2, 1):
        cell = ws2.cell(row=3, column=col_idx, value=header)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border_header

    config_data = [
        ("Base Login URL", "https://laravel.stacxuat.com/Login/index", "data/test_data.json -> url", "Primary authentication endpoint for STACX UAT environment."),
        ("User Email", "sumitkumar.sinha@avanzetechlabs.com", "data/test_data.json -> email", "User credential for login."),
        ("User Password", "Radiant@2026", "data/test_data.json -> password", "User secret password."),
        ("2FA / OTP Code", "320516 (Dynamic)", "data/test_data.json -> otp", "6-digit TOTP code received via Google Authenticator or SMS."),
        ("Session Storage", "session_state.json", "d:/Antigravaity/session_state.json", "Encrypted Playwright storage state (cookies & localStorage) for persistent login."),
        ("Order Entry URL", "https://laravel.stacxuat.com/Orderentry/index", "data/test_data.json -> order_entry_url", "Single & Bulk Order Entry interface."),
        ("Selected Client", "Freedom (CL009 / FREEDOM)", "data/test_data.json -> client", "Target Client dropdown selection (underlying select#Customer)."),
        ("Selected Product", "Post closing product (Post Closing Review)", "data/test_data.json -> product", "Target Product dropdown selection (value='22')."),
        ("Selected Project", "freedom pcr (CL138 / FREEDOM PCR Project)", "data/test_data.json -> project", "Target Project dropdown selection (value='138')."),
        ("Dynamic Order Number", "ORD_FDM_1017_155959", "data/test_data.json -> order_number", "Unique order number generated dynamically per test run to prevent collision."),
        ("Test Package Source", "C:\\Users\\Sumitkumar.Sinha\\Downloads\\Mc Test file\\Testloanpackge_1.pdf", "Local Downloads", "Original test package file provided by the user."),
        ("Test Package Directory", "d:/Antigravaity/testpackage/Testloanpackge_1.pdf", "data/test_data.json -> package_file", "Dedicated local workspace test package repository for headless/headed reuse."),
        ("Transactions URL", "https://laravel.stacxuat.com/Transactions", "data/test_data.json -> transactions_url", "Order tracking and workflow pipeline monitoring grid."),
        ("Extracted STACX ID", "MCL72626122406", "data/test_data.json -> stacx_id", "System-generated unique identifier extracted from Table column 1."),
        ("Classification Screen URL", "https://laravel.stacxuat.com/Indexing/index/...", "Classification action URL", "Target screen for manual page indexing and document stacking."),
        ("Total Package Pages", "74 Pages", "Screen Metric #Total_Count", "Total page count extracted dynamically from classification screen."),
        ("Initial Classified Pages", "57 Pages", "Screen Metric #Classi_Count", "Number of auto-classified pages prior to manual indexing."),
        ("Initial Unclassified Pages", "17 Pages", "Unclassified container count", "Number of unclassified pages needing manual doc-type assignment."),
        ("Target Document Type", "Attorney Representation Notice - 1", "Subcategory: 7EBXJ2", "1st document type on left side to which unclassified pages were assigned."),
        ("Final Classified Pages", "74 of 74 Pages (100%)", "Updated #Classi_Count", "Complete classification count after running sortpages()."),
        ("Classification Toast", "indexing successful", "Bottom-right notification toast", "Confirmation message displayed upon saving page stacking."),
        ("Final Verified Status", "Ready for Manual Data Entry", "data/test_data.json -> status", "Target workflow gate reached after manual classification and auto-extraction."),
        ("Auto Extracted Percentage", "100.00%", "Data Extraction Grid Column 9", "Extraction completion percentage verified in grid."),
        ("Execution Mode", "Headed (headless=False)", "auth_helper.py -> launch_headed_browser", "Explicit browser execution required for audit and visual paired testing.")
    ]

    for row_idx, (param, val, loc, desc) in enumerate(config_data, 4):
        fill_color = fill_zebra_even if row_idx % 2 == 0 else fill_zebra_odd
        ws2.row_dimensions[row_idx].height = 22
        
        c1 = ws2.cell(row=row_idx, column=1, value=param)
        c2 = ws2.cell(row=row_idx, column=2, value=val)
        c3 = ws2.cell(row=row_idx, column=3, value=loc)
        c4 = ws2.cell(row=row_idx, column=4, value=desc)

        for col_idx, cell in enumerate([c1, c2, c3, c4], 1):
            cell.font = font_regular
            cell.fill = fill_color
            cell.border = border_cell
            if col_idx == 1:
                cell.font = font_bold
                cell.alignment = align_left
            elif col_idx in [2, 3]:
                cell.font = font_code
                cell.alignment = align_left
            else:
                cell.alignment = align_left

    col_widths_ws2 = {1: 28, 2: 44, 3: 40, 4: 55}
    for col_idx, width in col_widths_ws2.items():
        ws2.column_dimensions[get_column_letter(col_idx)].width = width

    # =============================================================
    # SHEET 3: Selectors & Technical Reference
    # =============================================================
    ws3 = wb.create_sheet(title="Selectors & Technical Mapping")
    ws3.views.sheetView[0].showGridLines = True

    # Title Block
    ws3.merge_cells("A1:E1")
    ws3["A1"] = "STACX Automation - DOM Selectors & Technical Reference"
    ws3["A1"].font = font_title
    ws3["A1"].fill = fill_title
    ws3["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws3.row_dimensions[1].height = 36

    headers_ws3 = ["Page / Section", "Logical Field Name", "Playwright Locator / Selector", "Element Attributes", "Implementation Notes & Gotchas"]
    ws3.row_dimensions[3].height = 26
    for col_idx, header in enumerate(headers_ws3, 1):
        cell = ws3.cell(row=3, column=col_idx, value=header)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border_header

    selectors_data = [
        ("Login Page", "Email Field", "page.locator('#Email')", "id='Email', name='Email', type='email'", "Must be populated before password."),
        ("Login Page", "Password Field", "page.locator('#Password')", "id='Password', name='Password', type='password'", "Masked password field."),
        ("Login Page", "Sign In Button", "page.locator('#submitbtn')", "id='submitbtn', type='submit'", "Submits form and redirects to /qrcode_verify_2fa."),
        ("Login Page", "2FA Code Input", "page.locator('#2fa_code')", "id='2fa_code', name='2fa_code', type='text'", "Enter 6-digit TOTP code."),
        ("Login Page", "Verify 2FA Button", "page.locator('#btn-2fa-verify')", "id='btn-2fa-verify', type='submit'", "Triggers SweetAlert verification response."),
        ("Login Page", "SweetAlert Confirm", "page.locator('.swal-button--catch')", "class='swal-button swal-button--catch'", "Clicking this modal executes window.location.replace('/Dashboard/index')."),
        ("Order Entry", "Single Entry Tab", "page.locator('#single_entry, a:has-text(\"Single Entry\")')", "id='single_entry'", "Ensures single loan order entry form is active."),
        ("Order Entry", "Client Select", "page.locator('#Customer')", "id='Customer', name='Customer', tag='<select>'", "Selects 'CL009 / FREEDOM'. Triggers AJAX event to load products."),
        ("Order Entry", "Product Select", "page.locator('#Single-ProductUID')", "id='Single-ProductUID', name='ProductUID', tag='<select>'", "Selects option with text 'Post Closing Review' (value='22'). Triggers AJAX event."),
        ("Order Entry", "Project Select", "page.locator('#Single-ProjectUID')", "id='Single-ProjectUID', name='ProjectUID', tag='<select>'", "Selects option with text 'CL138 / FREEDOM PCR Project' (value='138')."),
        ("Order Entry", "Order Number", "page.locator('#LoanNumber')", "id='LoanNumber', name='LoanNumber'", "Labeled 'Order Number *' in UI, but DOM attribute is #LoanNumber."),
        ("Order Entry", "Upload File", "page.locator('#DocumentUploadNew')", "id='DocumentUploadNew', type='file', class='dropify'", "Use set_input_files() to attach PDF without OS dialog."),
        ("Order Entry", "Submit Button", "page.locator('#saveandexit')", "id='saveandexit', type='submit', text='Save & Continue'", "CRITICAL: Do NOT click navbar #searchbtn or generic button[type='submit']."),
        ("Transactions", "Workflow Stepper Tabs", "page.locator('.TransactionWorkflowTab li')", "class='TransactionWorkflowTab'", "Switch tabs: 'Classification', 'Data Extraction', etc."),
        ("Transactions", "Table Search", "page.locator('#custom_search_value')", "id='custom_search_value', name='custom_search_value'", "CRITICAL: Top search is #search (navbar). Table filter is #custom_search_value."),
        ("Transactions", "Data Table", "page.locator('#table_allloans')", "id='table_allloans', class='dataTable'", "Primary active grid for pending orders in STACX."),
        ("Transactions", "Table Processing Indicator", "page.locator('#table_allloans_processing')", "id='table_allloans_processing'", "Wait for state='hidden' before reading rows to avoid stale data."),
        ("Transactions", "Action Menu Ellipsis", "row.locator('td').last.locator('a, button, i.fa-ellipsis-v')", "3-dots icon / .dropdown-toggle", "Opens contextual menu for target order row."),
        ("Transactions", "Classification Action", "page.locator('.dropdown-menu.show a:has-text(\"Classification\")')", "Action menu item", "Opens /Indexing/index/... for manual classification."),
        ("Classification", "Edit Mode Modal Button", "page.locator('button:has-text(\"Open in Edit Mode\")')", "class='btn btn-success'", "Required when another session or lock is present."),
        ("Classification", "Total Page Count", "page.locator('#Total_Count')", "id='Total_Count'", "Displays total pages in document package (e.g. 74)."),
        ("Classification", "Classified Count", "page.locator('#Classi_Count')", "id='Classi_Count'", "Displays currently classified pages count (e.g. 57 -> 74)."),
        ("Classification", "OCR Confidence Badges", "page.locator('.page-cofidence-legends-range button')", "class='page-cofidence-legends-range'", "Buttons representing OCR confidence score ranges."),
        ("Classification", "Unclassified Checkboxes", "page.locator('#unclassifiedPageContainerId .checkbox_unsorted')", "class='checkbox_unsorted'", "Checkboxes for selecting unclassified pages on the right."),
        ("Classification", "Doc Type Dropdown", "page.locator('.stackdropdown')", "class='stackdropdown'", "Selects target master category and subcategory."),
        ("Classification", "Doc Type Tree Item", "page.locator('.Questionlist_Document_type')", "class='Questionlist_Document_type'", "1st doc type element on left side tree."),
        ("Classification", "Save Stacking", "page.evaluate('window.fn_save_stacking()')", "POST /Indexing/PageInsertLatest", "AJAX call to commit page assignments to database."),
        ("Classification", "Indexing Toast", "page.locator('.toast, .jquery-toast-single, [class*=\"toast\"]')", "class='toastify / jquery-toast'", "Confirms 'indexing successful' bottom-right."),
        ("Classification", "Classification Complete", "page.locator('#stackingcomplete')", "id='stackingcomplete'", "Checks UnClassify_Count and triggers SweetAlert confirmation modal."),
        ("Classification", "Confirm Complete Modal", "page.locator('.swal-modal .swal-button--catch')", "class='swal-button swal-button--catch'", "Button text: 'Complete & Go to My Loans!'. Confirms final classification submission."),
        ("Data Extraction", "Workflow Tab", "page.locator('.TransactionWorkflowTab li:has-text(\"Data Extraction\")')", "class='TransactionWorkflowTab'", "Switches to Data Extraction module."),
        ("Data Extraction", "Current Status Column", "row.locator('td').nth(6)", "Column Index 6", "Displays 'Ready for Manual Data Entry' upon auto-extraction completion.")
    ]

    for row_idx, (section, field, locator, attrs, notes) in enumerate(selectors_data, 4):
        fill_color = fill_zebra_even if row_idx % 2 == 0 else fill_zebra_odd
        ws3.row_dimensions[row_idx].height = 24
        
        c1 = ws3.cell(row=row_idx, column=1, value=section)
        c2 = ws3.cell(row=row_idx, column=2, value=field)
        c3 = ws3.cell(row=row_idx, column=3, value=locator)
        c4 = ws3.cell(row=row_idx, column=4, value=attrs)
        c5 = ws3.cell(row=row_idx, column=5, value=notes)

        for col_idx, cell in enumerate([c1, c2, c3, c4, c5], 1):
            cell.font = font_regular
            cell.fill = fill_color
            cell.border = border_cell
            if col_idx == 1:
                cell.font = font_bold
                cell.alignment = align_left
            elif col_idx == 2:
                cell.font = font_bold
                cell.alignment = align_left
            elif col_idx in [3, 4]:
                cell.font = font_code
                cell.alignment = align_code
            else:
                cell.alignment = align_left

    col_widths_ws3 = {1: 18, 2: 24, 3: 48, 4: 42, 5: 60}
    for col_idx, width in col_widths_ws3.items():
        ws3.column_dimensions[get_column_letter(col_idx)].width = width

    # Save Workbook
    target_file = Path(output_path).resolve()
    wb.save(str(target_file))
    print(f"[Success] Workflow Excel generated successfully at: {target_file}")
    return target_file

if __name__ == "__main__":
    create_workflow_excel()
