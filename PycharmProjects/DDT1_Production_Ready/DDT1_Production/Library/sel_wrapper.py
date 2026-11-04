from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumWrapper:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def enter_txt(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(str(value))

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def upload_file(self, locator, file_path):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(str(file_path))
