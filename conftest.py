"""
Конфигурация для pytest
"""

import sys
import os
import time

# Добавляем корневую директорию в PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from data.test_data import BASE_URL


def pytest_addoption(parser):
    """Добавляем опцию для выбора браузера"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )


@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для получения названия браузера"""
    return request.config.getoption("--browser")


@pytest.fixture(scope="function")
def driver(request):
    """
    Фикстура для создания драйвера браузера
    """
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")
        
        # Используем локальный chromedriver.exe (как в test_connection.py)
        chromedriver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

    elif browser_name == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=firefox_options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(BASE_URL)
    time.sleep(2)

    yield driver

    driver.quit()


@pytest.fixture
def registered_user():
    """
    Фикстура для создания зарегистрированного пользователя
    """
    from utils.helpers import generate_login, generate_name, generate_password

    email = generate_login()
    name = generate_name()
    password = generate_password()

    return {
        'email': email,
        'name': name,
        'password': password
    }
