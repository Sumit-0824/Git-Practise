from time import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(20)
print(driver.name)
print(driver.current_url)
print(driver.title)
search_box=driver.find_element("id","small-searchterms")
print(search_box)
search_box.send_keys("Computer")
button=driver.find_element("class name","button-1.search-box-button")
button.click()

#Xpath-
'''xpath using 1. attribute-//tagname[@attr_value,"attr_value"
Xpath using text()-//tagname[text()="value"]
Xpath using contains-attribute-'//tagname[contains(@attr_value,attr_value)]'
Xpath using contains-text()-'//tagname[contains(text(),"value")]'
'''