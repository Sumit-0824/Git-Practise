import time

# from data import reading_objects       #1st we need to import after launching browser to get the data- after line 12
# from selenium import webdriver   #to launch browser
# opts=webdriver.ChromeOptions()   #to not close the broswer immediately
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=opts)
# driver.get("https://shoppersstack.com/user-signin")
# driver.maximize_window()
# time.sleep(10)
# login_object=reading_objects.reading_locators()          #Accessing the data    #dictionary      filename.functionname()
# #
# class LoginPage:                         #creating class Syntax   class ClassName
#
#     def enter_email(self):                #1st argument is self
#          driver.find_element(*login_object["txt_email"]).send_keys("sumitkumarsinha1992@gmail.com")
#     def enter_password(self):
#          driver.find_element(*login_object["txt_pwd"]).send_keys("Testing@123")
#     def click_login(self):
#          driver.find_element(*login_object["btn_login"]).click()
# # #To call class 1st we need to create object of class
# lp=LoginPage()
# # #To call methods inside the class    Syntax-----  obj.methodname
# lp.enter_email()
# lp.enter_password()
# lp.click_login()
######################################################################################
from data import reading_objects       #1st we need to import after launching browser to get the data- after line 12
from Library.sel_wrapper import SeleniumWrapper
# from selenium import webdriver   #to launch browser
# opts=webdriver.ChromeOptions()   #to not close the broswer immediately
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=opts)
# driver.get("https://shoppersstack.com/user-signin")
# driver.maximize_window()
# time.sleep(10)
login_object=reading_objects.reading_locators()          #Accessing the data    #dictionary      filename.functionname()

class LoginPage:                         #creating class Syntax   class ClassName

    def __init__(self,driver):
        self.driver=driver
        self.sel_wrapper=SeleniumWrapper(driver)
    def enter_email(self):                #1st argument is self
        # driver.find_element(*login_object["txt_email"]).send_keys("Sumitsinha@gmail.com")
        self.sel_wrapper.enter_txt(login_object["txt_email"],"sumitkumarsinha1992@gmail.com")

    def enter_password(self):
        # driver.find_element(*login_object["txt_pwd"]).send_keys("Demo@123")
        self.sel_wrapper.enter_txt(login_object["txt_pwd"], "Testing@123")

    def click_login(self):
        # driver.find_element(*login_object["btn_login"]).click()
        self.sel_wrapper.click_element(login_object["btn_login"])

    def click_men(self):
        time.sleep(10)
        self.sel_wrapper.click_element(login_object["btn_men"])

    def click_add_cart(self):
        time.sleep(10)
        self.sel_wrapper.click_element(login_object["btn_add_cart"])
# #To call class 1st we need to create object of class
#lp=LoginPage(driver)
# # #To call methods inside the class    Syntax-----  obj.methodname
# lp.enter_email()
# lp.enter_password()
# lp.click_login()
#lp.click_men()