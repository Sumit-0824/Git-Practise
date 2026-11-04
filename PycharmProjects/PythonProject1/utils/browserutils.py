class BrowserUtils:

    def __init__(self,driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

#Utils are used for reusable actions for all testcase.We can create utils and pass this as argument in test class.
#It will be activated by passing declaring as global variable -super()__init__(driver)

#To run test parallelly we need to install pip install pytest -xdist through command prompt
#Pass pytest -n 2/3...
# report will be generated in html format by using command pytest --html=report.html
#pytest test_e2eframework.py -vs --html reports/report.html