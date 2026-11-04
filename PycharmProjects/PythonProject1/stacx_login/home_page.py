# home_page.py
from selenium.webdriver.common.by import By
from base_page import BasePage

class HomePage(BasePage):
    HOME_HEADER = (By.XPATH, "//h1[contains(text(), 'Home')]")

    def is_home_page_displayed(self):
        try:
            self.find_element(*self.HOME_HEADER)
            return True
        except:
            return False
