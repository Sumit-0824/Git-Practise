
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options to disable notifications
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Path to your ChromeDriver
serv_obj = Service("C:\\Drivers\\chromedriver-win64.zip\\chromedriver-win64\\chromedriver.exe")

# Launch Chrome with the specified options
driver = webdriver.Chrome(service=serv_obj, options=chrome_options)

# Example usage: Open a website
driver.get('https://www.example.com')

# Don't forget to quit the driver
driver.quit()
