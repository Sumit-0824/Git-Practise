# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("init_driver")
class TestLogin:

    def test_login(self):
        # Open login page
        self.driver.get("https://www.stacxuat.com/Login/index_new")

        # Initialize Page Objects
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        # Enter credentials and login
        login_page.enter_username("sumitkumar.sinha@avanzetechlabs.com")
        login_page.enter_password("Testuatdec@2025")
        login_page.click_login()

        # Wait dynamically for OTP button
        wait = WebDriverWait(self.driver, 60)  # Adjust time if needed
        otp_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-lg btn-warning ForgetPassword']")))
        otp_button.click()

        # Verify Home Page
        assert home_page.is_home_page_displayed(), "Home page not loaded! Login failed."
