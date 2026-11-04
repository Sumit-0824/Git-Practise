from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utils.Browserutils import BrowserUtils


class OrderPage(BrowserUtils):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.order_entry_button = ("xpath", "//a[@href='/order-entry']")
        self.order_entry_page_title = ("xpath", "//h1[contains(text(),'Order Entry')]")
        self.click = ("id", "select2-Customer-container")
        self.client_input = (
            "xpath",
            "//input[@class='select2-search__field']"
        )



    def navigate_to_order_entry(self):
        self.driver.find_element(*self.order_entry_button).click()
        return self

    def get_order_entry_page_title(self):
        return self.driver.find_element(*self.order_entry_page_title).text


    def enter_client_info(self, client_info):
        wait = WebDriverWait(self.driver, 15)

        # Step 1: Wait for and click Customer dropdown
        customer_dropdown = wait.until(
            expected_conditions.element_to_be_clickable(self.click)
        )
        customer_dropdown.click()

        # Step 2: Wait for the search input and enter client name
        search_input = wait.until(
            expected_conditions.visibility_of_element_located(
                self.client_input
            )
        )
        search_input.send_keys(client_info)

        # Step 3: Wait for the matching customer option
        options_locator = (
            "CSS_SELECTOR",
            "li.select2-results__option"
        )

        wait.until(
            expected_conditions.visibility_of_any_elements_located(
                options_locator
            )
        )

        options = self.driver.find_elements(*options_locator)

        # Step 4: Iterate through options and select the matching customer
        for option in options:
            if client_info.lower() in option.text.strip().lower():
                option.click()
                print(f"Selected customer: {option.text}")
                break
        else:
            raise Exception(
                f"Customer '{client_info}' not found in dropdown"
            )









