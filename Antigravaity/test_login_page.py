import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigate_and_verify_login():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Edge(options=options)
    wait = WebDriverWait(driver, 15)

    try:
        # Step 1: Navigate to the given URL
        target_url = "https://app-uat.stacx.ai/"
        print(f"[Step 1] Navigating to: {target_url}")
        driver.get(target_url)

        # Step 2: Verify user is able to view the login page
        print("[Step 2] Verifying login page redirection and elements...")

        # Wait until the URL changes to include '/login' or elements are visible
        wait.until(lambda d: "/login" in d.current_url)
        current_url = driver.current_url
        page_title = driver.title
        print(f" -> Redirected URL: {current_url}")
        print(f" -> Page Title: {page_title}")

        # Wait for the login form elements to render
        email_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[autocomplete='username']"))
        )
        password_input = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
        )
        submit_btn = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
        )

        # Check for card title and SSO buttons
        page_text = driver.find_element(By.TAG_NAME, "body").text
        is_welcome_back_present = "Welcome back" in page_text or "Sign in" in page_text

        # Assertions
        assert "/login" in current_url, f"Expected URL to contain '/login', got: {current_url}"
        assert email_input.is_displayed(), "Work email input is not visible"
        assert password_input.is_displayed(), "Password input is not visible"
        assert submit_btn.is_displayed(), "Sign in button is not visible"
        assert is_welcome_back_present, "Expected login text ('Welcome back' / 'Sign in') not found"

        print(" -> Work Email Input: Visible")
        print(" -> Password Input: Visible")
        print(" -> Sign in Button: Visible")
        # Set stdout encoding safety or print repr/clean ascii
        print(f" -> Submit Button Text: {submit_btn.text.encode('ascii', 'backslashreplace').decode('ascii')}")

        # Check SSO buttons
        buttons = driver.find_elements(By.TAG_NAME, "button")
        button_texts = [b.text.strip().encode('ascii', 'backslashreplace').decode('ascii') for b in buttons if b.text.strip()]
        print(f" -> Action Buttons: {button_texts}")

        # Take a screenshot as proof of verification
        screenshot_path = "login_page_verified.png"
        driver.save_screenshot(screenshot_path)
        print(f" -> Verification screenshot saved to: {screenshot_path}")

        print("\n[SUCCESS] Step 1 and Step 2 verified successfully!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_navigate_and_verify_login()
