#operator are the special symbols that perform specific operations on one, two, or more operands. The value that the operator operates on is called the operand. For example, in the expression 2 + 3, the operator is + and the operands are 2 and 3.
#All the operator are library functions in Python.
#Whenever we want to perform any operation on the operands, we use the operator. The operator can be classified into the following types

# Sorting the list of vegetables in the browser and comparing it with the sorted list of vegetables in the browser.
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.find_element("xpath","//span[text()='Veg/fruit name']").click()
browser_sorted_list=[]
#collect all the vegetable names in browser into list
vegetables=driver.find_elements("xpath","//tr/td[1]")
for ele in vegetables:
    browser_sorted_list.append(ele.text)
original_list=browser_sorted_list.copy()
#sort the browser list to check whether the list is sorted or not
browser_sorted_list.sort()
#check whether the original list is same as the sorted list or not
assert original_list==browser_sorted_list