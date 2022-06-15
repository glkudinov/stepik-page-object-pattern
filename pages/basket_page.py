from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Some item in basket!"

    def is_basket_empty_negative(self):
        assert self.is_not_element_present(*BasketPageLocators.SOME_ITEM), "Your basket is empty"
