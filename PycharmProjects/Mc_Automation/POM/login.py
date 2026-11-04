
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM import order_entry
from Utils.Browserutils import BrowserUtils



class LoginPage(BrowserUtils):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.username_input = ("id", "Username")
        self.password_input = ("id","Password")
        self.sign_in_button = ("xpath", "//button [@type='submit']")
        self.enter_otp= ("id","code")
        self.verify= ("xpath", "//button [@type='submit']")

    def login(self, username, password, wait=None):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sign_in_button).click()
        self.driver.implicitly_wait(20)
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.presence_of_element_located(self.enter_otp))
        self.driver.find_element(*self.verify).click()



        order_page = order_entry.OrderPage(self.driver)
        return order_page