"""
Локаторы для страниц Stellar Burgers
"""

from selenium.webdriver.common.by import By


class RegistrationLocators:
    """Локаторы страницы регистрации"""
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class LoginLocators:
    """Локаторы страницы входа"""
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class MainPageLocators:
    """Локаторы главной страницы"""
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]//a")
    BURGER_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")


class PersonalAccountLocators:
    """Локаторы страницы личного кабинета"""
    # На основе реальных текстов со страницы
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PROFILE_TITLE = (By.XPATH, "//a[text()='Профиль']")
    PROFILE_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    PROFILE_LOGIN = (By.XPATH, "//label[text()='Логин']/following-sibling::input")
    PROFILE_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    HISTORY_ORDERS = (By.XPATH, "//a[text()='История заказов']")
