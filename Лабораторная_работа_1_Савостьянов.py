import math

# Функция для вычисления выражения
def calculate_expression(x, y):
    # Проверка на деление на ноль
    if abs(x + y) == 0:
        return "Ошибка: деление на 0 невозможно"
    
    # Первая часть выражения
    part1 = y ** (x + 1) / (abs(y - 2) + 3) ** (1 / 3)
    
    # Вторая часть выражения
    part2 = ((x + y) / 2) / (2 * abs(x + y)) * (x + 1)
    
    # Полное выражение
    result = part1 + part2
    return result

# Ввод данных от пользователя
try:
    x = float(input("Введите значение x: "))
    y = float(input("Введите значение y: "))
    
    # Вычисление и вывод результата
    result = calculate_expression(x, y)
    print(f"Результат вычисления: {result}")

except ValueError:
    print("Ошибка: введите числовые значения.")
