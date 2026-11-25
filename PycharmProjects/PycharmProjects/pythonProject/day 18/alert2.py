import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Serv_obj = Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)
driver.close()