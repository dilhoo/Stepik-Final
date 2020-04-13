from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current = self.browser.current_url
        should_be = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        assert  current == should_be, f"LOGIN URL DONT MATCH, page OPENED: {current} page SHOULD BE{should_be}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login FORM is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register FORM is not presented"

    def register_new_user(self, email, password):
        self.input_value(email, *LoginPageLocators.REGISTRATION_EMAIL_FORM)
        self.input_value(password, *LoginPageLocators.REGISTRATION_PASSWORD1_FORM)
        self.input_value(password, *LoginPageLocators.REGISTRATION_PASSWORD2_FORM)
        submit_btn = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION_BTN)
        submit_btn.click()
    