# from selenium import webdriver
# from selenium.webdriver.common.by import By
# class Login:
#     textbox_username_id="Email"
#     textbox_password_id="Password"
#     button_login_Xpath="///button[normalize-space()='Log in']"
#     link_logout_linktext="logout"
#
#     def __init__(self,driver):
#         self.driver=driver
#
#     def setuserName(self,username):
#         self.driver.find_element_by_id(self.textbox_username_id).clear()
#         self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
#
#     def setpassword(self,password):
#         self.driver.find_element(By.ID, "self.textbox_password_id").clear()
#         self.driver.find_element(By.ID, "self.textbox_password_id").send_keys(password)
#        # self.driver.find_element_by_id(self.textbox_password_id).clear()
#         #self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
#
#     def clicklogin(self):
#         self.driver.find_element_by_Xpath(self.button_login_Xpath).click()
#
#     def logout(self):
#         self.driver.find_element_by_linktext(self.link_logout_linktext).click()
