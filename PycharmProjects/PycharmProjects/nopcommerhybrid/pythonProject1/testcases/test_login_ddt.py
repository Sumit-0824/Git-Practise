import time

import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import time

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger=LogGen.logger()

    def test_login_ddt(self,setup):
        self.logger.info("********Test_002_DDT_Login*****")
        self.logger.info("********Test_002_DDT_Login*****")
        self.driver=setup
        self.driver.get(self,baseURL)
        self.lp=LoginPage(self.driver)
        self.rows=XLUtils.getRowCount(self.path,'sheet1')
        print("Number of ROws in a excel:",self.rows)

        1st_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'sheet1',r,1)
            self.password=XLUtils.readData(self.path,'sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'sheet1',r,3)

            self.lp.setuserName(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep()
            act_title==self.driver.title
            exp_title="Dashboard/nopcommerce.administration"


            if act_title==self.driver.title
                if self.exp=="Pass"
                    self.logger.info("******Passed*************")
                    self.lp.click_logout();
                    1st_status.append("Pass")

                elif self.exp=="Fail"
                    self.logger.info("******Failed*************")
                    self.lp.click_logout();
                    1st_status.append("Fail")

            if act_title != self.driver.title
                if self.exp == "Pass"
                    self.logger.info("******Failed****")
                    self.lp.click_logout();
                    1st_status.append("Fail")

                elif self.exp== "Fail"
                    self.logger.info("******Passed*******")
                    1st_status.append("Pass")

             if "Fail" not in 1st status:
                 self.logger.info("********Login DDT test Passed*****")
                 self.driver.close()
                assert True

              else:
                  self.logger.info("********Login DDT test Failed*****")
                  self.driver.close()
                  assert False

            self.logger.info("*******End ofLogin DDT Test*****")
            self.logger.info("********Completed TC_Login_DDT_002***************")