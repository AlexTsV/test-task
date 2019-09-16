from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#signin_form')
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, '.email')
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, '.pass')
    LOGIN_THROUGH_FACEBOOK_BUTTON = (By.CSS_SELECTOR, 'a.btn:nth-child(4)')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a.btn:nth-child(5)')
    RESET_PASSWORD_LINK = (By.CSS_SELECTOR, 'p.text-muted:nth-child(6) > a:nth-child(1) > small:nth-child(1)')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'a.btn:nth-child(8)')
    LOGIN_FORM_TOOLTIP = (By.CLASS_NAME, 'tooltip.fade.right.in')
