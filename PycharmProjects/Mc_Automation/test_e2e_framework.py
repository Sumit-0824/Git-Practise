import json
import time

import pytest

from POM.login import LoginPage

test_data_path = 'C:\\Users\\Sumitkumar.Sinha\\PycharmProjects\\Mc_Automation\\data\\test_e2e_framework.json' #../-to comeout of the current folder and go to data folder and get the test_e2eframework.json file
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data['data']

@pytest.mark.parametrize("test_list_item",  test_list) #collect the data from the json file and store it in test_list_item variable and pass it to the test_e2e function
def test_e2e(browserInstance, test_list_item):
    driver= browserInstance
    login_page = LoginPage(driver)
    login_page.getTitle()
    order_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
    order_page.enter_client_info(test_list_item["client_info"])
    time.sleep(15)
