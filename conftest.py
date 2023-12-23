import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from webdriver_manager.core import manager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from check_api_post import get_login



with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


# выбор и инициализация на выбор из yaml драйвера браузера на всю ссессию тестов
@pytest.fixture(scope='session')
def browser():
    if browser == "firefox":
        service = Service(
            executable_path=GeckoDriverManager().install())  # установка драйвера при автоматической установки
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)  # свойство класса
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver    # в первый проход всех тестов инициализация драйвера
    driver.quit()   # полсе прохождения всех тестов выполнение закрытие браузера


# получения токена для API теста
@pytest.fixture()
def token():
    return get_login()
