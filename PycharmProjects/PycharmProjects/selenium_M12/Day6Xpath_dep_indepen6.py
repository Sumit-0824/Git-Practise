'''dynamic xpath
xpath using dependent and independent element

1. identify the dependent and independent element
2. write the xpath expression for independent element
3. traverse back till we get the common parent of both dependent and independent element /..
4. locate the dependent element (writing the xpath for dep ele)
"""




from time import sleep
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

path=r"C:\Users\Sumit\PycharmProjects\selenium_M12\HTML_files\demo.html"
driver.get(path)
driver.maximize_window()
# #Java
# driver.find_element("xpath",'//td[text()="Java"]/..//input[@name="download"]').click()
# sleep(2)
# #Perl
# driver.find_element("xpath",'//td[text()="Perl"]/..//input[@name="download"]').click()
# sleep(2)
#python-- using name attribute
# driver.find_element("xpath",'//td[text()="Python"]/..//input[@type="checkbox"]').click()
# sleep(2)

# #program to select all the checkboxes
language=["Java","Ruby","Perl","Python","C#","JavaScript"]
# for lang in language:
#     driver.find_element("xpath",f'//td[text()="{lang}"]/..//input[@name="download"]').click()
#     sleep(2)

#program to select all the checkboxes in reverse order
for lang in language[::-1]:
    driver.find_element("xpath",f'//td[text()="{lang}"]/..//input[@name="download"]').click()  #formated string
    sleep(2)