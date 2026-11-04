import time

from POM.login_page import LoginPage


class TestLoginPage :
    def test_login(self,_driver):
        lp = LoginPage(_driver)
        lp.enter_email()
        lp.enter_password()
        lp.click_login_button()
        time.sleep(20)
        lp.click_verify_button()


