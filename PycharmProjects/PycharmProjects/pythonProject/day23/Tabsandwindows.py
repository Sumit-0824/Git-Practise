from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
regilink =Keys.CONTROL+Keys.RETURN
driver.find_element(By.LINK_TEXT,"Register").send_keys(regilink)

#New Tab-Selenium 4:opens a new tabs & Switches to new tab

driver.get("https://www.opencart.com/")
driver.switch_to.new_window('tab')
driver.get("https://www.orangehrm.com/")

