from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
# path=r"C:\Users\Sumit\PycharmProjects\selenium_M12\HTML_files\actions.html"
# driver.get(path)
# driver.maximize_window()
#
# #mouse actions
# action_obj=ActionChains(driver)
# text_field1=driver.find_element("id","clickField")
# text_field2=driver.find_element("id","doubleClickField")
#
# #####Single click
# text_field1.click()
# sleep(2)
# #####double click
# action_obj.double_click(text_field2).perform()
# sleep(2)
# action_obj.context_click(text_field2).perform()
# sleep(2)

driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
driver.maximize_window()
#Drag and drop
source=driver.find_element("id","draggable")
target=driver.find_element("id","droppable")

action_obj=ActionChains(driver)
action_obj.drag_and_drop(source,target).perform()
sleep(2)