from pageObjects.checkout_confirmation import Checkout_Confirmation
from utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils) :

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.shop_link = ("xpath", "//a[text()='Shop']")
        self.product_cards = ("xpath", "//div[@class='card h-100']")
        self.checkout_button = ("xpath", "//a[@class='nav-link btn btn-primary']")


    def add_item_to_cart(self,product_name):   #(do not _as prefix in method name)


        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            product_Name = product.find_element("xpath", "div/h4/a").text
            if product_Name == "product_name":

                product.find_element("xpath", "div/button").click()


    def go_to_cart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation_page = Checkout_Confirmation(self.driver)
        return checkout_confirmation_page






