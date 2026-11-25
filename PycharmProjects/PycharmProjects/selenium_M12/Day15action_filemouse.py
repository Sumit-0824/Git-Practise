from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

driver.get("https://www.myntra.com/")
driver.maximize_window()

#mouse actions
action_obj=ActionChains(driver)

#Hover over men
men_category=driver.find_element("xpath",'(//a[text()="Men"])[1]')
sleep(2)
action_obj.move_to_element(men_category).perform()
sleep(2)

#Hover over kid
kid_category=driver.find_element("xpath",'(//a[text()="Kids"])[1]')
sleep(2)
action_obj.move_to_element(kid_category).perform()
sleep(2)
#####################ASSIGNMENT##################
#flipkart.com and locate the element
###################################################