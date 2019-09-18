from pages.base_page import BasePage
from pages.locators import FacebookLoginWithCookiePageLocators


class FacebookLoginPage(BasePage):
    def should_be_login_as_button(self):
        assert self.browser.find_element(
            *FacebookLoginWithCookiePageLocators.CONTINUE_AS_BUTTON) is True, 'Login as button does not exist'

    def auth_through_facebook(self):
        auth_through_facebook = self.browser.find_element(*FacebookLoginWithCookiePageLocators.CONTINUE_AS_BUTTON)
        auth_through_facebook.click()
        assert 'https://www.yclients.com/' == self.browser.current_url, 'is not current url'
