from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT)
        assert product_name.text == added_product_name.text, \
            f"Product name is incorrect, must be {product_name.text}, now {added_product_name.text}"

    def should_be_correct_adding_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        cart_product_price = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        assert product_price.text == cart_product_price.text, \
            f"Product price is incorrect, must be {product_price.text}, now {cart_product_price.text}"

    def should_be_success_message_name_product(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT), "Success message with name is not present"

    def should_be_success_message_price_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRICE), "Success message with price is not present"
