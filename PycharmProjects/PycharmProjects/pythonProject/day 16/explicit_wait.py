import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

Serv_obj = Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
WebDriverWait(driver,10)                #explicit wait declaration
driver.get("https://www.google.com/")
driver.maximize_window()
searchbox=driver.find_element(By.NAME,'q')
searchbox.send_keys("Selenium")
searchbox.submit()
mywait.until(EC.(By.XPATH,"//h3[text()='Selenium']").click()

