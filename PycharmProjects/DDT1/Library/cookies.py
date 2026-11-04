import pickle
import os

COOKIE_FILE = "cookies.pkl"

class CookieManager:

    @staticmethod
    def save_cookies(driver):
        with open(COOKIE_FILE, "wb") as file:
            pickle.dump(driver.get_cookies(), file)

    @staticmethod
    def load_cookies(driver):
        if not os.path.exists(COOKIE_FILE):
            return False

        with open(COOKIE_FILE, "rb") as file:
            cookies = pickle.load(file)

        for cookie in cookies:
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"Cookie skipped: {e}")

        return True