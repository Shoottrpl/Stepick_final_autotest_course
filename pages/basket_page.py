from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_on_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is presented, but should not be"

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "Empty message is not presented, but should be"




