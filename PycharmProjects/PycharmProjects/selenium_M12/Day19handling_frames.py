from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()  #to launch the browser without instantly closing
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

path=r"C:\Users\Sumit\PycharmProjects\selenium_M12\HTML_files\iframe.html"
driver.get(path)
driver.maximize_window()

frame1=driver.find_element("id","FR1")     # search for iframe tag
driver.switch_to.frame(frame1)

driver.find_element('id',"small-searchterms").send_keys("Hello Sumit")
sleep(2)
driver.switch_to.parent_frame()

frame2=driver.find_element("name","frame2")
driver.switch_to.frame(frame2)

driver.find_element("xpath",'//input[@type="text"]').send_keys("Welcome to Python-Selenium")
sleep(2)