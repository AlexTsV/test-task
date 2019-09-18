from pages.base_page import BasePage
from pages.locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):

    def should_be_reset_password_page_url(self):
        assert 'signin/reset' in self.browser.current_url, 'not reset password page'

    def should_be_email_field(self):
        assert self.browser.find_element(*ResetPasswordPageLocators.EMAIL_FORM_FIELD), 'email field does not exist'

    def click_email_field(self):
        email_field = self.browser.find_element(*ResetPasswordPageLocators.EMAIL_FORM_FIELD)
        email_field.click()

    def should_be_phone_tooltip(self):
        assert self.browser.find_element(*ResetPasswordPageLocators.PHONE_TOOLTIP), 'phone tooltip does not exist'

    def should_be_reset_password_button(self):
        assert self.browser.find_element(
            *ResetPasswordPageLocators.RESET_PASSWORD_BUTTON), 'reset password button does not exist'
