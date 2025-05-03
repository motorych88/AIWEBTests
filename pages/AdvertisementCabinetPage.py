import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AdvertisementCabinetLocators:
    TITLE = (By.XPATH, '//span[text()="Рекламный кабинет"]')

class AdvertisementCabinetPagesHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверка загрузки страницы'):
            self.attach_screenshot()
        self.find_element(AdvertisementCabinetLocators.TITLE)