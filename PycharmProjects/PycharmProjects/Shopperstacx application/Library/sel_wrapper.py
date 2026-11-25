import time

# from selenium import webdriver   #to launch browser
# opts=webdriver.ChromeOptions()   #to not close the broswer immediately
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=opts)
# driver.get("https://shoppersstack.com/user-signin")
# driver.maximize_window()
# time.sleep(10)

class SeleniumWrapper:
    def __init__(self,driver):
        self.driver=driver

    def enter_txt(self,locater,value):
        self.driver.find_element(*locater).send_keys(value)

    def click_element(self,locater):
        self.driver.find_element(*locater).click()
