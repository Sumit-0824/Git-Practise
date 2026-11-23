import base64
import os
import re
from typing import Generator

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright
from pytest_html import extras

from browser_utils import create_browser_context, launch_browser


@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    with sync_playwright() as playwright_instance:
        yield playwright_instance


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run Chromium with a visible browser window.",
    )


@pytest.fixture(scope="session")
def browser(request: pytest.FixtureRequest, playwright: Playwright) -> Generator[Browser, None, None]:
    headed = request.config.getoption("--headed")
    headless = not headed and os.getenv("HEADLESS", "true").strip().lower() not in {
        "0",
        "false",
        "no",
    }
    browser_instance = launch_browser(playwright, headless=headless)
    yield browser_instance
    browser_instance.close()


@pytest.fixture
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    browser_context = create_browser_context(browser)
    yield browser_context
    browser_context.close()


@pytest.fixture
def page(context: BrowserContext) -> Page:
    return context.new_page()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[object]):
    outcome = yield
    report = outcome.get_result()
    if not report.failed or call.excinfo is None:
        return

    page = item.funcargs.get("page")
    if page is None or page.is_closed():
        return

    screenshots_dir = item.config.rootpath / "reports" / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    test_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid)
    screenshot_path = screenshots_dir / f"{test_name}.png"
    page.screenshot(path=str(screenshot_path), full_page=True)

    image = base64.b64encode(screenshot_path.read_bytes()).decode("ascii")
    report_extras = getattr(report, "extras", [])
    report_extras.append(
        extras.image(image, name="Failure screenshot", mime_type="image/png")
    )
    report.extras = report_extras
