import math
import statistics

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> Union[float, str]:
    if b == 0:
        raise ZeroDivisionError("Нельзя делить на нуль")
    operation_type = input("Выберите вид деления (1 - обычное, 2 - остаток, 3 - целочисленное): ")
    if operation_type == '1':
        return a / b
    elif operation_type == '2':
        return a % b
    elif operation_type == '3':
        return a // b
    else:
        raise ValueError("Некорректный выбор вида деления")

def power(base: float, exponent: float) -> float:
    return base ** exponent

def calculate_factorial(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise TypeError("Факториал определяется только для целых неотрицательных чисел")
    return math.factorial(n)

def calculate_sine(angle: float) -> float:
    return math.sin(angle)

def get_median(numbers: list) -> float:
    if not isinstance(numbers, list):
        raise TypeError("Для вычисления медианы необходим список чисел")
    if not all(isinstance(val, (int, float)) for val in numbers):
        raise TypeError("Список должен содержать только числовые значения")

    return statistics.median(numbers)

def perform_calculation():
    while True:
        print("\nДоступные действия:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Факториал")
        print("7. Синус")
        print("8. Медиана")
        print("--------------------")

        choice = input("Выберите действие (или 'exit' для выхода): ")

        if choice.lower() == 'exit':
            break

        try:
            choice = int(choice)
            if not 1 <= choice <= 8:
                raise ValueError
        except ValueError:
            print("Недопустимый номер действия.")
            continue

        try:
            if choice in [1, 2, 3, 4, 5]:
                num1 = float(input("Аргумент 1: "))
                num2 = float(input("Аргумент 2: "))
                if choice == 1:
                    result = add(num1, num2)
                elif choice == 2:
                    result = subtract(num1, num2)
                elif choice == 3:
                    result = multiply(num1, num2)
                elif choice == 4:
                    result = divide(num1, num2)
                elif choice == 5:
                    result = power(num1, num2)
            elif choice == 6:
                val = int(input("Целое число: "))
                result = calculate_factorial(val)
            elif choice == 7:
                angle_rad = float(input("Значение угла (в радианах): "))
                result = calculate_sine(angle_rad)
            elif choice == 8:
                numbers_str = input("Ввод списка чисел через пробел: ")
                try:
                    number_list = [float(x) for x in numbers_str.split()]
                except ValueError:
                    print("Некорректный ввод списка чисел.")
                    continue
                result = get_median(number_list)
            print(">>>", result)

        except (ValueError, TypeError, ZeroDivisionError) as error:
            print(error)
        print("--------------------")

if __name__ == "__main__":
    perform_calculation()
