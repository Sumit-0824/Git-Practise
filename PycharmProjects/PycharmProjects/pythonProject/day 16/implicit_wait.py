import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Serv_obj = Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.maximize_window()
searchbox=driver.find_element(By.NAME,'q')
searchbox.send_keys("Selenium")
searchbox.submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

