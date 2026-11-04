# from pages.login_page import LoginPage
#
#
# def test_valid_login(page):
#
#     login = LoginPage(page)
#
#     login.open()
#
#     login.enter_username("your_username")
#     login.enter_password("your_password")
#
#     login.click_login()
#
#     login.verify_dashboard()
# To make the test more readable and maintainable, we can use the login method from the LoginPage class to perform the login action instead of calling the enter_username, enter_password, and click_login methods separately. This will reduce code duplication and make the test easier to read.

from pages.login_page import LoginPage


def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "your_username",
        "your_password"
    )

    login_page.verify_dashboard()
