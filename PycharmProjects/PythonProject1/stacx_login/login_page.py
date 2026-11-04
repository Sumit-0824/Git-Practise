# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "Username")
    PASSWORD_FIELD = (By.ID, "Password")
    LOGIN_BUTTON = (By.ID, "submit")
    OTP_BUTTON = (By.XPATH, "//*[@class='btn btn-lg btn-warning ForgetPassword']")

    def enter_username(self, username):
        self.send_keys(*self.USERNAME_FIELD, text=username)

    def enter_password(self, password):
        self.send_keys(*self.PASSWORD_FIELD, text=password)

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)

    def click_otp_verification(self):
        self.click(*self.OTP_BUTTON)
