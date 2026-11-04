import os# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver=None
@pytest.fixture(scope="class")
def init_driver(request):
    opts = Options()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser name: browser selector"
    )



@pytest.fixture(scope="function")
def browserInstance(request):
    global driver

    browser_name = request.config.getoption("browser_name")

    if browser_name.lower() == "chrome":

        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opts)
        driver.implicitly_wait(5)

    elif browser_name.lower() == "firefox":

        opts = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=opts)


    elif browser_name.lower() == "ie":

        opts = webdriver.IeOptions()
        driver = webdriver.Ie(options=opts)

    else:
        raise pytest.UsageError(
            "Invalid browser. Use chrome, firefox, or ie."
        )

    driver.get("https://laravel.stacxuat.com/Login/index")
    driver.implicitly_wait(5)

    yield driver

    driver.close()

@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)

