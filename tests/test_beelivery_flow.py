import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestBeeliveryFlow:
    def test_beelivery_order_flow(self):
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        product = ProductPage(self.driver)
        checkout = CheckoutPage(self.driver)

        login.login("rishithaagan070890@gmail.com", "Rishitha@1812")
        home.enter_postcode_and_select_groceries("SW1A 1AA")
        home.place_order()
        product.search_product("cake")
        product.add_cake()
        product.increase_quantity(2)
        product.select_delivery_slot("Sunday, 04/20", "09:50AM")
        product.confirm_delivery_slot()
        product.proceed_to_checkout()
        checkout.verify_checkout_summary()