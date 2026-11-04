import os
from datetime import datetime
import pytest


#need to work
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("_driver")

        if driver:
            screenshot_dir = os.path.join(os.getcwd(), "Screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            file_name = f"{item.name}_{timestamp}.png"

            driver.save_screenshot(
                os.path.join(screenshot_dir, file_name)
            )

            print(f"\nScreenshot saved : {file_name}")