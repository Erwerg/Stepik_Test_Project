from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_form()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket url is not correct"

    def should_be_basket_form(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_FORM), "Basket form is not presented"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), "Basket is not empty"

    def should_be_empty_basket_message(self):
        assert "empty" in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text, \
            "Empty basket message is not presented"
