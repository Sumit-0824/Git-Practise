import time

import pytest


@pytest.fixture()
def _driver():
    from selenium import webdriver  # to launch browser
    opts = webdriver.ChromeOptions()  # to not close the broswer immediately
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opts)
    driver.get("https://shoppersstack.com/user-signin")
    driver.maximize_window()
#    driver.implicitly_wait(10)
    time.sleep(10)
    yield driver
    driver.quit()