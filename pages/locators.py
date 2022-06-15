from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_ADDRESS = (By.XPATH, "//input[@name='registration-email']")
    REGISTER_PASSWORD = (By.XPATH, "//input[@name='registration-password1']")
    REGISTER_PASSWORD_CONFIRM = (By.XPATH, "//input[@name='registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADDED_PRODUCT = (By.CSS_SELECTOR, "div.alert:nth-child(1) div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    CART_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")

class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    SOME_ITEM = (By.CSS_SELECTOR, "div.basket-items")