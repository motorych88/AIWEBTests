import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPagesLocators:
    TAB_QR = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    TAB_MAIL = (By.XPATH, '//*[@data-l="t,login_tab"]')

    LOGIN_FIELD_EMAIL = (By.ID, 'field_email')
    LOGIN_FIELD_PASSWORD = (By.ID, 'field_password')

    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    BUTTON_LOGIN_QR = (By.XPATH, '//*[@data-l="t,get_qr"]')

    BUTTON_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    BUTTON_MAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    BUTTON_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')

    CANT_LOGIN = (By.XPATH, '//*[@data-l="t,restore"]')
    BUTTON_REGISTRATION = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide" and @data-l="t,register"]')

    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')


class LoginPagesHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPagesLocators.TAB_QR)
        self.find_element(LoginPagesLocators.TAB_MAIL)
        self.find_element(LoginPagesLocators.LOGIN_FIELD_EMAIL)
        self.find_element(LoginPagesLocators.LOGIN_FIELD_PASSWORD)
        self.find_element(LoginPagesLocators.LOGIN_BUTTON)
        self.find_element(LoginPagesLocators.BUTTON_LOGIN_QR)
        self.find_element(LoginPagesLocators.BUTTON_VK)
        self.find_element(LoginPagesLocators.BUTTON_MAIL)
        self.find_element(LoginPagesLocators.BUTTON_YANDEX)
        self.find_element(LoginPagesLocators.CANT_LOGIN)
        self.find_element(LoginPagesLocators.BUTTON_REGISTRATION)

    @allure.step('клик на кнопку авторизации')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPagesLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPagesLocators.ERROR_TEXT).text

    @allure.step('ввод текста в поле ввода почты')
    def text_login(self):
        self.find_element(LoginPagesLocators.LOGIN_FIELD_EMAIL).send_keys('Михаил')

    @allure.step('ввод текста в поле ввода пароля')
    def text_password(self):
        self.find_element(LoginPagesLocators.LOGIN_FIELD_PASSWORD).send_keys('Задов')
