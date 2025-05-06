import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class VKEcosystemLocators:
    LOGO_VK = (By.XPATH, '//*[@class="Header_logo__tL_od"]')


class VKEcosystemHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверка загрузки страницы'):
            self.attach_screenshot()
        self.find_element(VKEcosystemLocators.LOGO_VK)
