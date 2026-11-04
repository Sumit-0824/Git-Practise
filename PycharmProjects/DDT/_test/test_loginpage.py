import time

from POM.login_page import LoginPage


class TestLoginPage :
    def test_login(self,_driver):
        lp = LoginPage(_driver)
        lp.enter_email()
        lp.enter_password()
        lp.click_login_button()
        time.sleep(30)
        lp.click_verify_button()
        print(_driver.current_url)
        print(_driver.title)
        lp.click_single_entry()
        time.sleep(10)
        # lp.click_client()
        lp.enter_client()
        #time.sleep(10)
        lp.select_product("Post Closing Review")
        time.sleep(20)
        lp.enter_ordernumber()
        time.sleep(10)
        lp.upload_document()
        time.sleep(10)
        lp.click_save_continue()
        lp.click_classification()
        lp.search_loan("Testloansk250926004")



