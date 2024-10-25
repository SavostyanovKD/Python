import math

# Исходные данные
a = 5.3
x1 = 4
xn = 8
delta_x = 0.2

# Функция для вычисления y
def calculate_y(x, a):
    return math.sqrt(math.log(a ** 2) / (x + a)) + math.cos(a) ** 2

# Вычисление значений y с помощью цикла while
x = x1
while x <= xn:
    y = calculate_y(x, a)
    print(f"x = {x:.2f}, y = {y:.5f}")
    x += delta_x
