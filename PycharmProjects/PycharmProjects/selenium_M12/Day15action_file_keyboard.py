#keyboard action/simulation
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys   #Keyboard action
from selenium.webdriver.common.action_chains import ActionChains

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

driver.get("https://www.myntra.com/")
driver.maximize_window()

action_obj=ActionChains(driver)

#selecting everything- ctrl+A
# action_obj.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()
# sleep(2)

#Scrolling action
#1 page down
# action_obj.send_keys(Keys.PAGE_DOWN).perform()
# sleep(2)
# #1 page up
# action_obj.send_keys(Keys.PAGE_UP).perform()
# sleep(2)
#Arrow Down
action_obj.send_keys(Keys.ARROW_DOWN).perform()
sleep(2)
#Arrow up
action_obj.send_keys(Keys.ARROW_UP).perform()
sleep(2)
#Scrolling to end
action_obj.send_keys(Keys.END).perform()
sleep(2)
#Scroll to top
action_obj.send_keys(Keys.PAGE_UP).perform()
sleep(2)
search_bar = driver.find_element("xpath", '//input[@placeholder="Search for products, brands and more"]')
search_bar.send_keys("Puma")
sleep(2)

action_obj.send_keys(Keys.ENTER).perform()
sleep(2)
