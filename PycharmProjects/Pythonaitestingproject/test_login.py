from playwright.sync_api import Page


def test_open_google(page: Page):
    page.goto("https://www.google.com")

    print(page.title())

    assert "Google" in page.title()
