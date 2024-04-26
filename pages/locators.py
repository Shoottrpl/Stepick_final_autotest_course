from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_IN_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color')
    SUCCESS_ADD_MESSAGE = (By.CSS_SELECTOR, '#messages .alert')
    SUCCESS_ADD_MESSAGE_NAME = (By.CSS_SELECTOR, '#messages strong')

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, 'basket-items')
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')


