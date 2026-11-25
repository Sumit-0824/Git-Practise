import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Serv_obj = Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"(//button[normalize-space()='Click for JS Prompt'])[1]").click()
time.sleep(5)
alertwindows=driver.switch_to.alert
print(alertwindows.text)
alertwindows.send_keys("welcome")
alertwindows.accept()# close alert window by using Ok button
#alertwindows.dismiss()#close alert windows by using cancel

