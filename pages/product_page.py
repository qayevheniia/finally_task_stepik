from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):


    def should_be_same_name1(self):
        assert self.is_element_present(*ProductPageLocators.RIGHT_NAME), "The Name book in basket)  is not presented"


    def should_be_same_name2(self):
        assert self.is_element_present(*ProductPageLocators.Name_BOOK), "The name book in page is not presented"

    def should_have_the_same_name(self):
        assert self.browser.find_element(*ProductPageLocators.RIGHT_NAME).text == self.browser.find_element(*ProductPageLocators.Name_BOOK).text, "Names are different"


    def can_add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.Add_BASKET)
        link.click()

    def should_have_the_same_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text == self.browser.find_element(*ProductPageLocators.RIGHT_AMOUNT).text, "Prices are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    #метод, который проверяет, что элемент не появляется на странице в течение заданного времени (часть Base Object)


    def should_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Succes message isn't disappeared"