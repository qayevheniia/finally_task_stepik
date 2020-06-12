from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTRATION = (By.CSS_SELECTOR,"#id_registration-email")
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR,"#id_registration-password1")
    PASSWORD_REGISTRATION2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REG = (By.CSS_SELECTOR,"#register_form > button")

class ProductPageLocators():
    Add_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    RIGHT_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div>strong')
    Name_BOOK = (By.CSS_SELECTOR, ' div.col-sm-6.product_main > h1')
    PRICE_BOOK = (By.CSS_SELECTOR, 'p.price_color')
    RIGHT_AMOUNT = (By.CSS_SELECTOR, '.alertinner > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_BASKET = (By.CSS_SELECTOR, ".btn-group>a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ITEMS_LINK = (By.CSS_SELECTOR, ".availability.instock")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner> p")


