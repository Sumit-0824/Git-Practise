import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Serv_obj = Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
driver.implicitly_wait(10)
#driver.get("https://the-internet.herokuapp.com/basic-auth")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic-auth")
driver.maximize_window()