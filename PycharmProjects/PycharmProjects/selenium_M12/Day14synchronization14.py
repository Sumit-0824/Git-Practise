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

path=r"C:\Users\Sumit\PycharmProjects\selenium_M12\HTML_files\loading.html"

driver.get(path)
driver.maximize_window()
#############Implicit wait##################:ElementNotInteractableException
# driver.implicitly_wait(20)
# driver.find_element("name","fname").send_keys("Sumit")
# sleep(2)
# driver.find_element("xpath",'//input[@name="lname"]').send_keys("Sinha")
# sleep(2)
# driver.find_element("xpath",'//input[@value="Login"]').click()
#############Explicit wait/webdriver wait ##################:TimeOutExceptions########
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
w=WebDriverWait(driver,20)  #2 parameter(driver,timeout)
locator=("name","fname")
element=w.until(EC.visibility_of_element_located(locator))
element.send_keys("Sumit")





