from selenium.webdriver.common.by import By
class LoginPage:
    # username_input = (By.ID, "Email")
    # password_input = (By.ID, "Password")
    # login_button = (By.CSS_SELECTOR, "button[type='submit']")
    # logout_button = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver
        # self.username_input = (By.ID, "Email")  # Correctly using By.ID
        # self.password_input = (By.ID, "Password")
        # self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        # self.logout_button = (By.LINK_TEXT, "Logout")

        # self.username_input = (By.ID, "UserLogin_username")  # Correctly using By.ID
        # self.password_input = (By.ID, "UserLogin_password")
        # self.login_button = (By.XPATH, "//button[@id='login-submit']")
        #self.logout_button = (By.LINK_TEXT, "Logout")

        self.username_input = (By.CSS_SELECTOR, "input[placeholder='Username']")  # Update selector based on the actual page
        self.password_input = (By.CSS_SELECTOR, "input[placeholder='Password']")  # Update selector based on the actual page
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
    def setuserName(self, username):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(*self.login_button).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()




