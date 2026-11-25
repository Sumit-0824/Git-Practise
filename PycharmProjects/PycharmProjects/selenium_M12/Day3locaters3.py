
from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
# locating element using id locater
# search_bar=driver.find_element("id","small-searchterms")
# print(search_bar)
# locating element using name locater
search_bar=driver.find_element("name","q")
print(search_bar)

search_bar.send_keys("computer")
sleep(2)
# search_bar.clear()
# sleep(2)
# locating search button element using class name locater
# #button=driver.find_element("class name","button-1 search-box-button")  #only for classname replace the space with.
# button=driver.find_element("class name","button-1.search-box-button")  #class in html
# button.click()
# sleep(2)

##link text and partial link text - we can use only if html tag starts with <a href##
# locating search button element using link text locater
# reg_link=driver.find_element("link text","Register")
# reg_link.click()

# locating search button element using partial link text locater
login_link=driver.find_element("partial link text","Log")
login_link.click()
#sleep(2)