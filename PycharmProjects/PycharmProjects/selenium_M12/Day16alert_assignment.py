from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()  #to launch the browser without instantly closing
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)


driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()


driver.find_element("xpath",'(//input[@type="text"])[1]').send_keys()
driver.find_element("xpath",'//input[@type="submit"]').click()
sleep(2)
alert_obj=driver.switch_to.alert
alert_obj.accept()
sleep(2)