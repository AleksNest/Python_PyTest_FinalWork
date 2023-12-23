#Расширение BasePage дополлнительными операциями функции по управлению элементами страниц ( более детальные операции, которые могут меняться
# локаторы хранятся

import logging
from baseApp import BasePage
from selenium.webdriver.common.by import By
import yaml


# класс локаторов, которые берутся из файла locators.yaml
class TestSearchLocators:
    ids = dict()
    with open('./locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])

# класс для работы с Web страницами
class OperationsHelper(BasePage):       # наследуется от класса BasePage

    #ENTER TEXT METHODS

    # метод для ввода значений в форму с обработкой ошибок
    def enter_text_into_field(self, locator, word, description=None):

        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator)
        logging.debug(f'Send {word} of element {element_name}')
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True


    def enter_login(self, word):                # метод вводо логина в поле логина
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description='login')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description='pass')

    def enter_title_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE_POST"], word, description='title post')

    def enter_description_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION_POST"], word, description='description post')

    def enter_name_contuct_page(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NAME_CONTACTPAGE"], word, description='name contact')

    def enter_content_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_POST"], word, description='content post')

    def enter_email_contuct_page(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_EMAIL_CONTACTPAGE"], word, description='email')

    def enter_content_contuct_page(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_CONTACTPAGE"], word, description='content contact')


   # ENTER CLICK METHODS

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("exception with click")
            return  False
        logging.debug(f'Click {element_name} button')
        return True

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description='login button')

    def click_add_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ADD_POST_BTN"], description='add post button')

    def click_save_post(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_POST_BTN"], description='save post button')

    def click_contuct_buttton(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description='connact button')

    def click_contuct_us_buttton(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTUCT_US_BTN"], description='contact us button')

    #   GET TEXT FROM ELEMENT METHODS
    def get_text_from_element(self, locator, description=None):
        field = self.find_element(locator, time=5)
        if description:
            element_name = description
        else:
            element_name = locator
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {field}')
        return text

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description='get text hello user')

    def get_hello_user(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_SUCCESS_FIELD"], description='get text hello user')

    def get_title_post(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_OUTPUT_TITLE_POST"], description='get text title postr')


    # GET TEXT IN  ALERT
    def get_alert(self):
        try:
            text = self.get_alert_text()
        except:
            logging.exception(f'Exception with alert')
            return None
        logging.info(f' We find text {text} after click contact button')
        return text





