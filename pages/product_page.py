from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        self.should_be_add_to_basket_btn()
        self.adding_item_params = self.find_adding_item_name_and_cost()
        self.can_add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_alert_added_selected_item()
        self.should_be_equal_item_cost_and_basket_cost_after_adding_item()
          
    def guest_cant_see_success_message(self):
        self.should_not_be_success_message()
    
    def success_message_disappeared(self):
        self.should_dissapear_success_message()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "ADD_TO_BASKET_BTN is not presented"

    def find_adding_item_name_and_cost(self):
        adding_item_name = self.browser.find_element(*ProductPageLocators.ADDING_ITEM_NAME).text
        adding_item_cost = self.browser.find_element(*ProductPageLocators.ADDING_ITEM_COST).text
        adding_item_params = {'name':adding_item_name, 'cost':adding_item_cost}
        return adding_item_params 

    def can_add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()
    
    def should_be_alert_added_selected_item(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_ADDED_ITEM_ALERT).text == self.adding_item_params['name'], \
            "ADDED ITEM NAME AND ITEM NAME IN ALERT AFTER ADDING DONT MATCH"

    def should_be_equal_item_cost_and_basket_cost_after_adding_item(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_COST_ALERT).text == self.adding_item_params['cost'], \
            "ADDED ITEM COST AND BASKET TOTAL COST IN ALERT AFTER ADDING DONT MATCH"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_ITEM_ALERT), \
        "Success message is presented, but should not be"

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADDED_ITEM_ALERT), \
        "Success message hasn't dissapeared"