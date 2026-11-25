#auto complete list boxes
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(5)
element=driver.find_element("xpath",'//input[@placeholder="Search for products, brands and more"]')
element.send_keys("Puma shoes")
sleep(2)
driver.find_element("xpath",'//li[text()="Puma Shoes White"]').click()
sleep(2)