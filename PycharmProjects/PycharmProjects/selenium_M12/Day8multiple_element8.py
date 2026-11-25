from time import sleep
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

################################################
# selecting all the checkboxes in demo.html

path = r"C:\Users\Sumit\PycharmProjects\selenium_M12\HTML_files\demo.html"
driver.get(path)
driver.maximize_window()
checkboxes = driver.find_elements("xpath", '//input[@name="download"]')
for check in checkboxes:
    check.click()
    sleep(1)

################################
# count the number of input tags in demo.html

# input_tags = driver.find_elements("tag name", 'input')
# print(input_tags)
# #[<selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.3")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.4")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.5")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.6")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.7")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.8")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.9")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.10")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.11")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.12")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.13")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.14")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.15")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.16")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.17")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.18")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.19")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.20")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.21")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.22")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.42")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.23")>, <selenium.webdriver.remote.webelement.WebElement (session="a44f9690e1dd1d81a37fe5f4552483fc", element="f.8CC21FB5B0637E355B230C8E78CE65B9.d.93CBF2ACB2B4F2B5F84604DC1D934E59.e.24")>]
# print(len(input_tags))
# #23

##################################
# print all the link texts present in demo.html

links = driver.find_elements("tag name", "a")
for link in links:
    print(link.text)
#    print(link.get_property("href"))
    sleep(1)



# '''
# # C:\Users\Sumit\AppData\Local\Programs\Python\Python311\python.exe C:\Users\Sumit\PycharmProjects\selenium_M12\multiple_element1.py
# # Download
# # https://www.android.com/intl/en_in/
# # Download
# # https://www.linux.org/
# # Download
# # https://www.microsoft.com/en-in/windows
# # Download
# # https://www.apple.com/in/
# # Inbox(2000)
# # http://www.google.com/
# # Shopping
# # http://www.google.com/
# # Continue Shopping
# # http://demowebshop.tricentis.com/
# # Apple
# # https://www.apple.com/in/
# # Google
# # https://www.google.com/
# # Yahoo
# # https://www.apple.com/in/
# # Yelp
# # https://www.google.com/
# # Model Window
# # file:///C:/Users/Sumit/PycharmProjects/selenium_M12/HTML_files/demo.html#
# # Webshop
# # http://demowebshop.tricentis.com/
# # LOGIN
# # https://the-internet.herokuapp.com/basic_auth
# # Facebook
# # https://www.facebook.com/
# #
# # Process finished with exit code 0 '''

###########################################
# words = ["hello", "hai", "welcome", "python", "world", "program", "how", "are", "you"]
# text_boxes = driver.find_elements("name", 'fname')
# for text_box, word in zip(text_boxes, words):
#     text_box.send_keys(word)
#     sleep(1)

"""
zip(iterator)
zip is an inbuilt class which combines the two or more iterables
"""