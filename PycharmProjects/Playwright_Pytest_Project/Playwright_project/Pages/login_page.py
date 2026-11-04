# from playwright.sync_api import Page
# from playwright.sync_api import Page, expect
#
#
# class LoginPage:
#
#     def __init__(self, page: Page):
#         self.page = page
#
#         self.username = page.locator("#Username")
#         self.password = page.locator("#Password")
#         self.login_button = page.locator("//button[@type='submit']")
#
#         self.dashboard = page.get_by_text("Dashboard")
#
#     def open(self):
#         self.page.goto("https://your-application-url/Login")
#
#     def enter_username(self, username: str):
#         self.username.fill(username)
#
#     def enter_password(self, password: str):
#         self.password.fill(password)
#
#     def click_login(self):
#         self.login_button.click()
#
#     def verify_dashboard(self):
#         expect(self.dashboard).to_be_visible()
#         To make locator more reliable, we can use get_by_label and get_by_role methods instead of using locators with IDs and XPaths. This will make the code more readable and maintainable.
from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):

        self.page = page

        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.login_button = page.get_by_role(
            "button",
            name="Login"
        )

    def open(self):
        self.page.goto(
            "https://your-application-url/Login"
        )

    def login(self, username: str, password: str):

        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def verify_dashboard(self):

        expect(
            self.page.get_by_text("Dashboard")
        ).to_be_visible()