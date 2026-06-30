"""
Тесты входа
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators.locators import MainPageLocators, LoginLocators, RegistrationLocators
from data.test_data import BASE_URL
import time


class TestLogin:
    """Класс для тестирования входа"""

    def test_login_by_main_button(self, driver, registered_user):
        """
        Проверка входа по кнопке "Войти в аккаунт" на главной
        """
        # Регистрируем пользователя
        self._register_user(driver, registered_user)
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 15)

        # Кликаем по кнопке "Войти в аккаунт"
        login_button = wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        login_button.click()
        
        # Ждем загрузки страницы входа
        time.sleep(2)
        print(f"Текущий URL после клика: {driver.current_url}")
        print(f"Заголовок страницы: {driver.title}")
        
        # Проверяем, что есть поле Email
        try:
            email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
            print("✅ Поле Email найдено!")
        except:
            print("❌ Поле Email не найдено!")
            # Показываем HTML страницы для отладки
            print("HTML страницы:", driver.page_source[:500])

        # Вводим данные для входа
        self._login_user(driver, registered_user['email'], registered_user['password'])

        # Проверяем, что выполнен вход
        personal_account = wait.until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT))
        assert personal_account.is_displayed()

    def _register_user(self, driver, user_data):
        """Вспомогательный метод для регистрации пользователя"""
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
        wait.until(EC.url_contains("login"))

    def _login_user(self, driver, email, password):
        """Вспомогательный метод для входа"""
        wait = WebDriverWait(driver, 15)
        
        # Пробуем разные локаторы для поля Email
        try:
            email_input = wait.until(EC.element_to_be_clickable(LoginLocators.EMAIL_INPUT))
        except:
            # Если не работает, пробуем найти по классу
            email_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".input_type_text input")))

        email_input.send_keys(email)

        try:
            password_input = wait.until(EC.element_to_be_clickable(LoginLocators.PASSWORD_INPUT))
        except:
            password_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".input_type_password input")))
            
        password_input.send_keys(password)

        login_button = driver.find_element(*LoginLocators.LOGIN_BUTTON)
        login_button.click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT))
