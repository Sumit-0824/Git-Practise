from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()  #to launch the browser without instantly closing
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)


driver.get("https://www.myntra.com/")
driver.maximize_window()

# #Scroll to bottom of page
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# sleep(2)
#
# #scroll to particular element
# element=driver.find_element("xpath",'//a[text()=" ONLINE SHOPPING "]')
# driver.execute_script("arguments[0].scrollIntoView();",element)
# sleep(2)
#Scroll 500px downward
driver.execute_script("window.scrollBy(0,500)","")
sleep(2)
#Scroll 500px upward
driver.execute_script("window.scrollBy(0,-500)","")
sleep(2)
#Code for scrolling left and right
# #Scroll 200px right
# driver.execute_script("window.scrollBy(200,0)","")
# sleep(2)
# #Scroll 200px left
# driver.execute_script("window.scrollBy(-200,0)","")
# sleep(2)