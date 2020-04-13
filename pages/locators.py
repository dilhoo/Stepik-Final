from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group>.btn.btn-default[href*="basket"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

    REGISTRATION_EMAIL_FORM = (By.CSS_SELECTOR,'[name="registration-email"]')
    REGISTRATION_PASSWORD1_FORM = (By.CSS_SELECTOR,'[name="registration-password1"]')
    REGISTRATION_PASSWORD2_FORM = (By.CSS_SELECTOR,'[name="registration-password2"]')
    SUBMIT_REGISTRATION_BTN = (By.CSS_SELECTOR,'[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_ADDED_ITEM_ALERT = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner>strong") 
    BASKET_TOTAL_COST_ALERT = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>.alertinner>p>strong") 
    ADDING_ITEM_NAME = (By.CSS_SELECTOR, ".product_main>h1") 
    ADDING_ITEM_COST = (By.CSS_SELECTOR, ".product_main>.price_color")

class BasketPageLocators():
    BASKET_ITEMS_DIV = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY_TEXT_DIV = (By.CSS_SELECTOR, "#content_inner")