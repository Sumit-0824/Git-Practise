import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Serv_obj = Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://practice.expandtesting.com/checkboxes")
driver.maximize_window()
checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')

# Loop through checkboxes and uncheck them if they are checked
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

if checkboxes:
    checkboxes[0].click()

time.sleep(5)
driver.quit()