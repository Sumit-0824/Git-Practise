#Testcase
#Open web browser(Chrome/firefox/IE)
#open URL https://demo.nopcommerce.com/login
#Provide Email
#Provide Password
#Click on login
#capture title of the dashboard page(Actual title)
#Verify title of the page
#close Browser
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/login")
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(5)
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.close()
