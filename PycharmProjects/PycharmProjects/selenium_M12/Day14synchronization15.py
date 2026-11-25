"""
process of matching the application speed with selenium web driver
2 types
1. unconditional sync : makes interpreter to wait for "n" seconds

2. conditional sync : makes the web driver to wait until some condition is met
    2 types
    1. implicit wait()
    2. explicit wait()
"""

from time import sleep
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

path=r"C:\Users\Sumit\PycharmProjects\selenium_M12\HTML_files\progress.html"

driver.get(path)
driver.maximize_window()
#############Implicit wait##################:ElementNotInteractableException
# driver.find_element("xpath",'//button[text()="Click Me"]').click()
# sleep(2)
# driver.implicitly_wait(30)
# driver.find_element("xpath",'//div[text()="100%"]')
# sleep(2)
# driver.find_element("xpath",'//button[text()="Click Me"]').click()
################################Explicit wait####################################

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

w=WebDriverWait(driver,30)  #2 parameter(driver,timeout)

driver.find_element("xpath",'//button[text()="Click Me"]').click()
sleep(2)

locator=("xpath",'//div[text()="100%"]')
element=w.until(EC.presence_of_element_located(locator))
sleep(2)
driver.find_element("xpath",'//button[text()="Click Me"]').click()
sleep(2)

