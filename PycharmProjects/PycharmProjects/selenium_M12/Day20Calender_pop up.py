from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(20)
#click on departure
driver.find_element("xpath",'//span[text()="Departure"]').click()
sleep(2)
for year in range(1,13):
    month=driver.find_element("xpath",'(//div[@class="DayPicker-Caption"])[1]')    #choosing the month for parent tag
    if month.text=="April 2025":
        driver.find_element("xpath",'//span[@aria-label="Next Month"]').click()
    else:
        driver.find_element("xpath",'//p[text()="1"]').click()
        break
