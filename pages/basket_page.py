from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        self.should_be_no_items_in_basket()
        self.should_be_basket_is_empty_text()

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_DIV), "FOUND ITEMS IN BASKET BUT SHOULDN'T"

    def should_be_basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT_DIV), "NO TEXT 'Your basket is empty' ON PAGE"
