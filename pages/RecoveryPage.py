import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RecoveryPagesLocators:
    PHONE_BUTTON = (By.XPATH, '//*[@data-l="t,phone"]')
    EMAIL_BUTTON = (By.XPATH, '//*[@data-l="t,email"]')
    ICON_QR = (By.XPATH, '//*[@class="qr_code_info"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')


class RecoveryPagesHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверка загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RecoveryPagesLocators.PHONE_BUTTON)
        self.find_element(RecoveryPagesLocators.EMAIL_BUTTON)
        self.find_element(RecoveryPagesLocators.ICON_QR)
        self.find_element(RecoveryPagesLocators.SUPPORT_BUTTON)

    @allure.step('клик на кнопку телефона')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(RecoveryPagesLocators.PHONE_BUTTON).click()

    @allure.step('клик на кнопку почты')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(RecoveryPagesLocators.EMAIL_BUTTON).click()