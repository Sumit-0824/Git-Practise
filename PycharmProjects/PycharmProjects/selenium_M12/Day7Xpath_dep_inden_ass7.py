from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

path=r"C:\Users\Sumit\PycharmProjects\selenium_M12\HTML_files\demo.html"
driver.get(path)
driver.maximize_window()

driver.find_element("xpath",'//td[text()="Yahoo"]/..//a[@target="_blank"]').click()
sleep(2)

# driver.find_element("xpath",'//td[text()="Linux"]/..//a[text()="Download"]').click()
# sleep(2)
