#Xpath--XMl
'''
xpath : xml path
syntax or language for finding any element on the web page
used to find the location of any element
xpath allows to navigate through the ewb page
xpath helps selenium to find the elements that are not found by any other locator id, name, class name

'''

#Types of Xpath
#1.Absolute Xpath
#2.Relative Xpath

#Absolute Xpath- / == meaning immediate child
#absolute xpath we need to consider from root-/body/div/div1
#Relative Xpath- element can be searched anywhere in the webpage
#syntax
# 1. using attributes
# driver.find_element("xpath", '//tagname[@attr_name="attr_value"]')
# 2. using text()
# driver.find_element("xpath", '//tagname[text()="value"]')
# 3. using contains()
# 1.attributes = driver.find_element("xpath", '//tagname[contains(@attr_name, attr_value)]')
# 2.text() = driver.find_element("xpath", '//tagname[contains(text(), "value")]')
#Replace // with single slash for absolute xpath
# if attrubute then use class as attribute name instead of classname
#copy the text even it followed by spaces or line---later we can trim as required
#

from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
url="https://demowebshop.tricentis.com/"
driver.get(url)
driver.maximize_window()

# 1. using attributes
# driver.find_element("xpath", '//tagname[@attr_name="attr_value"]')
#Register
# reg_link=driver.find_element("xpath",'//a[@class="ico-register"]')
# reg_link.click()
# sleep(2)
#login
# driver.find_element("xpath",'//a[@class="ico-login"]').click()
# sleep(2)

# 2. using text()
# driver.find_element("xpath", '//tagname[text()="value"]')
# reg_link=driver.find_element("xpath",'//a[text()="Register"]')
# reg_link.click()
# sleep(2)
#login
# driver.find_element("xpath",'//a[text()="Log in"]').click()
# sleep(2)

# 3. using contains()
# 1.attributes = driver.find_element("xpath", '//tagname[contains(@attr_name, attr_value)]')
# driver.find_element("xpath",'//a[contains(@class,"ico-register")]').click()
# sleep(2)
#Group indexing starts from 1
# 2.text() = driver.find_element("xpath", '//tagname[contains(text(), "value")]')
# driver.find_element("xpath",'(//a[contains(text(),"Books")])[3]').click()
# sleep(2)

#Ex 2 for gender
#driver.find_element("xpath", '//tagname[text()="value"]')
reg_link=driver.find_element("xpath",'//a[text()="Register"]')
reg_link.click()
sleep(2)

# driver.find_element("xpath",'(//input[contains(@name,"Gender")])[1]').click()  #for male
# sleep(2)

driver.find_element("xpath",'(//input[contains(@name,"Gender")])[2]').click()  #for female
sleep(2)