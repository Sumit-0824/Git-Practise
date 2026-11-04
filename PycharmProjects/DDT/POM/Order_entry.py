# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import pytest
# import time
#
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.wait import WebDriverWait
# driver = webdriver.Chrome()
#
#
# def test_loanentry():
#  global driver
#  driver.implicitly_wait(1000)
#  #select the mandatory fields for the single loan entry
#  customer = driver.find_element("name", "Customer")
#  select = Select(customer)
#  select.select_by_visible_text('CL094 / MortgageConnect1')
#  time.sleep(6)
#  driver.find_element("id", "LoanNumber").send_keys("Test0083Alima")
#  #upload the loan documents
#  driver.find_element("id", "DocumentUploadNew").send_keys("C:\\Users\\AT2158\\OneDrive - Avanze Technologies India Pvt Ltd\\Desktop\\SeleniumFiles\\loancd.pdf")
#  time.sleep(10)
#  SaveandOrder= driver.find_element("id", "saveandexit ").click()
#  time.sleep(10)
#  assert True

 from selenium.webdriver.common.by import By
 from selenium.webdriver.support.ui import WebDriverWait
 from selenium.webdriver.support import expected_conditions as EC

 class OrderEntryPage:

     def __init__(self, driver):
         self.driver = driver
         self.wait = WebDriverWait(driver, 20)

     # Locators
     CHANNEL = (By.XPATH, "//label[contains(text(),'Channel')]/following::input[1]")

     PRODUCT = (By.XPATH, "//label[contains(text(),'Product')]/following::input[1]")

     PROJECT = (By.XPATH, "//label[contains(text(),'Project')]/following::input[1]")

     ORDER_NUMBER = (By.XPATH, "//label[contains(text(),'Order Number')]/following::input[1]")

     ORDER_TYPE = (By.XPATH, "//label[contains(text(),'Order Type')]/following::input[1]")

     ADDRESS1 = (By.XPATH, "//input[@placeholder='1234 Main St']")

     ADDRESS2 = (By.XPATH, "//input[contains(@placeholder,'Apartment')]")

     ZIP = (By.XPATH, "//label[text()='Zip']/following::input[1]")

     CITY = (By.XPATH, "//label[text()='City']/following::input[1]")

     COUNTY = (By.XPATH, "//label[text()='County']/following::input[1]")

     STATE = (By.XPATH, "//label[text()='State']/following::input[1]")

     UPLOAD = (By.XPATH, "//input[@type='file']")

     SAVE_CONTINUE = (By.XPATH, "//button[contains(text(),'Save & Continue')]")

     SAVE_NEW = (By.XPATH, "//button[contains(text(),'Save & New Order')]")

     # Generic Dropdown Selection
     def select_dropdown(self, locator, value):
         self.wait.until(
             EC.element_to_be_clickable(locator)
         ).click()

         option = (
             By.XPATH,
             f"//li[normalize-space()='{value}'] | //span[normalize-space()='{value}']"
         )

         self.wait.until(
             EC.element_to_be_clickable(option)
         ).click()

     def enter_text(self, locator, value):
         element = self.wait.until(
             EC.visibility_of_element_located(locator)
         )

         element.clear()
         element.send_keys(value)

     def upload_document(self, filepath):
         self.driver.find_element(*self.UPLOAD).send_keys(filepath)

     def click_save_continue(self):
         self.driver.find_element(*self.SAVE_CONTINUE).click()

     def click_save_new(self):
         self.driver.find_element(*self.SAVE_NEW).click()