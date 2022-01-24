from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert-success > .alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[text()='View basket']")

class BasketPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, "#content_inner")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, "#basket_formset")
