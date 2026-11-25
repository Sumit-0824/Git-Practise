"""
css : cascading style sheet : used to give the styles for the web page
parent child relationship
for direct relationship  >
for indirect relationship  space
"""

from time import sleep

from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

path=r"C:\Users\Sumit\PycharmProjects\selenium_M12\HTML_files\css_selectors.html"
#copy absolute path and use formatted string to avoid error for special character
#it will not consider the special character as special character
driver.get(path)
driver.maximize_window()

#css_selector
#td and input
'''
for direct relationship we use >
for indirect relationship we use space
Example 1
Parent
 child
   grandchild
parent>child- direct relationship
parent Grand child- indirect relationship
child>grandchild- direct relationship
Ex2
Parent
 child 1
  child 2
parent>child 1- direct relationship
parent child 2- indirect relationship
child 1>child 2- direct relationship
'''
#Syntax
#driver.find_element("css selector",'tagname[attribute name="attribute value"]')

#td and input-- direct
username=driver.find_element("css selector",'td>input[type="text"]')
username.send_keys("sumit")
sleep(2)

#tr and input-- indirect
password=driver.find_element("css selector",'tr input[type="password"]')
password.send_keys("Sumit@123")
sleep(2)


"""
drawbacks of css selector
1. if the attributes are not present, then it is difficult to write the css selector expression
2. no elements can be located using text in css selector 
"""
