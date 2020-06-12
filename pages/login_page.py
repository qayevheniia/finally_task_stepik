from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()



    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "Login register is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION)
        password_field.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION2)
        password_field2.send_keys(password)
        link = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        link.click()



