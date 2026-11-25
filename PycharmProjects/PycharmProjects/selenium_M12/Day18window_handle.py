from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()  #to launch the browser without instantly closing
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)


driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

driver.find_element("xpath",'//a[text()="Facebook"]').click()
sleep(2)
handles=driver.window_handles            #window_handles  is a property
print(handles)

driver.switch_to.window(handles[1])      #window() is a method
driver.find_element("xpath",'(//input[@name="email"])[2]').send_keys("abc@gmail.com")
sleep(2)

driver.switch_to.window(handles[0])
driver.find_element("xpath",'//a[text()="Register"]').click()
sleep(2)

driver.quit()