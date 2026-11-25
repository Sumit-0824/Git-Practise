from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
url="https://demowebshop.tricentis.com/"
driver.get(url)
driver.maximize_window()
#Register
reg_link=driver.find_element("xpath",'//a[@class="ico-register"]')
reg_link.click()
sleep(2)
#Gender
driver.find_element("xpath",'(//input[contains(@name,"Gender")])[1]').click()  #for male
sleep(2)
#First name
first_name=driver.find_element("xpath",'//input[@name,"FirstName"]')
first_name.send_keys("Sumit")
#Last name
last_name=driver.find_element("xpath",'//input[@name,"LastName"]')
last_name.send_keys("Sinha")

user_email=driver.find_element("xpath",'//input[@name="Email"]')
user_email.send_keys("sinhasumit01@gmail.com")
sleep(1)
#Password
driver.find_element("xpath",'//input[@name="Password"]').send_keys("Sumit@123")
#confirm password  ConfirmPassword
driver.find_element("xpath",'//input[@name="ConfirmPassword"]').send_keys("Sumit@123")
sleep(2)
#Register  //input[@value="Register"]
driver.find_element("xpath",'//input[@value="Register"]').click()
sleep(2)