from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def message(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_MESSAGE).text

    def message_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_MESSAGE_NAME).text

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    def should_add_product_to_backet(self):
        self.add_to_basket()
        self.should_be_message()
        self.should_be_price()

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()


    def should_be_message(self):
        time.sleep(2)
        assert self.product_name() == self.message_name(), 'Product name incorrect in success add messages'

    def should_be_price(self):
        assert self.product_price() in self.message(), 'Product price incorrect in success add messages'
