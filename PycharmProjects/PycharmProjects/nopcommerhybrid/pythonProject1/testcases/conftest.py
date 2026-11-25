from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver

#******************************************Pytest html Reports********************
#It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.metadata['ProjectName']='nopcommerce'
    config.metadata['ModuleName']='customers'
    config.metadata['Tester']='Pavan'



#It is hook for delete/Modify Environment Info  to Html Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME",None)
    metadata.pop("Plugins", None)