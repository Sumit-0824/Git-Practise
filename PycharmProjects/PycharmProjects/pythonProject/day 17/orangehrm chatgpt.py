from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the path to your chromedriver.exe
driver_path = '/path/to/your/chromedriver.exe'
# Initialize Chrome WebDriver
Serv_obj = Service("C:\Drivers\chromedriver-win64.zip\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome()

# Open the URL
url = "https://opensource-demo.orangehrmlive.com/"
driver.get(url)

try:
    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtUsername")))

    # Find the username and password input elements and enter credentials
    username_input = driver.find_element(By.ID, "txtUsername")
    password_input = driver.find_element(By.ID, "txtPassword")

    username_input.send_keys("admin")
    password_input.send_keys("admin123")

    # Find and click the login button
    login_button = driver.find_element(By.ID, "btnLogin")
    login_button.click()

    # Wait for the dashboard page to load after login
    WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))

    # Confirm successful login by printing the title of the dashboard page
    print("Login successful. Dashboard title:", driver.title)

except Exception as e:
    print("Error during login:", e)

finally:
    # Close the browser session
    driver.quit()
