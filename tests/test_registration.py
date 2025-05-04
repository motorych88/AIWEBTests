import allure
from core.BaseTests import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPagesHelper
from pages.RegistrationPage import RegistrationPagesHelper

BASE_URL = 'https://ok.ru'


@allure.feature('Тесты формы регистрации')
class TestRegistration:
    @allure.title('Регистрация с рандомной страной')
    def test_registration_random_country(self, browser):
        BasePage(browser).get_url(BASE_URL)
        login_page = LoginPagesHelper(browser)
        login_page.click_registration()
        registration_page = RegistrationPagesHelper(browser)
        registration_page.select_random_country()
        expected_code = registration_page.select_random_country()
        actual_code = registration_page.get_value_phone()
        with allure.step('Проверяем что код страны совпадает с кодом в поле ввода телефона'):
            assert expected_code == actual_code

