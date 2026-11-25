import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    # baseURL="https://admin-demo.nopcommerce.com/"
    # username="admin@yourstore.com"
    # password="admin"
    # use dynamic value from read config


    # baseURL = "https://avanze.darwinbox.in/user/login"
    # username = "Admin"
    # password = "admin123"

    #baseURL = https: // admin - demo.nopcommerce.com /
    #username = admin @ yourstore.com
    #password = admin
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getPassword()



    def test_homePageTitle(self,setup):
        self.logger.info("*********Test_001_Login*********")
        self.logger.info("*********Verifying HomePage Title*********")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        #self.driver.close()
        if act_title=="Your store. Login":
            assert True
            self.logger.info("*********HomePage is passed*********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********HomePage is Failed*********")
            assert False


    def test_login(self,setup):
        self.logger.info("*********Verifying login*********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setuserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title= self.driver.title
        if act_title =="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*********Login is passed*********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_login.png")
            self.driver.close()
            self.logger.error("*********Login is Failed*********")
            assert False
