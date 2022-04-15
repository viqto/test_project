from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Wrong page!!!"

    def should_be_login_form(self):
        assert LoginPageLocators.LOGIN_FORM, 'No login form!!!'

    def should_be_register_form(self):
        assert LoginPageLocators.REGISTER_FORM, 'No register form!!!'
