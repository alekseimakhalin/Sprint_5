"""
Конфигурация для pytest
"""

import sys
import os

# Добавляем корневую директорию в PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from data.test_data import BASE_URL


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для создания драйвера браузера
    """
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Используем webdriver-manager для автоматической загрузки драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(BASE_URL)
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