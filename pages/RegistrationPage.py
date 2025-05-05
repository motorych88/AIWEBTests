import allure
import random
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class RegistrationPagesLocators:
    FIELD_PHONE = (By.ID, 'field_phone')
    COUNTRY_LIST = (By.XPATH, '//div[@data-l="t,country"]')
    COUNTRY_ITEM = (By.XPATH, '//div[@class="country-select_code"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')


class RegistrationPagesHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверка загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RegistrationPagesLocators.FIELD_PHONE)
        self.find_element(RegistrationPagesLocators.COUNTRY_LIST)
        self.find_element(RegistrationPagesLocators.SUBMIT_BUTTON)
        self.find_element(RegistrationPagesLocators.SUPPORT_BUTTON)

    @allure.step('клик на выбор страны')
    def select_random_country(self):
        random_number = random.randint(0, 212)
        self.find_element(RegistrationPagesLocators.COUNTRY_LIST).click()
        country_item = self.find_elements(RegistrationPagesLocators.COUNTRY_ITEM)
        country_code = country_item[random_number].get_attribute('text')
        country_item[random_number].click()
        return country_code

    @allure.step('поиск кода страны в поле')
    def get_value_phone(self):
        return self.find_element(RegistrationPagesLocators.FIELD_PHONE).get_attribute('text')
