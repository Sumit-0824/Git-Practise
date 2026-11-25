import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.opencart.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@class='btn btn-black navbar-btn']")
driver.find_element(By.NAME,"Username").send_keys("SumitYuvi")
driver.find_element(By.ID,"input-firstname").send_keys("SumitKumar")
driver.find_element(By.XPATH,"//input[@id='input-lastname']").send_keys("Sinha")
driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("sumitkumarsinha1992@gmail.com")
drpcountry=Select(driver.find_element(By.ID,"input-country"))
drpcountry.select_by_visible_text("India")
driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("sumit@123")
time.sleep(10)