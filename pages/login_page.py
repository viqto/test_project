from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self):
        generated_email = str(time.time()) + "@fakemail.org"
        user_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        user_email.send_keys(generated_email)
        print(user_email)
        user_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        user_password.send_keys("xfMAT3C?oNbC")
        print(user_password)
        repeat_password = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        repeat_password.send_keys("xfMAT3C?oNbC")
        print(repeat_password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Wrong page!!!"

    def should_be_login_form(self):
        self.browser.find_element(LoginPageLocators.LOGIN_FORM)
        assert LoginPageLocators.LOGIN_FORM, 'No login form!!!'

    def should_be_register_form(self):
        self.browser.find_element(LoginPageLocators.REGISTER_FORM)
        assert LoginPageLocators.REGISTER_FORM, 'No register form!!!'
