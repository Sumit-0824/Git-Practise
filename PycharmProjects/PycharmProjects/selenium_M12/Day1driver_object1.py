# # to launch the chrome browser
# #creating session
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.google.com/")
#Commenting - select the line and ctrl+ forward slash
################################################################
#if session is closing automaticlly

# from selenium import webdriver
# #it will not close the browser
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True) #no need to provide the keyword and value externally
# driver=webdriver.Chrome(options=opts)
# # driver.get("https://www.google.com/")
# # driver.get("https://www.youtube.com/")
# driver.get("https://demowebshop.tricentis.com/")
# driver.implicitly_wait(20)

# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# time.sleep(5)
#
# search=driver.find_element("id","twotabsearchtextbox").send_keys(Bicycle)
# print(search)

