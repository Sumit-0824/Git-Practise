from playwright.sync_api import Page


class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.success_message = page.get_by_text(
            "Congratulations student. You successfully logged in!"
        )
        self.logout_button = page.get_by_role("link", name="Log out")

    def open(self) -> None:
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()
