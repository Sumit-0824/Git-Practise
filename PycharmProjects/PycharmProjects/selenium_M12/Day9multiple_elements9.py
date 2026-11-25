"""
# handling multiple elements
find_element() : 1 web element
find_elements() : list[] of web elements
//{tagname)- for selecting all the elements under
"""
from time import sleep
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
elements = driver.find_elements("xpath", '//div[@class="block block-category-navigation"]//a')
print(elements)    #it will give output in list format
#Output-[<selenium.webdriver.remote.webelement.WebElement (session="ff5351ab48b8293bd5107445d83b0f7a", element="f.CF429815F3DDDB0E2D7FDE59CC724EA4.d.E1B760EF0BA178B41438F15A5A951A4B.e.35")>, <selenium.webdriver.remote.webelement.WebElement (session="ff5351ab48b8293bd5107445d83b0f7a", element="f.CF429815F3DDDB0E2D7FDE59CC724EA4.d.E1B760EF0BA178B41438F15A5A951A4B.e.36")>, <selenium.webdriver.remote.webelement.WebElement (session="ff5351ab48b8293bd5107445d83b0f7a", element="f.CF429815F3DDDB0E2D7FDE59CC724EA4.d.E1B760EF0BA178B41438F15A5A951A4B.e.37")>, <selenium.webdriver.remote.webelement.WebElement (session="ff5351ab48b8293bd5107445d83b0f7a", element="f.CF429815F3DDDB0E2D7FDE59CC724EA4.d.E1B760EF0BA178B41438F15A5A951A4B.e.38")>, <selenium.webdriver.remote.webelement.WebElement (session="ff5351ab48b8293bd5107445d83b0f7a", element="f.CF429815F3DDDB0E2D7FDE59CC724EA4.d.E1B760EF0BA178B41438F15A5A951A4B.e.39")>, <selenium.webdriver.remote.webelement.WebElement (session="ff5351ab48b8293bd5107445d83b0f7a", element="f.CF429815F3DDDB0E2D7FDE59CC724EA4.d.E1B760EF0BA178B41438F15A5A951A4B.e.40")>, <selenium.webdriver.remote.webelement.WebElement (session="ff5351ab48b8293bd5107445d83b0f7a", element="f.CF429815F3DDDB0E2D7FDE59CC724EA4.d.E1B760EF0BA178B41438F15A5A951A4B.e.41")>]

for ele in elements:
    print(ele.text)  # text is a property
    sleep(1)

#Output-
'''
Books
Computers
Electronics
Apparel & Shoes
Digital downloads
Jewelry
Gift Cards
'''
#################################################
# get the text of all the footer links

elements = driver.find_elements("xpath", '//div[@class="footer-menu-wrapper"]//a')
for ele in elements:
    print(ele.text)
    sleep(1)
'''
output
Sitemap
Shipping & Returns
Privacy Notice
Conditions of Use
About us
Contact us
Search
News
Blog
Recently viewed products
Compare products list
New products
My account
Orders
Addresses
Shopping cart
Wishlist
Facebook
Twitter
RSS
YouTube
Google+
'''