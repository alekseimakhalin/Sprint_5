"""
Тесты выхода из аккаунта
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import MainPageLocators, PersonalAccountLocators, LoginLocators, RegistrationLocators
from data.test_data import BASE_URL


class TestLogout:
    """Класс для тестирования выхода из аккаунта"""

    def test_logout(self, driver, registered_user):
        """
        Проверка выхода по кнопке "Выйти" в личном кабинете
        """
        # Регистрируемся и входим
        self._register_and_login(driver, registered_user)

        wait = WebDriverWait(driver, 15)

        # Переходим в личный кабинет
        personal_account = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT))
        personal_account.click()

        # Ждем загрузки страницы личного кабинета
        wait.until(EC.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))

        # Кликаем по кнопке "Выйти"
        logout_button = wait.until(EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON))
        logout_button.click()

        # Проверяем, что открылась страница входа
        wait.until(EC.visibility_of_element_located(LoginLocators.LOGIN_BUTTON))
        assert "login" in driver.current_url

    def _register_and_login(self, driver, user_data):
        """Вспомогательный метод для регистрации и входа"""
        # Регистрация
        driver.get(f"{BASE_URL}register")
        wait = WebDriverWait(driver, 15)

        name_input = wait.until(EC.element_to_be_clickable(RegistrationLocators.NAME_INPUT))
        name_input.send_keys(user_data['name'])

        email_input = driver.find_element(*RegistrationLocators.EMAIL_INPUT)
        email_input.send_keys(user_data['email'])

        password_input = driver.find_element(*RegistrationLocators.PASSWORD_INPUT)
        password_input.send_keys(user_data['password'])

        register_button = driver.find_element(*RegistrationLocators.REGISTER_BUTTON)
        register_button.click()

        # Вход после регистрации
        wait.until(EC.visibility_of_element_located(LoginLocators.LOGIN_BUTTON))

        email_input = wait.until(EC.element_to_be_clickable(LoginLocators.EMAIL_INPUT))
        email_input.send_keys(user_data['email'])

        password_input = driver.find_element(*LoginLocators.PASSWORD_INPUT)
        password_input.send_keys(user_data['password'])

        login_button = driver.find_element(*LoginLocators.LOGIN_BUTTON)
        login_button.click()

        # Проверяем, что после входа мы на главной
        wait.until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT))