from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.monsterindia.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@class='uprse semi-bold']").click()
driver.find_element(By.XPATH,"//span[@id='file-upload']").send_keys("C:\SeleniumPractise\sample.pdf")