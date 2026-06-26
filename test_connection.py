from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")

chromedriver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
service = Service(chromedriver_path)

try:
    print("Запускаем драйвер...")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("Драйвер запущен!")
    
    print("Открываем сайт...")
    driver.get("https://stellarburgers.education-services.ru/login")
    print("✅ Сайт открыт!")
    print(f"Заголовок: {driver.title}")
    
    driver.quit()
    print("Браузер закрыт")
except Exception as e:
    print(f"❌ Ошибка: {e}")
