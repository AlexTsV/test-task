from selenium.webdriver.common.by import By


class LoginPageLocators:
    BACK_MAIN = (By.CSS_SELECTOR, '.back_main')
    LOGIN_FORM = (By.CSS_SELECTOR, '#signin_form')
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, '.email')
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, '.pass')
    LOGIN_THROUGH_FACEBOOK_BUTTON = (By.CSS_SELECTOR, 'a.btn.btn-success')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.btn:nth-child(5)')
    RESET_PASSWORD_LINK = (By.CSS_SELECTOR, '.text-muted.text-center>a[href]')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'a.btn:nth-child(8)')
    LOGIN_FORM_TOOLTIP = (By.CLASS_NAME, 'tooltip.fade.right.in')
    LOGIN_BEAUTY_ID = (By.CSS_SELECTOR, 'a.btn.btn-block.btn-white.btn-sm.m-b')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '.btn.btn-sm.btn-white.btn-block[href="/add"]')


class FacebookLoginWithCookiePageLocators:
    EDIT_BUTTON = (By.CSS_SELECTOR, '#u_0_5')
    CONTINUE_AS_BUTTON = (By.CSS_SELECTOR, '._1fm0')
    CANCEL_BUTTON = (By.CSS_SELECTOR, '#u_0_0')
    DROPDOWN_BUTTON = (By.CSS_SELECTOR, '#u_0_3')
    CHANGE_USER_BUTTON = (By.CSS_SELECTOR, '._54nc')
    CONDITIONALS_LINK = (By.CSS_SELECTOR, 'a._58xj:nth-child(1)')
    PRIVACY_POLICY = (By.CSS_SELECTOR, 'a._58xj:nth-child(3)')
    USER_PRESENT_INFO_BOX = (By.CSS_SELECTOR, '._bk9')
    TOGGLE_EMAIL_BUTTON = (By.CSS_SELECTOR, '._kv1')
    BACK_TO_MAIN_BUTTON = (By.CSS_SELECTOR, 'span._5kx5:nth-child(2)')


class ResetPasswordPageLocators:
    BACK_MAIN = (By.CSS_SELECTOR, '.back_main')
    EMAIL_FORM_FIELD = (By.CSS_SELECTOR, '.email')
    RESET_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a.btn:nth-child(4)')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.btn:nth-child(6)')
    PHONE_TOOLTIP = (By.CSS_SELECTOR, '.tooltip-inner')


class RegistrationPageLocators:
    BACK_MAIN = (By.CSS_SELECTOR, '.back_main')
    COMPANY_NAME_FIELD = (By.CSS_SELECTOR, 'input.form-control[data-register-company-title]')
    CLIENT_NAME_FIELD = (By.CSS_SELECTOR, 'input.form-control[name="name"]')
    PHONE_FIELD = (By.CSS_SELECTOR, '#landing_phone')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#email')
    PROMO_CODE_LINK = (By.CSS_SELECTOR, '.enter_promo')
    PROMO_CODE_FIELD = (By.CSS_SELECTOR, '#promo_code')
    CHECKBOX = (By.CSS_SELECTOR, '.checkbox > label:nth-child(1) > input:nth-child(1)')
    USER_AGREEMENT_LINK = (By.CSS_SELECTOR, '.checkbox > label:nth-child(1) > a:nth-child(2)')
    GET_ACCESS_BUTTON = (By.CSS_SELECTOR, 'button.btn:nth-child(10)')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.btn')
