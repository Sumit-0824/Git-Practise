from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)

path=r"C:\Users\Sumit\PycharmProjects\selenium_M12\HTML_files\demo.html"
driver.get(path)
driver.maximize_window()
element=driver.find_element("id","multiple_cars")
select_obj=Select(element)

select_obj.select_by_value("aud")
sleep(2)
select_obj.select_by_index(2)
sleep(2)
select_obj.select_by_visible_text("Ford")
sleep(2)
# print(select_obj.is_multiple)   #if multiple elements are selected  #True

########For deselecting any selected input
# select_obj.deselect_by_value("aud")
# sleep(2)
# select_obj.deselect_by_index(2)
# sleep(2)
# select_obj.deselect_by_visible_text("Ford")
# sleep(2)
#################Deselecting all##############
#select_obj.deselect_all()
##########Selecting all options######################
# all_options=select_obj.options
# for option in all_options:
#     print(option.text)

''' Output
Select car:
Audi
BMW
Ford
Honda
Jaguar
Land Rover
Mercedes
Mini
Nissan
Toyota
Volvo
'''
##For selecting 1st option####

#print(select_obj.first_selected_option.text)        #Audi

selected_options=select_obj.all_selected_options
for option in selected_options:
    print(option.text)

'''
output-
Audi
BMW
Ford
'''