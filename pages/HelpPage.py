import allure
from selenium.webdriver import ActionChains

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HelpPagesLocators:

    ACTUAL_TODAY = (By.XPATH, '//a[contains(@href, "segodnya-aktualno")]')
    REGISTRATION = (By.XPATH, '//a[contains(@href, "registraciya")]')
    MY_PROFILE = (By.XPATH, '//a[contains(@href, "moi-profil")]')
    COMMUNICATION = (By.XPATH, '//a[contains(@href, "obshchenie")]')
    ACCESS_PROFILE = (By.XPATH, '//a[contains(@href, "dostup-k-profilu")]')
    SECURITY = (By.XPATH, '//a[contains(@href, "bezopasnost")]')
    GROUP = (By.XPATH, '//a[contains(@href, "gruppy")]')
    PAY_FUNCTION = (By.XPATH, '//a[contains(@href, "platnye-funkcii")]')
    SPAM = (By.XPATH, '//a[contains(@href, "narusheniya-i-spam")]')
    GAME_APP = (By.XPATH, '//a[contains(@href, "igry-i-prilojeniya")]')
    OTHER_SERVICE = (By.XPATH,'//a[contains(@href, "drugie-servisy")]')
    USEFULL_INFORMATION = (By.XPATH, '//a[contains(@href, "poleznaya-informaciya")]')
    ADVERTISEMENT_CABINET = (By.XPATH, '//a[contains(@href, "reklamnyi-kabinet")]')

    SEARCH_FIELD = (By.XPATH, '//*[@type="search"]')


class HelpPagesHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверка загрузки страницы'):
            self.attach_screenshot()
        self.find_element(HelpPagesLocators.ACTUAL_TODAY)
        self.find_element(HelpPagesLocators.REGISTRATION)
        self.find_element(HelpPagesLocators.MY_PROFILE)
        self.find_element(HelpPagesLocators.COMMUNICATION)
        self.find_element(HelpPagesLocators.ACCESS_PROFILE)
        self.find_element(HelpPagesLocators.SECURITY)
        self.find_element(HelpPagesLocators.GROUP)
        self.find_element(HelpPagesLocators.PAY_FUNCTION)
        self.find_element(HelpPagesLocators.SPAM)
        self.find_element(HelpPagesLocators.GAME_APP)
        self.find_element(HelpPagesLocators.OTHER_SERVICE)
        self.find_element(HelpPagesLocators.USEFULL_INFORMATION)
        self.find_element(HelpPagesLocators.ADVERTISEMENT_CABINET)
        self.find_element(HelpPagesLocators.SEARCH_FIELD)


    def scroll_item(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()
