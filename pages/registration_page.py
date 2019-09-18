from pages.base_page import BasePage
from pages.locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def should_be_back_to_main_button(self):
        assert self.browser.find_element(*RegistrationPageLocators.BACK_MAIN), 'Back to main page link does not present'

    def should_be_company_name_field(self):
        assert self.browser.find_element(
            *RegistrationPageLocators.COMPANY_NAME_FIELD), 'company name field does not exist'

    def should_be_user_name_field(self):
        assert self.browser.find_element(
            *RegistrationPageLocators.CLIENT_NAME_FIELD), 'client name field does not exist'

    def should_be_phone_field(self):
        assert self.browser.find_element(*RegistrationPageLocators.PHONE_FIELD), 'phone field does not exist'

    def should_be_email_field(self):
        assert self.browser.find_element(*RegistrationPageLocators.EMAIL_FIELD), 'email field does not exist'

    def should_be_promo_code_link(self):
        assert self.browser.find_element(*RegistrationPageLocators.PROMO_CODE_LINK), 'promo code link does not exist'

    def click_promo_code_link(self):
        promo_code_link = self.browser.find_element(*RegistrationPageLocators.PROMO_CODE_LINK)
        promo_code_link.click()

    def should_be_promo_code_field(self):
        assert self.browser.find_element(*RegistrationPageLocators.PROMO_CODE_FIELD), 'promo code field does not exist'

    def should_be_checkbox(self):
        assert self.browser.find_element(*RegistrationPageLocators.CHECKBOX), 'checkbox does not exist'

    def should_be_user_agreement_link(self):
        assert self.browser.find_element(
            *RegistrationPageLocators.USER_AGREEMENT_LINK), 'user agreement link does not exist'

    def should_be_get_access_button(self):
        assert self.browser.find_element(
            *RegistrationPageLocators.GET_ACCESS_BUTTON), 'Get access button does not exist'

    def should_be_login_button(self):
        assert self.browser.find_element(*RegistrationPageLocators.LOGIN_BUTTON), 'login button does not exist'
