import time
from data import reading_objects
from Library.sel_wrapper import selenium_wrapper
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
        self.sel_wrapper.enter_txt(login_object["txt_pwd"],"Testpreprod@20256")
    def click_login_button(self):
        #driver.find_element(*login_object["btn_login"]).click()
        self.sel_wrapper.click_element(login_object["btn_login"])
        self.driver.implicitly_wait(40)

    def click_verify_button(self):

        #driver.find_element(*login_object["btn_verify"]).click()
        self.sel_wrapper.click_element(login_object["btn_verify"])

# lp=LoginPage(driver)
# lp.enter_email()
# lp.enter_password()
# lp.click_login_button()
# lp.click_verify_button()