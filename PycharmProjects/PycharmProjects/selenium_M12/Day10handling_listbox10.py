"handling list boxes/select class/ dropdown"

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

path=r"C:\Users\Sumit\PycharmProjects\selenium_M12\HTML_files\demo.html"
driver.get(path)
driver.maximize_window()

#
list_box=driver.find_element("id","standard_cars")
select_obj=Select(list_box)   # creating obj for select
'''
to select option tag using
1. using text(select_by_visible_text)
2. using value(select_by_value)
3. using index--starts from 0 
Note: in all except group indexing(1) the count starts from 0
'''
#selecting an option using text
select_obj.select_by_visible_text("BMW")   #always in ""
sleep(2)
select_obj.select_by_visible_text("Honda")
#selecting an option using value
select_obj.select_by_value("jgr")
select_obj.select_by_value("merc")
#selecting an option using index
car_obj=select_obj.select_by_index(9)   #no "" required
print(car_obj.text)



