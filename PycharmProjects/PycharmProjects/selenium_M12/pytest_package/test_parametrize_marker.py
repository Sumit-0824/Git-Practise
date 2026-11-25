"""
parameterize is an inbuilt marker, to pass arguments
@pytest.mark.parametrize("arg_name",arg_value)
arg_name--string
arg_value-list  example-[2,3,4,5] ---integer
 if we have data in string then use nested list-[[data]]


"""
from time import sleep

import pytest

# @pytest.mark.parametrize("num",[2,4,6,8])
# def test_add(num):
#     assert num +2 ==10, "sum is not equal to 10"
####################################################################
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

def test_reg():
    driver.find_element("xpath",'//a[text()="Register"]').click()
    sleep(2)
@pytest.mark.parametrize("first_name,last_name",[["Sumit","Sinha"]])
def test_name(first_name,last_name):
    driver.find_element("id","FirstName").send_keys(first_name)
    driver.find_element("name","LastName").send_keys(last_name)
    sleep(2)


