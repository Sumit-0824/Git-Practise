from playwright.sync_api import playwright, Page


def test_login(page: Page):
    # Navigate to the login page
    page.goto("https://www.stacxuat.com/Login/index")

    # Fill in the username and password fields
    page.fill("input[name='username']", "sumitkumar.sinha@avanzetechlabs.com")
    page.fill("input[name='password']", "password123")

    # Click the login button
    page.click("button[type='submit']")

    # Assert that the user is redirected to the dashboard
    assert page.url == "https://www.stacxuat.com/Orderentry/index"