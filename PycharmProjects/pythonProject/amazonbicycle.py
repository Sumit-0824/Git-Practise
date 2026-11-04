from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Setup Chrome Driver ---
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

try:
    # Step 1: Go to Amazon
    driver.get("https://www.amazon.com")

    # Step 2: Locate the search bar and search for "bicycle"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("bicycle")
    search_box.send_keys(Keys.RETURN)

    # Step 3: Wait for results to load
    time.sleep(3)

    # Step 4: Get all bicycle product titles
    product_elements = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")

    bicycles = [product.text for product in product_elements if product.text.strip() != ""]
    print("\n--- Bicycles Found ---")
    for i, title in enumerate(bicycles, start=1):
        print(f"{i}. {title}")

    # Step 5: Select (click) the bicycle for women if available
    for product in product_elements:
        if "women" in product.text.lower():
            print(f"\n✅ Selecting: {product.text}")
            driver.execute_script("arguments[0].scrollIntoView();", product)
            product.click()
            break
    else:
        print("\n❌ No bicycle for women found on this page.")

finally:
    # Optional: keep the browser open for review
    time.sleep(10)
    driver.quit()
