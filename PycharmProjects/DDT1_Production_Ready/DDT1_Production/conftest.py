import pytest
from datetime import datetime
from pathlib import Path
from selenium import webdriver

BASE_URL = "https://www.stacxuat.com/Login/index"

@pytest.fixture
def _driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)
    driver.implicitly_wait(0)
    driver.get(BASE_URL)

    yield driver

    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        folder = Path("reports/screenshots")
        folder.mkdir(parents=True, exist_ok=True)
        name = f"{request.node.name}_{datetime.now():%Y%m%d_%H%M%S}.png"
        driver.save_screenshot(str(folder / name))
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
