from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.implicitly_wait(5)
#//a[contains(@href,'shop')],a[href*='shop'],a[href$='shop'],a[href^='shop']
driver.find_element("xpath","//a[text()='Shop']").click()
products=driver.find_elements("xpath","//div[@class='card h-100']")
for product in products:
    product_name=product.find_element("xpath","div/h4/a").text
    if product_name=="Blackberry":
        product.find_element("xpath","div/button").click()

driver.find_element("xpath","//a[@class='nav-link btn btn-primary']").click()
driver.find_element("xpath","//button[@class='btn btn-success']").click()
driver.find_element("id","country").send_keys("ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located(("link text","India")))
driver.find_element("link text","India").click()
driver.find_element("xpath","//div[@class='checkbox checkbox-primary']").click()
driver.find_element("css selector","input[type='submit']").click()
#driver.find_element("xpath","//input[@value='Purchase']").click()
#success_text=driver.find_element("xpath","//div[@class='alert alert-success alert-dismissible']")
success_text=driver.find_element("class name",'alert-success').text

assert "Success! Thank you!" in success_text
driver.close()

