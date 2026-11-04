from selenium.webdriver.common.by import By
from Library.sel_wrapper import SeleniumWrapper

class LoginPage:
    USERNAME = (By.ID, "Username")
    PASSWORD = (By.ID, "Password")
    LOGIN = (By.ID, "submit")
    VERIFY = (By.XPATH, "//*[@class='btn btn-lg btn-warning ForgetPassword']")

    def __init__(self, driver):
        self.ui = SeleniumWrapper(driver)

    def login(self, username, password):
        self.ui.enter_txt(self.USERNAME, username)
        self.ui.enter_txt(self.PASSWORD, password)
        self.ui.click_element(self.LOGIN)
