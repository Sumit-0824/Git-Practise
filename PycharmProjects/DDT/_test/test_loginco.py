from Library.cookies import CookieManager
from POM.login_page import LoginPage

def test_login(self, _driver):
    lp = LoginPage(_driver)

    lp.enter_email()
    lp.enter_password()
    lp.click_login_button()

    input("Complete OTP and press Enter...")

    CookieManager.save_cookies(_driver)