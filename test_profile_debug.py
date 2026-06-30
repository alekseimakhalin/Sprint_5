from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.test_data import BASE_URL
import os
import time

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

chromedriver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Открываем страницу входа
    driver.get(f"{BASE_URL}login")
    wait = WebDriverWait(driver, 15)
    
    # Вводим email и пароль
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Email']/following-sibling::input")))
    email_input.send_keys("test@test.com")
    
    password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    password_input.send_keys("123456")
    
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()
    time.sleep(3)
    
    # Нажимаем на личный кабинет
    personal_account = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']")))
    personal_account.click()
    time.sleep(3)
    
    print(f"URL: {driver.current_url}")
    print(f"Заголовок: {driver.title}")
    
    # Ищем все элементы на странице
    print("\n=== Все тексты на странице ===")
    all_text = driver.find_elements(By.XPATH, "//*[text()!='']")
    for el in all_text:
        text = el.text
        if len(text) > 0 and len(text) < 50:
            print(f"- {text}")
            
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    driver.quit()
