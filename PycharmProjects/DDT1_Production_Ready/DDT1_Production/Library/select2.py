from selenium.webdriver.common.by import By

class Select2:
    def __init__(self, ui):
        self.ui = ui

    def select_by_text(self, container_locator, text):
        self.ui.click_element(container_locator)
        search = (By.CSS_SELECTOR, "input.select2-search__field")
        self.ui.enter_txt(search, text)
        option = (
            By.XPATH,
            f"//li[contains(@class,'select2-results__option') and normalize-space()={self._literal(text)}]"
        )
        self.ui.click_element(option)

    @staticmethod
    def _literal(value):
        if "'" not in value:
            return f"'{value}'"
        if '"' not in value:
            return f'"{value}"'
        parts = value.split("'")
        return "concat(" + ", \'\'\', ".join(f"'{p}'" for p in parts) + ")"
