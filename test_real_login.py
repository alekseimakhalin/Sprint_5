from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.test_data import BASE_URL
from utils.helpers import generate_login, generate_name, generate_password
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
    # Генерируем данные пользователя
    email = generate_login()
    name = generate_name()
    password = generate_password()
    
    print(f"Создаем пользователя: {email}, {name}, {password}")
    
    # 1. Регистрация
    driver.get(f"{BASE_URL}register")
    wait = WebDriverWait(driver, 15)
    
    name_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Имя']/following-sibling::input")))
    name_input.send_keys(name)
    
    email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
    email_input.send_keys(email)
    
    password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    password_input.send_keys(password)
    
    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()
    time.sleep(2)
    
    print("✅ Регистрация прошла")
    print(f"URL после регистрации: {driver.current_url}")
    
    # 2. Вход
    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Email']/following-sibling::input")))
    email_input.send_keys(email)
    
    password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    password_input.send_keys(password)
    
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()
    time.sleep(3)
    
    print("✅ Вход выполнен")
    print(f"URL после входа: {driver.current_url}")
    
    # 3. Переход в личный кабинет
    personal_account = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']")))
    personal_account.click()
    time.sleep(3)
    
    print(f"URL личного кабинета: {driver.current_url}")
    print(f"Заголовок: {driver.title}")
    
    # Ищем все тексты на странице
    print("\n=== Все тексты на странице личного кабинета ===")
    all_text = driver.find_elements(By.XPATH, "//*[text()!='']")
    for el in all_text:
        text = el.text
        if len(text) > 0 and len(text) < 50:
            print(f"- {text}")
            
except Exception as e:
    print(f"❌ Ошибка: {e}")
    print(f"Текущий URL: {driver.current_url}")
finally:
    driver.quit()
