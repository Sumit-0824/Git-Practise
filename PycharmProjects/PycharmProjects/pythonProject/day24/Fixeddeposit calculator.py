import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from day24 import XLUtils


serv_obj =Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver =webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/")
driver.maximize_window()

Contunue''
