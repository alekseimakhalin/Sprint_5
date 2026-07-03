"""
Вспомогательные функции для генерации тестовых данных
"""

import random
import string
from faker import Faker

fake = Faker('ru_RU')


def generate_login():
    """
    Генерирует уникальный email для регистрации
    Формат: имя_фамилия_номер_когорты_3_цифры@домен
    """
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    cohort = random.randint(1, 10)
    digits = ''.join(random.choices(string.digits, k=3))
    domain = 'yandex.ru'

    return f"{first_name}_{last_name}_{cohort}_{digits}@{domain}"


def generate_name():
    """Генерирует имя"""
    return fake.first_name()


def generate_password():
    """Генерирует пароль (минимум 6 символов)"""
    letters = string.ascii_lowercase
    digits = string.digits
    password = ''.join(random.choices(letters + digits, k=random.randint(6, 10)))
    return password


def generate_short_password():
    """Генерирует короткий пароль (менее 6 символов)"""
    return ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 5)))
