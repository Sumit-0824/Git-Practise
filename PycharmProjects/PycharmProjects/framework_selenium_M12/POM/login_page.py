"""
POM- Page object Model,design pattern to write business logic
design pattern in selenium that creates an object repositories for storing all web element

"""
from data import reading_objects       #1st we need to import after launching browser to get the data- after line 12
# from selenium import webdriver   #to launch browser
# opts=webdriver.ChromeOptions()   #to not close the broswer immediately
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=opts)
# driver.get("https://demowebshop.tricentis.com/login")
# driver.maximize_window()

# login_object=reading_objects.reading_locators()          #Accessing the data    #dictionary      filename.functionname()
#
# class LoginPage:                         #creating class Syntax   class ClassName
#
#     def enter_email(self):                #1st argument is self
#          driver.find_element(*login_object["txt_email"]).send_keys("Sumitsinha@gmail.com")
# #InvalidArgumentException--- if we donot unpack the data..unpack----*
#     #login_object["txt_email"]------accessing the locator available in excel using type_loc column
#     def enter_password(self):
#          driver.find_element(*login_object["txt_pwd"]).send_keys("Demo@123")
#
#     def click_login(self):
#          driver.find_element(*login_object["btn_login"]).click()
# #To call class 1st we need to create object of class
# lp=LoginPage()
# #To call methods inside the class    Syntax-----  obj.methodname
# lp.enter_email()
# lp.enter_password()
# lp.click_login()

#Day 3 after creating generic package
###################################################################################################################
from data import reading_objects       #1st we need to import after launching browser to get the data- after line 12
from Library.sel_wrapper import SeleniumWrapper   #done in day 3
#comment launching browser and webpage once we create conftest file
# from selenium import webdriver   #to launch browser
# opts=webdriver.ChromeOptions()   #to not close the broswer immediately
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=opts)
# driver.get("https://demowebshop.tricentis.com/login")
# driver.maximize_window()

login_object=reading_objects.reading_locators()          #Accessing the data    #dictionary      filename.functionname()

class LoginPage:                         #creating class Syntax   class ClassName

    def __init__(self,driver):
        self.driver=driver
        self.sel_wrapper=SeleniumWrapper(driver)
    def enter_email(self):                #1st argument is self
        # driver.find_element(*login_object["txt_email"]).send_keys("Sumitsinha@gmail.com")
        self.sel_wrapper.enter_txt(login_object["txt_email"],"Sumitsinha@gmail.com")
#InvalidArgumentException--- if we donot unpack the data..unpack----*
    #login_object["txt_email"]------accessing the locator available in excel using type_loc column
    def enter_password(self):
        # driver.find_element(*login_object["txt_pwd"]).send_keys("Demo@123")
        self.sel_wrapper.enter_txt(login_object["txt_pwd"], "Demo@123")

    def click_login(self):
        # driver.find_element(*login_object["btn_login"]).click()
        self.sel_wrapper.click_element(login_object["btn_login"])
# #To call class 1st we need to create object of class
# lp=LoginPage(driver)
# #To call methods inside the class    Syntax-----  obj.methodname
# lp.enter_email()
# lp.enter_password()
# lp.click_login()