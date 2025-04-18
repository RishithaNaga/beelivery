from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class ProductPage(BasePage):
    SEARCH_BAR = (By.XPATH, '//input[@class="textboxItemSearch ProductSearchBox"]')
    SEARCH_ICON = (By.XPATH, '//img[@class="productSearchIcon"]')
    ADD_CAKE = (By.XPATH, '//img[@alt="Gourmet Gold Savoury Cake Meat 8 x 85g (680g)"]//ancestor::div[@class="product_box_Small_container boxP578025"]//descendant::div[@class="plusbutton"]')
    SIDE_PANEL_ITEM = (By.XPATH, '//div[@class="item-name"]')
    PLUS_BUTTON = (By.XPATH, "//*[contains(text(), 'Gourmet Gold Savoury Cake Meat 8 x 85g (680g)')]/ancestor::*[@class='product_box_Small']/following-sibling::*[@class='product-button-container']/child::*[@class='plusbutton']")
    DELIVERY_WINDOW = (By.XPATH, '//div[@class="currentWindow"]')
    DELIVERY_DAY_SELECTOR = (By.ID, "delivery-day-selector")
    TIME_START = (By.ID, "delivery-time-start")
    TIME_END = (By.ID, "delivery-time-end")
    CONFIRM_SLOT = (By.ID, "confirm-delivery-window")
    CHECKOUT_BTN = (By.XPATH, '(//input[@value="Checkout"])[2]')
    SPINNER = (By.XPATH, '//*[contains(@class,"checkoutSpinner")]')

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_BAR, product_name)
        self.click(self.SEARCH_ICON)

    def add_cake(self):
        self.click(self.ADD_CAKE)
        #self.driver.save_screenshot("C:\\Proveway\pythonProject3\screenshots\screenshot_gourmet.png")
        assert self.get_element(self.SIDE_PANEL_ITEM).text == "Gourmet Gold Savoury Cake Meat 8 x 85g (680g)"

    def increase_quantity(self, count):
        for _ in range(count):
            self.click(self.PLUS_BUTTON)

    def select_delivery_slot(self, day, time):
        self.click(self.DELIVERY_WINDOW)
        select = Select(self.driver.find_element(*self.DELIVERY_DAY_SELECTOR))
        select.select_by_visible_text(day)
        self.clear_and_send_keys(self.TIME_START, time)
        self.get_element(self.TIME_END)

    def confirm_delivery_slot(self):
        self.js_click(self.CONFIRM_SLOT)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)