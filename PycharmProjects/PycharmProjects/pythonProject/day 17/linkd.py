import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Serv_obj = Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#click on link_Text
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
#click on link_Text
driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

#Find total number of links in a page
#links=driver.find_elements(By.TAG_NAME,'a')
links=driver.find_elements(By.XPATH,'//a')
print("total number of links:",len(links))
#print all the links
for link in links:
    print(link.text)
time.sleep(5)
driver.quit()

