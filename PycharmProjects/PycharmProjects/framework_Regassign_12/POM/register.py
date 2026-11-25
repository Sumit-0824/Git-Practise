from time import sleep

from data import reading_register      #1st we need to import after launching browser to get the data- after line 12
from Library.sel_wrapper import SeleniumWrapper
# from selenium import webdriver   #to launch browser
# opts=webdriver.ChromeOptions()   #to not close the broswer immediately
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=opts)
# driver.get("https://demowebshop.tricentis.com/register")
# driver.maximize_window()
sleep(2)

register_object=reading_register.reading_locators()


class RegisterPage:  # creating class Syntax   class ClassName

    def __init__(self, driver):
        self.driver = driver
        self.sel_wrapper = SeleniumWrapper(driver)

    # def enter_radio(self):
    #     driver.find_element(*register_object["btn_radio"]).click()
    def enter_fname(self):
        #driver.find_element(*register_object["txt_fname"]).send_keys("Sumit")
        self.sel_wrapper.enter_txt(register_object["txt_fname"], "Sumit")
    def enter_lname(self):
        #driver.find_element(*register_object["txt_lname"]).send_keys("Sinha")
        self.sel_wrapper.enter_txt(register_object["txt_lname"], "Sinha")
    def enter_email(self):  # 1st argument is self
        #driver.find_element(*register_object["txt_email"]).send_keys("Sumitsinha02@gmail.com")
        self.sel_wrapper.enter_txt(register_object["txt_email"], "Sumitsinha02@gmail.com")
    # InvalidArgumentException--- if we donot unpack the data..unpack----*
    # login_object["txt_email"]------accessing the locator available in excel using loc_type column
    def enter_password(self):
        #driver.find_element(*register_object["txt_pwd"]).send_keys("Demo@123")
        self.sel_wrapper.enter_txt(register_object["txt_pwd"], "Demo@123")
    def enter_cpassword(self):
        #driver.find_element(*register_object["txt_cpwd"]).send_keys("Demo@123")
        self.sel_wrapper.enter_txt(register_object["txt_cpwd"], "Demo@123")
    def click_register(self):
        #driver.find_element(*register_object["btn_register"]).click()
        self.sel_wrapper.click_element(register_object["btn_register"])
#To call class 1st we need to create object of class
# lp=RegisterPage(driver)
# #To call methods inside the class    Syntax-----  obj.methodname
# # lp.enter_radio()
# lp.enter_fname()
# lp.enter_lname()
# lp.enter_email()
# lp.enter_password()
# lp.enter_cpassword()
# lp.click_register()

