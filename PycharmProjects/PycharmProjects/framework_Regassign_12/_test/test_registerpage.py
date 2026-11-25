
from POM.register import RegisterPage
class TestRegisterPage:
    def test_login(self,_driver):
        lp = RegisterPage(_driver)
        # To call methods inside the class    Syntax-----  obj.methodname
        # lp.enter_radio()
        lp.enter_fname()
        lp.enter_lname()
        lp.enter_email()
        lp.enter_password()
        lp.enter_cpassword()
        lp.click_register()