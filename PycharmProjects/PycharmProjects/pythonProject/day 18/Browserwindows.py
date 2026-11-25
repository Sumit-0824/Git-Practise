import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Serv_obj = Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
#windowid=driver.current_window_handle
#print(windowid)  #169304924EF675235EC9A0270A3647F9 #D3BBE174866E43BCBE359E5712E6A58F
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/p[2]/a[1]").click()
windowIDS=driver.window_handles
parentwindowid=windowIDS[0]
childwindowid=windowIDS[1]
print(parentwindowid,childwindowid)
#Approach1
# driver.switch_to.window(childwindowid)
# print("title of the childwindow",driver.title) #OrangeHRM
#
# driver.switch_to.window(childwindowid)
# print("title of the Parentwindow",driver.title) #OrangeHRM

#Aprroach 2(Chose specific browser windows)
for winid in windowsiDS:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM":
        driver.close()
