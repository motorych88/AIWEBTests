import allure
from core.BaseTests import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPagesHelper
from pages.RecoveryPage import RecoveryPagesHelper

BASE_URL = 'https://ok.ru'
LOGIN = 'login'
PASSWORD = 'password'


@allure.feature('Тесты восстановления пароля')
class TestRecovery:
    @allure.title('Переход к восстановлению после неудачной авторизации')
    def test_go_recovery(self, browser):
        BasePage(browser).get_url(BASE_URL)
        login_page = LoginPagesHelper(browser)
        login_page.text_login(LOGIN)
        for i in range(3):
            login_page.text_password(PASSWORD)
            login_page.click_login()
        login_page.click_recovery()
        RecoveryPagesHelper(browser)