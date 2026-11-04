# from selenium  import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.stacxuat.com/Login/index_new")
# driver.maximize_window()

class selenium_wrapper:
    def __init__(self, driver):
        self.driver = driver
    def enter_txt(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)
    def click_element(self,locator):
        self.driver.find_element(*locator).click()
