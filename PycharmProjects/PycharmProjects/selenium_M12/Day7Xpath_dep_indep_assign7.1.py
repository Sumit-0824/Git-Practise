from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
driver.find_element("xpath",'//a[text()="Python 3.12.9"]/../..//a[text()="Release Notes"]').click()
sleep(2)