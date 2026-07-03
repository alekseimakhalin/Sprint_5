"""
Тесты личного кабинета
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import MainPageLocators, LoginLocators, RegistrationLocators, PersonalAccountLocators
from data.test_data import BASE_URL


class TestProfile:
    """Класс для тестирования личного кабинета"""

    def test_go_to_profile_from_main(self, driver, registered_user):
        """
        Проверка перехода в личный кабинет с главной страницы
        """
        self._register_user(driver, registered_user)
        driver.get(BASE_URL)
        
        wait = WebDriverWait(driver, 15)
        
        # Выполняем вход
        self._login(driver, registered_user['email'], registered_user['password'])
        
        # Кликаем на "Личный кабинет"
        personal_account = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT))
        personal_account.click()
        
        # Проверяем, что перешли в личный кабинет
        profile_title = wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_TITLE))
        assert profile_title.is_displayed()

    def test_logout_from_profile(self, driver, registered_user):
        """
        Проверка выхода из аккаунта через личный кабинет
        """
        self._register_user(driver, registered_user)
        driver.get(BASE_URL)
        
        wait = WebDriverWait(driver, 15)
        
        # Выполняем вход
        self._login(driver, registered_user['email'], registered_user['password'])
        
        # Переходим в личный кабинет
        personal_account = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT))
        personal_account.click()
        
        # Ждем загрузки страницы профиля
        wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_TITLE))
        
        # Кликаем на кнопку "Выход"
        logout_button = wait.until(EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON))
        logout_button.click()
        
        # Проверяем, что перешли на страницу входа
        login_button = wait.until(EC.visibility_of_element_located(LoginLocators.LOGIN_BUTTON))
        assert login_button.is_displayed()

    def test_go_to_constructor_from_profile(self, driver, registered_user):
        """
        Проверка перехода в конструктор из личного кабинета
        """
        self._register_user(driver, registered_user)
        driver.get(BASE_URL)
        
        wait = WebDriverWait(driver, 15)
        
        # Выполняем вход
        self._login(driver, registered_user['email'], registered_user['password'])
        
        # Переходим в личный кабинет
        personal_account = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT))
        personal_account.click()
        
        # Ждем загрузки страницы профиля
        wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_TITLE))
        
        # Кликаем на "Конструктор"
        constructor = wait.until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR))
        constructor.click()
        
        # Проверяем, что перешли на главную
        burger_title = wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))
        assert burger_title.is_displayed()

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

    def _login(self, driver, email, password):
        """Вспомогательный метод для входа"""
        wait = WebDriverWait(driver, 15)
        
        login_button = wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        login_button.click()
        
        email_input = wait.until(EC.element_to_be_clickable(LoginLocators.EMAIL_INPUT))
        email_input.send_keys(email)
        
        password_input = wait.until(EC.element_to_be_clickable(LoginLocators.PASSWORD_INPUT))
        password_input.send_keys(password)
        
        login_btn = driver.find_element(*LoginLocators.LOGIN_BUTTON)
        login_btn.click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT))
