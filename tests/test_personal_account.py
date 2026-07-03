"""
Тесты личного кабинета
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import MainPageLocators, PersonalAccountLocators, LoginLocators, RegistrationLocators
from data.test_data import BASE_URL


class TestPersonalAccount:
    """Класс для тестирования личного кабинета"""

    def test_go_to_personal_account(self, driver, registered_user):
        """
        Проверка перехода в личный кабинет
        """
        # Сначала регистрируемся и входим
        self._register_and_login(driver, registered_user)

        wait = WebDriverWait(driver, 15)

        # Кликаем по кнопке "Личный кабинет"
        personal_account = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT))
        personal_account.click()

        # Проверяем, что открылась страница личного кабинета
        profile_title = wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_TITLE))
        assert profile_title.is_displayed()

    def test_go_to_constructor_from_personal_account(self, driver, registered_user):
        """
        Проверка перехода из личного кабинета в конструктор по кнопке "Конструктор"
        """
        self._register_and_login(driver, registered_user)

        wait = WebDriverWait(driver, 15)

        # Переходим в личный кабинет
        personal_account = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT))
        personal_account.click()

        # Ждем загрузки личного кабинета
        wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_TITLE))

        # Кликаем по кнопке "Конструктор"
        constructor = wait.until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR))
        constructor.click()

        # Проверяем, что открылась главная страница
        burger_title = wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))
        assert burger_title.is_displayed()

    def test_go_to_main_page_from_personal_account_by_logo(self, driver, registered_user):
        """
        Проверка перехода из личного кабинета на главную по клику на логотип
        """
        self._register_and_login(driver, registered_user)

        wait = WebDriverWait(driver, 15)

        # Переходим в личный кабинет
        personal_account = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT))
        personal_account.click()

        # Ждем загрузки личного кабинета
        wait.until(EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_TITLE))

        # Кликаем по логотипу
        logo = wait.until(EC.element_to_be_clickable(MainPageLocators.LOGO))
        logo.click()

        # Проверяем, что открылась главная страница
        burger_title = wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))
        assert burger_title.is_displayed()

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