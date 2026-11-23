import json
import re
from pathlib import Path
from typing import Any

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


LOGIN_DATA_PATH = Path(__file__).resolve().parents[1] / "test_data" / "login_data.json"
with LOGIN_DATA_PATH.open(encoding="utf-8") as data_file:
    LOGIN_DATA: dict[str, list[dict[str, Any]]] = json.load(data_file)


@pytest.mark.parametrize(
    "credentials",
    LOGIN_DATA["valid_logins"],
    ids=[case["id"] for case in LOGIN_DATA["valid_logins"]],
)
def test_valid_login(page: Page, credentials: dict[str, str]) -> None:
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(credentials["username"], credentials["password"])

    expect(page).to_have_url(re.compile(r".*/logged-in-successfully/?$"))
    expect(login_page.success_message).to_be_visible()
    expect(login_page.logout_button).to_be_visible()
