#We need to install requests package through File--->Settings-->project Interpreter--Add-->requests and install it
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Serv_obj = Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
alllinks =driver.find_elements(By.TAG_NAME,'a')
count=0

for link in alllinks:
    url=link.get_attribute('href')
    try:
     res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url,"is broken link")
        count+=1
    else:
        print(url,"is valid link")
print("Total number of broken links",count)
