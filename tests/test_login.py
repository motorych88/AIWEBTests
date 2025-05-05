import allure
from core.BaseTests import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPagesHelper

BASE_URL = 'https://ok.ru'
EMPTY_LOGIN_ERROR = 'Введите логин'
EMPTY_PASSWORD_ERROR = 'Введите пароль'
LOGIN = 'login'
PASSWORD = 'password'


@allure.feature('Тесты формы авторизации')
class TestLogin:
    @allure.title('Попытка авторизации с пустыми полями')
    def test_empty_login_and_password(self, browser):
        BasePageHelper(browser).get_url(BASE_URL)
        login_page = LoginPagesHelper(browser)
        login_page.click_login()
        assert login_page.get_error_text() == EMPTY_LOGIN_ERROR

    @allure.title('Попытка авторизации с пустым полем пароля')
    def test_empty_password(self, browser):
        BasePageHelper(browser).get_url(BASE_URL)
        login_page = LoginPagesHelper(browser)
        login_page.text_login(LOGIN)
        login_page.click_login()
        assert login_page.get_error_text() == EMPTY_PASSWORD_ERROR

    @allure.title('Попытка авторизации с пустым полем почты')
    def test_empty_login(self, browser):
        BasePageHelper(browser).get_url(BASE_URL)
        login_page = LoginPagesHelper(browser)
        login_page.text_password(PASSWORD)
        login_page.click_login()
        assert login_page.get_error_text() == EMPTY_LOGIN_ERROR
