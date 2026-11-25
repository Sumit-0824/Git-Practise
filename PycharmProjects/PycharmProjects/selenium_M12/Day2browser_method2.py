

from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
url="https://demowebshop.tricentis.com/"
driver.get(url)

#interacting with browser methods
driver.maximize_window()
sleep(2)
# driver.minimize_window()
# sleep(2)
# driver.fullscreen_window()
# sleep(2)

#############################################################
# navigating in the browser
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# refreshing the webpage
# driver.refresh()

#############################################
#position ans size of window

#print(driver.get_window_position())           #{'x': -8, 'y': -8}
#print(driver.get_window_size())                #{'width': 1552, 'height': 832}
#print(driver.get_window_rect())                #{'height': 832, 'width': 1552, 'x': -8, 'y': -8}

#################################################
#modifying/altering the size of window
#driver.set_window_position(100,200)
#driver.set_window_size(200,50)
#driver.set_window_rect(100,50,300,100)

######################################################
#Properties of the browser
print(driver.name)                #chrome
print(driver.current_url)         #https://demowebshop.tricentis.com/
print(driver.title)               #Demo Web Shop

#####################################################
#closing the browser

#driver.close()  #closes the current tab
driver.quit()    #closes the entire session

