"""
Тесты регистрации
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import RegistrationLocators
from utils.helpers import generate_name, generate_login, generate_short_password
from data.test_data import BASE_URL


class TestRegistration:
    """Класс для тестирования регистрации"""

    def test_successful_registration(self, driver, registered_user):
        """
        Проверка успешной регистрации
        """
        driver.get(f"{BASE_URL}register")

        wait = WebDriverWait(driver, 15)

        name_input = wait.until(EC.element_to_be_clickable(RegistrationLocators.NAME_INPUT))
        name_input.send_keys(registered_user['name'])

        email_input = driver.find_element(*RegistrationLocators.EMAIL_INPUT)
        email_input.send_keys(registered_user['email'])

        password_input = driver.find_element(*RegistrationLocators.PASSWORD_INPUT)
        password_input.send_keys(registered_user['password'])

        register_button = driver.find_element(*RegistrationLocators.REGISTER_BUTTON)
        register_button.click()

        wait.until(EC.url_contains("login"))
        assert "login" in driver.current_url

    def test_registration_with_short_password_error(self, driver):
        """
        Проверка ошибки при регистрации с коротким паролем
        """
        driver.get(f"{BASE_URL}register")

        wait = WebDriverWait(driver, 15)

        name_input = wait.until(EC.element_to_be_clickable(RegistrationLocators.NAME_INPUT))
        name_input.send_keys(generate_name())

        email_input = driver.find_element(*RegistrationLocators.EMAIL_INPUT)
        email_input.send_keys(generate_login())

        password_input = driver.find_element(*RegistrationLocators.PASSWORD_INPUT)
        short_password = generate_short_password()
        password_input.send_keys(short_password)

        register_button = driver.find_element(*RegistrationLocators.REGISTER_BUTTON)
        register_button.click()

        error_message = wait.until(EC.visibility_of_element_located(RegistrationLocators.PASSWORD_ERROR))
        assert "Некорректный пароль" in error_message.text
