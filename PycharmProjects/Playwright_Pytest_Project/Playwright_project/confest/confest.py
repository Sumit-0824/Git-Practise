import pytest
from playwright.sync_api import Page


@pytest.fixture
def browser_page(page: Page):
    page.goto("https://www.google.com")
    return page