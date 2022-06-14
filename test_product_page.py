import time
import pytest
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    #url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_name_product()
    page.should_be_success_message_price_in_cart()
    page.should_be_correct_product_name()
    page.should_be_correct_adding_product_price()


