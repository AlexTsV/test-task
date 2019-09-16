from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM) is True, 'Login form does not exist'

    def should_be_login_through_facebook_button(self):
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_THROUGH_FACEBOOK_BUTTON) is True, 'Login through Facebook button does not exist'

    def should_be_login_button(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON) is True, 'Login button does not exist'

    def should_be_reset_password_link(self):
        assert self.browser.find_element(
            *LoginPageLocators.RESET_PASSWORD_LINK) is True, 'Reset password link does not exist'

    def should_be_sign_up_button(self):
        assert self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON) is True, 'Sign up button does not exist'

    def should_be_login_phone_tooltip(self):
        login_form_email = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL)
        login_form_email.click()
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM_TOOLTIP) is True, 'Tooltip does not exist'

    def  