from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    SUMMARY = (By.XPATH, "//*[@class='summary-prices']")

    def verify_checkout_summary(self):
        assert self.get_element(self.SUMMARY).is_displayed()