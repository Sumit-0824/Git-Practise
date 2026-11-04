import pytest
from data.reading_objects import read_test_data
from POM.login_page import LoginPage
from POM.order_entry_page import OrderEntryPage

@pytest.mark.regression
@pytest.mark.parametrize("data", read_test_data())
def test_login_and_upload(_driver, data):
    login = LoginPage(_driver)
    login.login(data["username"], data["password"])

    # If Verify/OTP is mandatory in your environment, complete it here.
    # login.click_verify()

    _driver.get(data["order_url"])

    OrderEntryPage(_driver).create_order(
        client=data["client"],
        product=data["product"],
        loan_number=data["loan_number"],
        file_path=data["file_path"]
    )
