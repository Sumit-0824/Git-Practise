from data import reading_objects
from Library.sel_wrapper import selenium_wrapper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClientPage:

    # Locators
    CLIENT_DROPDOWN = (By.XPATH, "//span[@id='select2-Customer-container']/parent::span")
    SEARCH_BOX = (By.XPATH, "//input[@class='select2-search__field']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def select_client(self, client_name):
        # Click Client dropdown
        self.wait.until(
            EC.element_to_be_clickable(self.CLIENT_DROPDOWN)
        ).click()

        # Enter client name
        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )
        search_box.clear()
        search_box.send_keys(client_name)

        # Click matching option
        option = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//li[contains(@class,'select2-results__option') and normalize-space()='{client_name}']"
                )
            )
        )
        option.click()

        # Verify selected client
        selected_client = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "select2-Customer-container")
            )
        ).text

        assert selected_client == client_name, \
            f"Expected '{client_name}', but found '{selected_client}'"

        print(f"Client '{selected_client}' selected successfully.")
