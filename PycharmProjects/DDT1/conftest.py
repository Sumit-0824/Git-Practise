import pytest
from Library.cookies import CookieManager


@pytest.fixture
def _driver():
    from selenium import webdriver
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opts)
    driver.get("https://www.stacxuat.com/Login/index")
    if CookieManager.load_cookies(driver):
        driver.refresh()
    driver.maximize_window()
    yield driver
    driver.quit()






