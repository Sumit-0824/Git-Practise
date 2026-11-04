from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserutils import BrowserUtils


class Checkout_Confirmation(BrowserUtils):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.checkout_button= ("xpath", "//button[contains(@class,'btn-success')]")
        self.country_input = ("id", "country")
        self.country_option = ("link text", "India")
        self.checkbox = ("xpath", "//div[@class='checkbox checkbox-primary']")
        self.submit_button = ("css selector", "input[type='submit']")
        self.success_message = ("class name", 'alert-success')




    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()


    def enter_delivery_address(self,countryName):

        self.driver.find_element(*self.country_input).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()


    def validate_success_message(self):
        success_text = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in success_text