"""
Тесты конструктора
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import MainPageLocators
from data.test_data import BASE_URL


class TestConstructor:
    """Класс для тестирования конструктора"""

    def test_buns_tab_active_by_default(self, driver):
        """
        Проверка, что по умолчанию активен таб "Булки"
        """
        self._open_constructor_page(driver)

        wait = WebDriverWait(driver, 15)

        # Проверяем, что активен таб "Булки"
        active_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Булки" in active_tab.text

    def test_sauces_tab_click(self, driver):
        """
        Проверка перехода к разделу "Соусы"
        """
        self._open_constructor_page(driver)

        wait = WebDriverWait(driver, 15)

        # Кликаем по разделу "Соусы"
        sauces_tab = wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB))
        sauces_tab.click()

        # Проверяем, что активен таб "Соусы"
        active_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Соусы" in active_tab.text

    def test_fillings_tab_click(self, driver):
        """
        Проверка перехода к разделу "Начинки"
        """
        self._open_constructor_page(driver)

        wait = WebDriverWait(driver, 15)

        # Кликаем по разделу "Начинки"
        fillings_tab = wait.until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB))
        fillings_tab.click()

        # Проверяем, что активен таб "Начинки"
        active_tab = wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB))
        assert "Начинки" in active_tab.text

    def _open_constructor_page(self, driver):
        """Вспомогательный метод для открытия конструктора"""
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 15)
        wait.until(EC.visibility_of_element_located(MainPageLocators.BURGER_TITLE))
