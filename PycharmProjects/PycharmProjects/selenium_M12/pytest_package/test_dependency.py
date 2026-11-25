"""
pip install pytest-dependency -------install in cmd
if test_a pass==== test_b will execute
if test_a fails====test_b will be skipped
command to run----pytest test_filename.py -vs


"""
import pytest
@pytest.mark.dependency
def test_a():
    assert 4==4      # assert 4==4
@pytest.mark.dependency(depends=["test_a"])
def test_b():
    assert "hello"=="hai"



# from time import sleep
#
# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
#
#
# @pytest.mark.dependency()
# def test_reg():
#     #driver.find_element("link text",'//a[text()="Register"]').click()  # wrong xpath to check the skipping
#     driver.find_element("link text", "Register").click()
#     sleep(2)
# @pytest.mark.dependency(depends=["test_reg"])
# def test_fname():
#     driver.find_element("id", "FirstName").send_keys("Sumit")

