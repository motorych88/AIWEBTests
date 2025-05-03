import allure
from core.BaseTests import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPagesHelper, HelpPagesLocators

BASE_URL = 'https://ok.ru/help'

@allure.feature('Тесты формы помощи')
class TestHelp:
    @allure.title('Проверка скролла')
    def test_help(self, browser):
        BasePage(browser).get_url(BASE_URL)
        help_page = HelpPagesHelper(browser)
        help_page.scroll_item(HelpPagesLocators.ADVERTISEMENT_CABINET)


