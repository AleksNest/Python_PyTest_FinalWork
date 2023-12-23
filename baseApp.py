# базовые функции по управлению элементами страницы сайта, которые не меняются : найти элемент страницы,
# получить свойства элемента, переход на страницу по url

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import yaml
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    url = testdata["address"]



class BasePage:

# конструктор инициализации драйвера браузера
    def __init__(self, driver):
        self.driver = driver
        self.base_url = url


# метод поиска элемента страницы по локатору
    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
        except:
            logging.exception(('Find element exception'))
            element = None
        return element



# метод получения свойства элемента страницы по локатору
    def get_element_property(self, locator, property):       # получение свойства элемента (например получение цвета кнопки)
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)          # получение свойства у элемента, если свойство есть
        else:
            logging.exception(f'Property {property} not found in element with {locator}')
            return None



# метод открытия главной страницы
    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open site')
            start_browsing = None
        return start_browsing


# метод возвращения текста перехвата alert страницы
    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text


