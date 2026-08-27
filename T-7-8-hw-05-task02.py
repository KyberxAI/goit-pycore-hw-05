import re
from decimal import Decimal
from typing import Callable

def generator_numbers(text: str):
    # Знаходимо всі дійсні числа (цілі і з дробами) відокремлені пробілами
    # re.findall() знайти всі відповідні варіанти
    # (?<=\s) зліва має бути пробіл
    # \d+ціла частина числа
    # (?:\.\d+)? необов'язкова дробова частина
    # (?=\s)  справа має бути пробіл
    number_list = re.findall(r"(?<=\s)\d+(?:\.\d+)?(?=\s)", text)
    for num in number_list:
        # Повертаємо числа по одному за допомогою генератора
        yield Decimal(num)


def sum_profit(text: str, func: Callable):
    # Передаємо текст функції-генератору та підсумовуємо отримані числа
    # print(repr(func(text)))
    total = 0
    for value in func(text):
        total += value
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 EUR як основний дохід, \
доповнений додатковими надходженнями 20.55 і 214.00 EUR."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
