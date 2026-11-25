from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element("xpath",'//a[text()="Create new account"]').click()
sleep(2)

day_list=driver.find_element("id","day")
select_day=Select(day_list)
select_day.select_by_value("5")
sleep(2)
select_day.select_by_visible_text("7")
sleep(2)
select_day.select_by_index(10)
sleep(2)
'''
Options.ismultiple- for selecting multiple dropdown- Returns True/None
'''