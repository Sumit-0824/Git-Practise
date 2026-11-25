import pytest
@pytest.fixture(autouse=True,scope="class")
def test_browser_launch():
    from time import sleep
    from selenium import webdriver
    opts = webdriver.ChromeOptions()  # to launch the browser without instantly closing
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opts)

class TestAlert:
    def test_launch_application(self):
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()

    # InvalidArgumentException-- if wrong locator
    # Simple Alert
    def test_locating(self):
        driver.find_element("xpath", '//button[text()="Simple Alert"]').click()
        sleep(2)

        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        sleep(2)


