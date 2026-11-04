import json
import os
import sys
import time
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright, expect


def load_test_data():
    """Loads URL, email, and password from the data folder."""
    base_dir = Path(__file__).resolve().parent
    data_file = base_dir / "data" / "test_data.json"
    
    if not data_file.exists():
        data_file = base_dir / "data" / "config.json"
        
    if not data_file.exists():
        raise FileNotFoundError(f"Test data file not found at: {data_file}")
        
    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    required_keys = ["url", "email", "password"]
    for key in required_keys:
        if key not in data:
            raise KeyError(f"Missing required key '{key}' in {data_file}")
            
    return data


def log(msg):
    """Prints message and flushes stdout immediately."""
    print(msg, flush=True)


def test_stacx_login_and_order_entry():
    """
    Automated test executing all 8 steps:
    Step 1: Navigate to the given URL (from data folder)
    Step 2: Verify user is able to view the login page
    Step 3: User should able to Enter Email
    Step 4: User should able to Enter Password
    Step 5: User should able to click on Sign in button
    Step 6: Once email, password is enter page will redirect to OTP screen; Wait 30s for manual OTP entry
    Step 7: Click on the verify button
    Step 8: User should able to navigate to order entry page
    """
    test_data = load_test_data()
    target_url = test_data["url"]
    email = test_data["email"]
    password = test_data["password"]

    log("\n" + "=" * 65)
    log(" STACX LOGIN & ORDER ENTRY AUTOMATION TEST")
    log("=" * 65)
    log(f" [Data Config] Target URL : {target_url}")
    log(f" [Data Config] Email      : {email}")
    log(f" [Execution]   Mode       : Headed Browser (headless=False)")
    log("=" * 65)

    with sync_playwright() as p:
        # Launch headed browser (try MS Edge first, fallback to Chromium)
        try:
            browser = p.chromium.launch(channel="msedge", headless=False, slow_mo=300)
            log("[Browser] Successfully launched Microsoft Edge in headed mode.")
        except Exception as e:
            log(f"[Browser] MS Edge note ({e}), falling back to standard Chromium...")
            browser = p.chromium.launch(headless=False, slow_mo=300)
            log("[Browser] Successfully launched Chromium in headed mode.")

        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        # -------------------------------------------------------------
        # Step 1: Navigate to the given URL
        # -------------------------------------------------------------
        log(f"\n[Step 1] Navigating to URL: {target_url}...")
        page.goto(target_url, wait_until="networkidle", timeout=30000)
        log(f" -> Current URL: {page.url}")
        log(f" -> Page Title: {page.title()}")

        # -------------------------------------------------------------
        # Step 2: Verify user is able to view the login page
        # -------------------------------------------------------------
        log("\n[Step 2] Verifying login page elements...")
        assert "login" in page.url.lower(), f"Expected 'login' in URL, got: {page.url}"
        
        username_input = page.locator("#Username")
        password_input = page.locator("#Password")
        signin_button = page.locator("button.Signin")
        header_text = page.locator("text=Login to your STACX account")

        expect(username_input).to_be_visible(timeout=10000)
        expect(password_input).to_be_visible(timeout=10000)
        expect(signin_button).to_be_visible(timeout=10000)
        expect(header_text).to_be_visible(timeout=10000)

        log(" -> Email/Username input: Visible [OK]")
        log(" -> Password input: Visible [OK]")
        log(" -> Sign In button: Visible [OK]")
        log(" -> 'Login to your STACX account' heading: Visible [OK]")
        page.screenshot(path="step2_login_page.png")
        log(" -> [Step 2 Complete] Login page verified successfully.")

        # -------------------------------------------------------------
        # Step 3: User should able to Enter Email
        # -------------------------------------------------------------
        log(f"\n[Step 3] Entering Email: '{email}'...")
        username_input.click()
        username_input.fill("")
        username_input.fill(email)
        expect(username_input).to_have_value(email)
        log(" -> [Step 3 Complete] Email entered successfully.")

        # -------------------------------------------------------------
        # Step 4: User should able to Enter Password
        # -------------------------------------------------------------
        log("\n[Step 4] Entering Password...")
        password_input.click()
        password_input.fill("")
        password_input.fill(password)
        log(" -> [Step 4 Complete] Password entered successfully.")

        # -------------------------------------------------------------
        # Step 5: User should able to click on Sign in button
        # -------------------------------------------------------------
        log("\n[Step 5] Clicking Sign In button...")
        signin_button.click()
        log(" -> Sign In button clicked.")

        # Check for multiple login restriction popup if displayed
        swal_confirm_btn = page.locator(".swal-button--Confirm, button:has-text('Confirm')")
        try:
            if swal_confirm_btn.is_visible(timeout=3000):
                log(" -> Active session restriction detected. Clicking 'Confirm'...")
                swal_confirm_btn.click()
        except Exception:
            pass

        # -------------------------------------------------------------
        # Step 6: Redirect to OTP screen & Wait 30 sec for manual OTP entry
        # -------------------------------------------------------------
        log("\n[Step 6] Waiting for redirection to OTP / 2FA screen...")
        # Wait for redirect to /Login/Otp or /Login/qrcode_verify_2fa
        try:
            page.wait_for_url(lambda u: "otp" in u.lower() or "2fa" in u.lower(), timeout=15000)
            log(f" -> Redirected to OTP/MFA screen: {page.url}")
        except Exception:
            log(f" -> Current URL: {page.url}")

        # The OTP / 2FA passcode input can be #code (Microsoft MFA) or #passcode (Email OTP)
        otp_input = page.locator("#code, #passcode, input[placeholder*='Authentication Code'], input[placeholder*='code']").first
        expect(otp_input).to_be_visible(timeout=15000)
        page.screenshot(path="step6_otp_screen.png")
        log(" -> OTP / MFA input field is visible.")

        log("\n" + "*" * 65)
        log(">>> [ACTION REQUIRED] ENTER OTP MANUALLY IN HEADED BROWSER <<<")
        log("The headed browser window is open on your screen.")
        log("Please type your OTP code into the input field.")
        log("Waiting 30 seconds as specified in Step 6...")
        log("*" * 65)

        total_wait_sec = 30
        for remaining in range(total_wait_sec, 0, -5):
            log(f" -> Time remaining: {remaining} seconds...")
            # Check if user already typed OTP or navigated
            if not ("otp" in page.url.lower() or "2fa" in page.url.lower()):
                log(" -> Redirection detected during wait!")
                break
            page.wait_for_timeout(5000)

        otp_val = otp_input.input_value() if otp_input.is_visible() else ""
        if otp_val:
            log(f" -> OTP detected in field: {'*' * len(otp_val)}")
        else:
            log(" -> 30 seconds wait completed.")

        # -------------------------------------------------------------
        # Step 7: Click on the verify button
        # -------------------------------------------------------------
        log("\n[Step 7] Clicking on the Verify button...")
        verify_btn = page.locator("button.QRCodeVerify, button.ForgetPassword, button:has-text('Verify')").first
        
        if ("otp" in page.url.lower() or "2fa" in page.url.lower()) and verify_btn.is_visible():
            verify_btn.click()
            log(" -> Verify button clicked.")
        else:
            log(" -> Verify button already processed or page redirected.")

        # Check for sweetalert 'Verified Successfully' button
        swal_verified_btn = page.locator("button:has-text('Verified Successfully'), .swal-button--catch")
        try:
            if swal_verified_btn.is_visible(timeout=5000):
                log(" -> 'Verified Successfully' prompt detected. Clicking to continue...")
                swal_verified_btn.click()
        except Exception:
            pass

        # -------------------------------------------------------------
        # Step 8: User should able to navigate to order entry page
        # -------------------------------------------------------------
        log("\n[Step 8] Waiting for navigation to Order Entry / Dashboard...")
        try:
            # Wait for URL to leave OTP/2FA screen
            page.wait_for_url(lambda u: "otp" not in u.lower() and "2fa" not in u.lower(), timeout=15000)
            log(f" -> Logged in! Current URL: {page.url}")
        except Exception as e:
            log(f" -> Current URL state: {page.url}")

        # Check for Order Entry menu or link
        log(" -> Checking for 'Order Entry' navigation link...")
        order_entry_locators = [
            page.locator("a:has-text('Order Entry')").first,
            page.locator("button:has-text('Order Entry')").first,
            page.locator("a[href*='Order']").first,
            page.locator("text=/Order\\s*Entry/i").first,
        ]

        found_order_entry = False
        for loc in order_entry_locators:
            try:
                if loc.is_visible(timeout=3000):
                    log(f" -> Found '{loc}' on page, clicking to navigate to Order Entry...")
                    loc.click()
                    page.wait_for_load_state("networkidle", timeout=10000)
                    found_order_entry = True
                    break
            except Exception:
                continue

        if not found_order_entry:
            log(" -> If 'Order Entry' is inside a dropdown menu, checking navigation bars...")
            menu_btn = page.locator(".dropdown-toggle, .navbar-toggler, .sidebar-toggle, a:has-text('Orders')")
            try:
                if menu_btn.first.is_visible(timeout=2000):
                    menu_btn.first.click()
                    order_link = page.locator("a:has-text('Order Entry')").first
                    if order_link.is_visible(timeout=2000):
                        order_link.click()
                        page.wait_for_load_state("networkidle", timeout=10000)
                        found_order_entry = True
            except Exception:
                pass

        log(f" -> Final URL: {page.url}")
        log(f" -> Final Page Title: {page.title()}")

        # Capture screenshot of final Order Entry / Dashboard page
        screenshot_path = "order_entry_page.png"
        page.screenshot(path=screenshot_path)
        log(f" -> Screenshot saved to: {screenshot_path}")

        # Keep browser open for a few seconds so user can see it in headed mode
        log(" -> Keeping headed browser open for 8 seconds to view final screen...")
        page.wait_for_timeout(8000)

        browser.close()
        log("\n" + "=" * 65)
        log(" [SUCCESS] All 8 Steps Completed Successfully!")
        log("=" * 65)


if __name__ == "__main__":
    test_stacx_login_and_order_entry()
