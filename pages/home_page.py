import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class HomePage(BasePage):
    cookie_accept_id=(By.ID,"//*[@id='cookiescript_accept']")
    POSTCODE = (By.XPATH, '//input[@placeholder="Enter your postcode"]')
    GROCERY_RADIO = (By.XPATH, '//input[@value="Groceries / Alcohol / Tobacco"]')
    PLACE_ORDER = (By.XPATH, "//span[contains(text(),'Place Order')]")

    def enter_postcode_and_select_groceries(self, postcode):
        try:
            print("searching for cookies")
            self.check_visibility1(self.cookie_accept_id)
            self.click(self.cookie_accept_id)
            print("cookie found")
        except Exception as e:
            print("Exception found while searching for cookies popup",type(e).__name__)

        try:
            self.send_keys(self.POSTCODE, postcode)
            self.click(self.GROCERY_RADIO)
        except StaleElementReferenceException:
            self.click(self.GROCERY_RADIO)
        # time.sleep(10)
        # self.send_keys(self.POSTCODE,postcode)
        # self.click(self.GROCERY_RADIO)

    def place_order(self):
        element = self.driver.find_element(*self.PLACE_ORDER)
        ActionChains(self.driver).move_to_element(element).click().perform()