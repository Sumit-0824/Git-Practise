from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Serv_obj = Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
#drpcountry_ele=driver.find_element(By.XPATH,"//Select[@id='input-country']")
drpcountry=Select(driver.find_element(By.ID,"input-country")) # because of security unable to get inside the url

#select options from the dropdown
drpcountry.select_by_visible_text("India")
#drpcountry.select_by_value("12")
#drpcountry.select_by_index(13)

#capture all the options and print them
alloptions = drpcountry.options
print("total no of options:" len(alloptions))
#print the all the options available
for opt in alloptions:
    print(opt.text)
#Select option from the dropdown without using buit in methods
for opt in alloptions:
    if opt.text=='India':
        opt.click()
        break
        

