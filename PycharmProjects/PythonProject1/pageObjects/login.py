from pageObjects.shop import ShopPage
from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.username_input = ("id", "username")  # Replace with the actual locator
        self.password_input = ("id","password")  # Replace with the
        self.sign_in_button = ("id", "signInBtn")  # Replace with the actual locator


    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sign_in_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page
