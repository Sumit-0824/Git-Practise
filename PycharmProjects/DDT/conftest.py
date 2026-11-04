import pytest
from Library.cookies import CookieManager


@pytest.fixture
def _driver():
    from selenium import webdriver
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opts)
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.support.select import Select
    # from selenium.webdriver.support.ui import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC
    driver.get("https://www.stacxuat.com/Login/index")
    driver.implicitly_wait(40)
    if CookieManager.load_cookies(driver):
        driver.refresh()
    driver.maximize_window()
    yield driver
    driver.quit()






