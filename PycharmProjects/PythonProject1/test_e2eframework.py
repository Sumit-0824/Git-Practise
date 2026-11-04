import json

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage, ShopPage
test_data_path = 'C:\\Users\\Sumitkumar.Sinha\\PycharmProjects\\PythonProject1\\data\\test_e2eframework.json' #../-to comeout of the current folder and go to data folder and get the test_e2eframework.json file
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data['data'] # Assuming the JSON structure has a key 'data' containing the list of test data

@pytest.mark.parametrize("test_list_item",  test_list) #collect the data from the json file and store it in test_list_item variable and pass it to the test_e2e function
def test_e2e(browserInstance, test_list_item):
    driver= browserInstance
    #Fetching the driver instance from the fixture browserInstance
    # opts = webdriver.ChromeOptions()
    # opts.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=opts)
    # driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    # driver.implicitly_wait(5) #line 9 to line 13 is moved to conftest.py and browserInstance fixture is created
    # //a[contains(@href,'shop')],a[href*='shop'],a[href$='shop'],a[href^='shop']
    #fetching the login credentials from the POM LoginPage class
    login_page = LoginPage(driver)
    login_page.getTitle()
    #login_page.login()
    #shop_page=login_page.login("rahulshettyacademy","Learning@830$3mK2")
    shop_page=login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])  #fetching the login credentials from the json file
    # driver.find_element("id","username").send_keys("rahulshettyacademy")
    # driver.find_element("id","password").send_keys("Learning@830$3mK2")
    # driver.find_element("id","signInBtn").click()
    #shop_page = ShopPage(driver)  #If we keep this at the end to loginpage no need to create driver again and again
    shop_page.add_item_to_cart(test_list_item["product_name"])  #fetching the product name from the json file
    # driver.find_element("xpath", "//a[text()='Shop']").click()
    # products = driver.find_elements("xpath", "//div[@class='card h-100']")
    # for product in products:
    #     product_name = product.find_element("xpath", "div/h4/a").text
    #     if product_name == "Blackberry":
    #         product.find_element("xpath", "div/button").click()
    checkout_confirmation_page = shop_page.go_to_cart()
    checkout_confirmation_page.checkout()
    checkout_confirmation_page.enter_delivery_address(test_list_item["countryName"])  #fetching the country name from the json file
    checkout_confirmation_page.validate_success_message()
    #check in  enter_delivery_details method in checkout_confirmation.py
    #driver.find_element("xpath", "//a[@class='nav-link btn btn-primary']").click()
    #     # driver.find_element("xpath", "//button[contains(@class,'btn-success')]").click()
    # driver.find_element("id", "country").send_keys("ind")
    # wait = WebDriverWait(driver, 10)
    # wait.until(expected_conditions.presence_of_element_located(("link text", "India")))
    # driver.find_element("link text", "India").click()
    # driver.find_element("xpath", "//div[@class='checkbox checkbox-primary']").click()
    # driver.find_element("css selector", "input[type='submit']").click()
    # # driver.find_element("xpath","//input[@value='Purchase']").click()
    # success_text=driver.find_element("xpath","//div[@class='alert alert-success alert-dismissible']")
    #Check in validate_success_message method in checkout_confirmation.py
    # success_text = driver.find_element("class name", 'alert-success').text
    #
    # assert "Success! Thank you!" in success_text



