from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    Add_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    RIGHT_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div>strong')
    Name_BOOK = (By.CSS_SELECTOR, ' div.col-sm-6.product_main > h1')
    PRICE_BOOK = (By.CSS_SELECTOR, 'p.price_color')
    RIGHT_AMOUNT = (By.CSS_SELECTOR, '.alertinner > p > strong')


