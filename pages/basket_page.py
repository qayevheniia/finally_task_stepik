from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def cant_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_LINK ), \
            "Item is presented in the basket, but should not be"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "The basket isn't empty"




