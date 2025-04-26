from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPagesLocators:
    LOGIN_FIELD_EMAIL = (By.ID, 'field_email')
    LOGIN_FIELD_PASSWORD = (By.ID, 'field_password')
    LOGIN_FIELD_QR = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD_MAIL = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_FIELD_BOTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_FIELD_BOTTON_QR = (By.XPATH, '//*[@data-l="t,get_qr"]')
    LOGIN_FIELD_BOTTON_VK = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    LOGIN_FIELD_BOTTON_MAIL = (By.XPATH, 'class="i ic social-icon __s __mailru"')
    LOGIN_FIELD_BOTTON_YANDEX = (By.XPATH, 'class="i ic social-icon __s __yandex"')
    LOGIN_FIELD_DONT_INSITE = (By.XPATH, '//*[@data-l="t,restore"]')
    LOGIN_FIELD_REGISTRATION = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]')




class LoginPagesHelper(BasePage):
    pass


