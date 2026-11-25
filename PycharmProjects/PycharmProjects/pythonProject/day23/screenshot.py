from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import os
serv_obj =Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.save_screenshot("C:\\Users\\Sumit\\PycharmProjects\\pythonProject\\day23\\homepage.png")
#driver.save_screenshot(os.getcwd()+"\\homepage.png")
#driver.save_screenshot_as_file(os.getcwd() +"\\homepage.png)
driver.quit()