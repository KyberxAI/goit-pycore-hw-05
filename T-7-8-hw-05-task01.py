# ФУНКЦІЯ fibonacci(n) 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0  # відповідь без обчислень
        if n == 1:
            return 1  # відповідь без обчислень
        if n in cache:
            return cache[n] # відповідь зі словника
        # рекурсивний математичний вираз числа Фібоначчі
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci    # Повертаємо внутрішню функцію, яка зберігає доступ до кешу через замикання


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
