import math

# Определяем функцию f(x)
def f(x, y, case):
    if case == 1:
        return math.tanh(y**3)
    elif case == 2:
        return math.sinh(y)
    elif case == 3:
        return x**3

# Основная функция для вычисления b
def calculate_b(x, y, case):
    x_cube = x**3

    if x_cube > 5:
        return math.log(f(x, y, case))**3
    elif x_cube < 45:
        return math.tan(x_cube) + f(x, y, case)
    else:
        return (y**2 - x**2)**(1/3) + f(x, y, case)

# Ввод значений x, y и выбор функции f(x)
def main():
    try:
        x = float(input("Введите значение x: "))
        y = float(input("Введите значение y: "))
        
        print("Выберите функцию f(x):")
        print("1. tanh(y^3)")
        print("2. sinh(y)")
        print("3. x^3")
        case = int(input("Введите номер функции (1, 2 или 3): "))

        if case not in [1, 2, 3]:
            print("Неверный выбор функции.")
            return

        # Вычисление b
        b = calculate_b(x, y, case)
        print(f"Результат: b = {b}")

    except ValueError:
        print("Ошибка: Введите корректные числовые значения.")

if __name__ == "__main__":
    main()
