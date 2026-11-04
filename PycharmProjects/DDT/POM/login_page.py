import time
from data import reading_objects
from Library.sel_wrapper import selenium_wrapper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium  import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.stacxuat.com/Login/index")
# driver.maximize_window()
login_object=reading_objects.reading_locators()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.sel_wrapper = selenium_wrapper(driver)
    def enter_email(self):
        #driver.find_element(*login_object["txt_email"]).send_keys("sumitkumar.sinha@avanzetechlabs.com")
        self.sel_wrapper.enter_txt(login_object["txt_email"],"sumitkumar.sinha@avanzetechlabs.com")
    def enter_password(self):
        #driver.find_element(*login_object["txt_pwd"]).send_keys("Testuatdec@2025")
        self.sel_wrapper.enter_txt(login_object["txt_pwd"],"Testpreprod@202562ss")
    def click_login_button(self):
        #driver.find_element(*login_object["btn_login"]).click()
        self.sel_wrapper.click_element(login_object["btn_login"])
        self.driver.implicitly_wait(40)

    def click_verify_button(self):

        #driver.find_element(*login_object["btn_verify"]).click()
        self.sel_wrapper.click_element(login_object["btn_verify"])

    def click_single_entry(self):
        self.sel_wrapper.click_element(login_object["btn_single_entry"])

    # def click_client(self):
    #     self.sel_wrapper.click_element(login_object["btn_client"])
    #     self.driver.implicitly_wait(40)

    def enter_client(self):
        wait = WebDriverWait(self.driver, 20)

        # Click Client dropdown
        self.sel_wrapper.click_element(login_object["CLIENT_DROPDOWN"])

        # Type client name
        self.sel_wrapper.enter_txt(login_object["SEARCH_BOX"], "CL101 / InsigHub Testing")

        # Click matching option
        option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//li[normalize-space()='CL101 / InsigHub Testing']")
            )
        )
        option.click()

    def select_product(self, product_name):
        wait = WebDriverWait(self.driver, 20)

        # Click Product dropdown
        self.sel_wrapper.click_element(login_object["PRODUCT_DROPDOWN"])

        # Wait for search box and type product
        search = wait.until(
            EC.visibility_of_element_located(login_object["SEARCH_BOX"])
        )
        search.clear()
        search.send_keys(product_name)

        # Click matching product
        wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//li[normalize-space()='{product_name}']"
                )
            )
        ).click()

    def enter_ordernumber(self):
        self.sel_wrapper.enter_txt(login_object["txt_ordernumber"], "Testloansk250926004")

    def upload_document(self):
        file_path = r"C:\Users\Sumitkumar.Sinha\Desktop\selenium\testpackage.pdf"

        upload = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(login_object["DOCUMENT_UPLOAD"])
        )

        upload.send_keys(file_path)

    def click_save_continue(self):
        wait = WebDriverWait(self.driver, 30)

        button = wait.until(
            EC.element_to_be_clickable(login_object["BTN_SAVE_CONTINUE"])
        )

        button.click()

        # Wait until the button becomes stale (page reload)
        wait.until(EC.staleness_of(button))

# class classificationPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.sel_wrapper = selenium_wrapper(driver)

    def click_classification(self):
        self.sel_wrapper.click_element(login_object["btn_classification"])

    def search_loan(self, loan_number):
        wait = WebDriverWait(self.driver, 20)

        # Click Loan Search dropdown
        self.sel_wrapper.click_element(login_object["LOAN_SEARCH_DROPDOWN"])

        # Type loan number
        self.sel_wrapper.enter_txt(login_object["SEARCH_BOX"], loan_number)

        # Click matching option
        option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//li[normalize-space()='{loan_number}']")
            )
        )
        option.click()




# lp=LoginPage(driver)
# lp.enter_email()
# lp.enter_password()
# lp.click_login_button()
# lp.click_verify_button()