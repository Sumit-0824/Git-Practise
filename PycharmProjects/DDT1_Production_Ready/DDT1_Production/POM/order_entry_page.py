from pathlib import Path
from selenium.webdriver.common.by import By
from Library.sel_wrapper import SeleniumWrapper
from Library.select2 import Select2

class OrderEntryPage:
    CLIENT = (By.XPATH, "//span[@id='select2-Customer-container']/parent::span")
    PRODUCT = (By.XPATH, "//span[@id='select2-Single-ProductUID-container']/parent::span")
    LOAN_NUMBER = (By.ID, "LoanNumber")
    FILE_UPLOAD = (By.ID, "DocumentUploadNew")
    SAVE = (By.CSS_SELECTOR, "button[title='Save and proceed to My Order(s)']")

    def __init__(self, driver):
        self.ui = SeleniumWrapper(driver)
        self.select2 = Select2(self.ui)

    def create_order(self, client, product, loan_number, file_path):
        self.select2.select_by_text(self.CLIENT, client)
        self.select2.select_by_text(self.PRODUCT, product)
        self.ui.enter_txt(self.LOAN_NUMBER, loan_number)

        path = Path(file_path).resolve()
        if not path.is_file():
            raise FileNotFoundError(f"Upload file not found: {path}")
        self.ui.upload_file(self.FILE_UPLOAD, path)
        self.ui.click_element(self.SAVE)
