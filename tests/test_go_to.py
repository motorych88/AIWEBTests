import allure
from core.BaseTests import browser
from pages.VKEcosystemPage import VKEcosystemHelper
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPagesHelper

BASE_URL = 'https://ok.ru'


@allure.feature('Проверка тулбара')
class TestGoToVKEcosystem:
    @allure.title('Проверка перехода в ВК экосистему')
    def test_help(self, browser):
        base_page = BasePageHelper(browser)
        base_page.get_url(BASE_URL)
        base_page.check_page()
        login_page = LoginPagesHelper(browser)
        current_window_id = login_page.get_windows_id(0)
        login_page.click_vk_ecosystem()
        login_page.click_vk_ecosystem_more()
        now_window_id = login_page.get_windows_id(1)
        login_page.switch_window(now_window_id)
        vk_ecosystem = VKEcosystemHelper(browser)
        vk_ecosystem.switch_window(current_window_id)
        LoginPagesHelper(browser)
