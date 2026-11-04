import json
import os
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "test_data.json"
CONFIG_FILE = BASE_DIR / "data" / "config.json"
SESSION_STATE_FILE = BASE_DIR / "session_state.json"
TESTPACKAGE_FILE = BASE_DIR / "testpackage" / "Testloanpackge_1.pdf"


def log(msg):
    """Prints message with immediate stdout flushing and safe unicode handling on Windows."""
    try:
        print(msg, flush=True)
    except (UnicodeEncodeError, Exception):
        safe_msg = str(msg).encode("ascii", errors="replace").decode("ascii")
        print(safe_msg, flush=True)


def load_test_data():
    """Loads configuration and credentials from data folder."""
    if not DATA_FILE.exists():
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            raise FileNotFoundError(f"Test data file not found at: {DATA_FILE}")
    else:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    return data


def save_test_data(data):
    """Saves updated data dynamically to data/test_data.json and data/config.json."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    log(f"[Data] Updated test data saved to: {DATA_FILE}")


def launch_headed_browser(playwright_instance):
    """Launches browser in headed mode (MS Edge preferred, fallback to Chromium)."""
    try:
        browser = playwright_instance.chromium.launch(channel="msedge", headless=False, slow_mo=300)
        log("[Browser] Launched Microsoft Edge in headed mode.")
    except Exception as e:
        log(f"[Browser] MS Edge launch notice ({e}), launching Chromium in headed mode...")
        browser = playwright_instance.chromium.launch(headless=False, slow_mo=300)
        log("[Browser] Launched Chromium in headed mode.")
    return browser


def create_browser_context(browser):
    """Creates a browser context, loading saved session state if available."""
    if SESSION_STATE_FILE.exists():
        log(f"[Session] Found existing session state: {SESSION_STATE_FILE}")
        try:
            context = browser.new_context(
                storage_state=str(SESSION_STATE_FILE),
                viewport={"width": 1440, "height": 900}
            )
            return context, True
        except Exception as e:
            log(f"[Session] Note loading session state ({e}), creating fresh context...")
    
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    return context, False


def ensure_authenticated_page(browser, context, test_data, target_url=None):
    """
    Ensures that the page is authenticated.
    If session is valid, navigates to target_url.
    If session expired or not logged in, performs login (with OTP step) and saves session_state.json.
    """
    if target_url is None:
        target_url = test_data.get("order_entry_url", "https://laravel.stacxuat.com/Orderentry/index")

    page = context.new_page()
    
    if not SESSION_STATE_FILE.exists():
        log("[Auth] No session state found. Performing login flow first...")
        perform_login(page, context, test_data)
        if target_url not in page.url:
            order_link = page.locator("a:has-text('Order Entry')").first
            try:
                if "orderentry" in target_url.lower() and order_link.is_visible():
                    log(" -> Clicking 'Order Entry' from top navbar...")
                    order_link.click()
                    page.wait_for_load_state("domcontentloaded")
                else:
                    log(f"[Auth] Navigating to target URL: {target_url}...")
                    page.goto(target_url, wait_until="domcontentloaded", timeout=30000)
            except Exception:
                page.goto(target_url, wait_until="domcontentloaded", timeout=30000)
    else:
        log(f"\n[Auth] Checking session by navigating to: {target_url}...")
        try:
            page.goto(target_url, wait_until="domcontentloaded", timeout=30000)
        except Exception as e:
            log(f"[Auth] Notice during navigation ({e}), retrying with load...")
            page.goto(target_url, wait_until="load", timeout=30000)

        # Check if we were redirected to Login or LandingPage
        if "login" in page.url.lower() or "landingpage" in page.url.lower():
            log("[Auth] Session expired or redirected to login/landing. Performing login flow...")
            perform_login(page, context, test_data)
            if target_url not in page.url:
                order_link = page.locator("a:has-text('Order Entry')").first
                try:
                    if "orderentry" in target_url.lower() and order_link.is_visible():
                        log(" -> Clicking 'Order Entry' from top navbar...")
                        order_link.click()
                        page.wait_for_load_state("domcontentloaded")
                    else:
                        page.goto(target_url, wait_until="domcontentloaded", timeout=30000)
                except Exception:
                    page.goto(target_url, wait_until="domcontentloaded", timeout=30000)
        else:
            log(f"[Auth] Already authenticated! Active on: {page.url}")
            try:
                context.storage_state(path=str(SESSION_STATE_FILE))
            except Exception:
                pass

    return page


def perform_login(page, context, test_data):
    """Performs full login and OTP verification in headed mode."""
    login_url = test_data.get("url", "https://laravel.stacxuat.com/Login/index")
    email = test_data["email"]
    password = test_data["password"]

    if "login" not in page.url.lower():
        page.goto(login_url, wait_until="domcontentloaded", timeout=30000)

    log(f" -> Filling Email: {email}")
    username_input = page.locator("#Username")
    expect(username_input).to_be_visible(timeout=10000)
    username_input.fill(email)

    log(" -> Filling Password...")
    password_input = page.locator("#Password")
    password_input.fill(password)

    log(" -> Clicking Sign In button...")
    page.locator("button.Signin").click()

    # Handle active session warning if prompted (use wait_for so we don't miss AJAX response)
    swal_confirm_btn = page.locator(".swal-button--Confirm, button:has-text('Confirm')").first
    try:
        swal_confirm_btn.wait_for(state="visible", timeout=5000)
        log(" -> Active session popup detected. Clicking 'Confirm'...")
        swal_confirm_btn.click()
    except Exception:
        pass

    # Wait for OTP/2FA screen
    log(" -> Waiting for redirection to OTP / MFA screen...")
    try:
        page.wait_for_url(lambda u: "otp" in u.lower() or "2fa" in u.lower(), timeout=20000)
        log(f" -> Redirected to OTP/MFA screen: {page.url}")
    except Exception:
        log(f" -> Current URL: {page.url}")

    otp_input = page.locator("#code, #passcode, input[placeholder*='Authentication Code'], input[placeholder*='code']").first
    try:
        otp_input.wait_for(state="visible", timeout=15000)
    except Exception:
        pass

    try:
        page.bring_to_front()
    except Exception:
        pass

    entered_code = False
    if test_data.get("otp"):
        log(f" -> Automatically filling provided OTP: {test_data['otp']}")
        otp_input.fill(str(test_data["otp"]))
        entered_code = True

    if not entered_code:
        log("\n" + "*" * 65)
        log(">>> [ACTION REQUIRED] ENTER OTP MANUALLY IN HEADED BROWSER <<<")
        log("Please enter your 6-digit OTP code in the opened browser window.")
        log("The script will automatically detect your code and proceed!")
        log("*" * 65)

    # Wait up to 120 seconds for user to type OTP or for page to navigate
    max_wait_sec = 120
    for i in range(max_wait_sec):
        if entered_code:
            break
        # Check if user already submitted and navigated
        if not ("otp" in page.url.lower() or "2fa" in page.url.lower() or "login" in page.url.lower()):
            log(" -> Page navigation away from OTP detected! Login proceeding...")
            break

        # Check if OTP code was typed into the input
        try:
            val = otp_input.input_value().strip()
            if len(val) >= 6:
                log(f" -> OTP code detected ({len(val)} digits entered).")
                entered_code = True
                break
        except Exception:
            pass

        if i > 0 and i % 5 == 0:
            log(f" -> Waiting for OTP entry ({max_wait_sec - i} seconds remaining)...")
        page.wait_for_timeout(1000)

    # If code was entered and still on OTP page, click Verify
    if entered_code and ("otp" in page.url.lower() or "2fa" in page.url.lower()):
        page.wait_for_timeout(1000)
        verify_btn = page.locator("button.QRCodeVerify, button.ForgetPassword, button:has-text('Verify')").first
        try:
            if verify_btn.is_visible():
                verify_btn.click()
                log(" -> Clicked Verify button.")
        except Exception:
            pass

    # Check for 'Verified Successfully' popup vs error popup
    swal_verified = page.locator("button:has-text('Verified Successfully'), .swal-button--catch, .swal-button:has-text('OK')").first
    swal_warning = page.locator(".swal-icon--warning").first

    try:
        swal_verified.wait_for(state="visible", timeout=8000)
        swal_verified.click()
        log(" -> Confirmed 'Verified Successfully' popup.")
    except Exception:
        pass

    # Wait for post-login dashboard redirect
    log(" -> Waiting for Dashboard redirection...")
    page.wait_for_url(lambda u: "dashboard" in u.lower() or "orderentry" in u.lower() or "transaction" in u.lower(), timeout=25000)
    log(f"[Auth] Successfully logged in! Current URL: {page.url}")
    page.wait_for_timeout(2000)

    # Save session state so subsequent runs don't need to re-login!
    try:
        context.storage_state(path=str(SESSION_STATE_FILE))
        log(f"[Auth] Saved session state to: {SESSION_STATE_FILE}")
    except Exception as e:
        log(f"[Auth] Session save notice: {e}")
