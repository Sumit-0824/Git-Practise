from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()  #to launch the browser without instantly closing
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)


driver.get("https://www.redbus.in/")
driver.maximize_window()

driver.find_element("xpath",'//span[text()="Account"]').click()
driver.find_element("xpath",'//span[text()="Login/ Sign Up"]').click()

element=driver.find_element("xpath",'//iframe[@class="modalIframe"]')
driver.switch_to.frame(element)

#driver.find_element("xpath",'//input[@type="number"]').send_keys("123456789")
driver.find_element("class name","IP").send_keys("123456789")