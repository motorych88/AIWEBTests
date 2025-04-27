from core.BaseTests import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPagesHelper

BASE_URL = 'https://ok.ru'
EMPTY_LOGIN_ERROR = 'Введите логин'
EMPTY_PASSWORD_ERROR = 'Введите пароль'

def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPagesHelper(browser)
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_LOGIN_ERROR


def test_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPagesHelper(browser)
    login_page.text_login()
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_PASSWORD_ERROR


def test_empty_login(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPagesHelper(browser)
    login_page.text_password()
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_LOGIN_ERROR
