"""
conftest-to share the common code
"""
import pytest
@pytest.fixture()
def _driver():
    from selenium import webdriver  # to launch browser
    opts = webdriver.ChromeOptions()  # to not close the broswer immediately
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opts)
    driver.get("https://demowebshop.tricentis.com/login")
    driver.maximize_window()
    yield driver
    driver.quit()



#To run conftest file ----pytest -vs


