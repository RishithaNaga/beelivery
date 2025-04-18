from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    cookies_XPATH=(By.XPATH, "//*[contains(text(), 'This website uses cookies')]")
    SIGN_IN_LINK = (By.XPATH, "//a[contains(text(),'Sign In')]")
    EMAIL = (By.ID, "tbEmail")
    PASSWORD = (By.ID, "tbPassword")
    SIGN_IN_BTN = (By.XPATH, "//input[@value='Sign In']")

    def login(self, email, password):
        self.check_visibility(self.cookies_XPATH)
        self.click(self.SIGN_IN_LINK)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.click(self.SIGN_IN_BTN)