from time import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(20)
print(driver.name)
print(driver.current_url)
print(driver.title)
search_box=driver.find_element("id","twotabsearchtextbox")
print(search_box)