import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePageLocators:
    LOGO_OK = (By.ID, 'nohook_logo_link')
    SEARCH_FIELD = (By.XPATH, '//*[@placeholder="Поиск в ОК"]')
    TOOLBAR = (By.XPATH, '//*[@data-l="t,vk_ecosystem"]')
    MORE_BUTTON = (By.XPATH, '//*[@data-l="t,more"]')


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверка загрузки страницы'):
            self.attach_screenshot()
        self.find_element(BasePageLocators.LOGO_OK)
        self.find_element(BasePageLocators.SEARCH_FIELD)
        self.find_element(BasePageLocators.TOOLBAR)


    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator),
                                                      message=f'Не удалось найти элемент {locator}')

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator),
                                                      message=f'Не удалось найти элементы {locator}')

    @allure.step(f'Открытие страницы')
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)

    @allure.step('клик на кнопку тулбара')
    def click_vk_ecosystem(self):
        self.find_element(BasePageLocators.TOOLBAR).click()

    @allure.step('клик на кнопку "Еще" в тулбаре')
    def click_vk_ecosystem_more(self):
        self.find_element(BasePageLocators.MORE_BUTTON).click()

    @allure.step('Получение хеша страницы')
    def get_windows_id(self, index):
        return self.driver.window_handles[index]

    @allure.step('Переход на страницу')
    def switch_window(self, window_id):
        self.driver.switch_to.window(window_id)

