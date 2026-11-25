from POM.login_page import LoginPage

class TestLoginPage:
    def test_login(self,_driver):    #Pass the fixture function as argument
        lp = LoginPage(_driver)      #_driver instead of driver
        lp.enter_email()
        lp.enter_password()
        lp.click_login()
        lp.click_men()
        lp.click_add_cart()