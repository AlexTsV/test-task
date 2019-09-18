from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_back_to_main_link(self):
        assert self.browser.find_element(*LoginPageLocators.BACK_MAIN), 'Back to main link does not present'

    def click_back_to_main_link(self):
        back_to_main_link = self.browser.find_element(*LoginPageLocators.BACK_MAIN)
        back_to_main_link.click()

    def should_be_main_page_url(self):
        assert 'https://yclients.com' == self.browser.current_url, 'Not main page url'

    def should_be_login_through_facebook_button(self):
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_THROUGH_FACEBOOK_BUTTON), 'Login through Facebook button does not exist'

    def should_be_email_field(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL), 'Email field does not present'

    def click_to_email_field(self):
        email_field = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL)
        email_field.click()

    def should_be_password_field(self):
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_FORM_PASSWORD), 'Password field does not present'

    def should_be_login_button(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON), 'Login button does not exist'

    def should_be_reset_password_link(self):
        assert self.browser.find_element(
            *LoginPageLocators.RESET_PASSWORD_LINK), 'Reset password link does not exist'

    def should_be_sign_up_button(self):
        assert self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON), 'Sign up button does not exist'

    def should_be_login_phone_tooltip(self):
        login_form_email = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL)
        login_form_email.click()
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM_TOOLTIP), 'Tooltip does not exist'

    def should_be_beauty_id_login(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_BEAUTY_ID), 'Login with beauty id'

    def click_beauty_id_button(self):
        enter_beaty_id_button = self.browser.find_element(*LoginPageLocators.LOGIN_BEAUTY_ID)
        enter_beaty_id_button.click()

    def should_be_beauty_url(self):
        assert 'beautyid.pro' in self.browser.current_url, 'Url is not beauty.pro'

    def is_not_beauty_id_present(self):
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_BEAUTY_ID)
        except NoSuchElementException:
            return True

    def login_through_facebook(self):
        facebook_login = self.browser.find_element(*LoginPageLocators.LOGIN_THROUGH_FACEBOOK_BUTTON)
        facebook_login.click()

    def should_be_facebook_login_window(self):
        try:
            new_window = self.browser.window_handles[1]
            new_window = True
        except IndexError:
            new_window = False
        assert new_window is True, 'Facebook login popup window does not exist'

    def should_be_forget_password(self):
        assert self.browser.find_element(
            *LoginPageLocators.RESET_PASSWORD_LINK), 'Reset password link does not exist'

    def click_reset_password_button(self):
        reset_password = self.browser.find_element(*LoginPageLocators.RESET_PASSWORD_LINK)
        reset_password.click()

    def should_be_registration_button(self):
        assert self.browser.find_element(
            *LoginPageLocators.REGISTRATION_BUTTON), 'Registration button does not exist'

    def click_registration_button(self):
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

    def should_be_registration_facebook_page(self):
        assert 'https://www.facebook.com/login.php' in self.browser.current_url, 'Not facebook registration page'
