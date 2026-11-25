from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()  #to launch the browser without instantly closing
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()

#InvalidArgumentException-- if wrong locator
#Simple Alert
# driver.find_element("xpath",'//button[text()="Simple Alert"]').click()
# sleep(2)
#
# alert_obj=driver.switch_to.alert
# alert_obj.accept()
# sleep(2)

#Confirm alert
# driver.find_element("xpath",'//button[text()="Confirmation Alert"]').click()
# sleep(2)
# alert_obj=driver.switch_to.alert
# # alert_obj.accept()
# # sleep(2)
# alert_obj.dismiss()
# sleep(2)

#Promt alert Prompt Alert

# driver.find_element("xpath",'//button[text()="Prompt Alert"]').click()
# sleep(2)
# alert_obj=driver.switch_to.alert
# alert_obj.send_keys("Sumit")
# sleep(2)
# # alert_obj.accept()
# # sleep(2)
# alert_obj.dismiss()      #User cancelled the prompt.
# sleep(2)

###########################file to upload
path=r"C:\Users\Sumit\PycharmProjects\selenium_M12\HTML_files\demo.html"
driver.get(path)
driver.maximize_window()

resume_path=r"C:\Users\Sumit\Downloads\dict.pdf"
driver.find_element("xpath",'//input[@type="file"]').send_keys(resume_path)
sleep(2)

