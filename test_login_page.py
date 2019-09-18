import pytest
import pickle
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from pages.facebook_login_with_cookie_page import FacebookLoginPage
from pages.registration_page import RegistrationPage

link = 'https://www.yclients.com/signin'


def test_guest_can_login_through_facebook(browser):
    cookie = {'name': 'c_user', 'value': '100023356991416', 'domain': 'www.facebook.com'}
    browser.add_cookie(cookie)
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_through_facebook_button()
    page.login_through_facebook()
    page.should_be_facebook_login_window()
    page.switch_to_new_window()
    page = FacebookLoginPage(browser, link)
    page.should_be_login_as_button()
    page.auth_through_facebook()
    page.close_current_window()


def test_guest_can_login(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_email_field()
    page.should_be_password_field()
    page.click_to_email_field()
    page.should_be_login_phone_tooltip()


@pytest.mark.xfail(reason='only for ru interface')
def test_guest_can_login_through_beauty_id(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_beauty_id_login()
    page.click_beauty_id_button()
    page.should_be_beauty_url()


def test_guest_can_reset_password(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_reset_password_link()
    page.click_reset_password_button()
    page = ResetPasswordPage(browser, link)
    page.should_be_reset_password_page_url()
    page.should_be_email_field()
    page.click_email_field()
    page.should_be_phone_tooltip()
    page.should_be_reset_password_button()


def test_guest_can_register(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_registration_button()
    page.click_registration_button()
    page = RegistrationPage(browser, link)
    page.should_be_company_name_field()
    page.should_be_user_name_field()
    page.should_be_phone_field()
    page.should_be_email_field()
    page.should_be_promo_code_link()
    page.click_promo_code_link()
    page.should_be_promo_code_field()
    page.should_be_checkbox()
    page.should_be_user_agreement_link()
    page.should_be_get_access_button()


@pytest.mark.xfail(reason='does not redirect to the main page')
def test_back_to_main_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_back_to_main_link()
    page.click_back_to_main_link()
    page.should_be_main_page_url()
