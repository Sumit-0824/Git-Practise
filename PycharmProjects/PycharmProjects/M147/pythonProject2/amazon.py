from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_expermental options("detach",True)
driver=webdriver.chrome(options=opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(5)

search=driver.find_element("id","twotabsearchtextbox").send_keys(Bicycle)
print(search)