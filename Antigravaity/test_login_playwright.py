import pytest
from playwright.sync_api import sync_playwright, expect


def test_navigate_and_verify_login_playwright():
    with sync_playwright() as p:
        # Launch in headed mode using system Microsoft Edge browser channel
        browser = p.chromium.launch(channel="msedge", headless=False, slow_mo=500)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # Step 1: Navigate to the given URL
        target_url = "https://app-uat.stacx.ai/"
        print(f"\n[Step 1] Navigating to: {target_url}")
        page.goto(target_url, wait_until="networkidle")

        # Step 2: Verify user is able to view the login page
        print("[Step 2] Verifying login page redirection and elements...")

        # Wait for redirect to /login
        page.wait_for_url("**/login**", timeout=15000)
        print(f" -> Current URL: {page.url}")
        print(f" -> Page Title: {page.title()}")

        # Locate key login elements
        email_input = page.locator("input[type='email']")
        password_input = page.locator("input[type='password']")
        submit_btn = page.locator("button[type='submit']")
        heading = page.locator("h2.card-title")

        # Assert visibility
        expect(email_input).to_be_visible(timeout=10000)
        expect(password_input).to_be_visible(timeout=10000)
        expect(submit_btn).to_be_visible(timeout=10000)
        expect(heading).to_be_visible(timeout=10000)

        print(" -> Work Email Input: Visible")
        print(" -> Password Input: Visible")
        print(" -> Sign in Button: Visible")
        print(" -> 'Welcome back' Title: Visible")

        # Verify SSO buttons
        ms_sso = page.get_by_text("Sign in with Microsoft")
        google_sso = page.get_by_text("Sign in with Google")
        expect(ms_sso).to_be_visible(timeout=5000)
        expect(google_sso).to_be_visible(timeout=5000)
        print(" -> Microsoft & Google SSO Buttons: Visible")

        # Save screenshot verification
        screenshot_path = "login_page_playwright.png"
        page.screenshot(path=screenshot_path)
        # Pause for 7 seconds in headed mode so you can view the browser window
        print(" -> Browser is open on screen. Pausing 7 seconds before closing...")
        page.wait_for_timeout(7000)

        browser.close()
        print("\n[SUCCESS] Step 1 and Step 2 verified successfully via Playwright!")


if __name__ == "__main__":
    test_navigate_and_verify_login_playwright()
