from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()  #to launch the browser without instantly closing
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)


driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
# driver.get_screenshot_as_file("reg_page.png")
# sleep(2)

driver.save_screenshot("image.png")
sleep(2)