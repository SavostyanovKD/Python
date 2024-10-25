import math

# Исходные данные
a = 5.3
x1 = 4
xn = 8
delta_x = 0.2

# Функция для вычисления y
def calculate_y(x, a):
    return math.sqrt(math.log(a ** 2) / (x + a)) + math.cos(a) ** 2

# Вычисление значений y с помощью цикла for
for x in range(int((xn - x1) / delta_x) + 1):
    current_x = x1 + x * delta_x
    y = calculate_y(current_x, a)
    print(f"x = {current_x:.2f}, y = {y:.5f}")
