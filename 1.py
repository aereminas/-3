from typing import List, Union

def scale_elements(values: List[Union[int, float]], factor: Union[int, float] = 2) -> List[Union[int, float]]:
    return [val * factor for val in values]

def run_program():
    numbers_text = input("Введите набор чисел через пробел: ")
    try:
        numbers = [float(number) for number in numbers_text.split()]
    except ValueError:
        print("Неправильный формат списка.")
        return

    try:
        scale_factor_text = input("Введите коэффициент масштабирования (по умолчанию 2): ")
        factor = float(scale_factor_text) if scale_factor_text else 2
    except ValueError:
        print("Неправильный формат коэффициента.")
        return

    scaled_values_func = scale_elements(numbers, factor)
    scaled_values_lambda = list(map(lambda x: x * factor, numbers))

    print("Результат (обычная функция):", scaled_values_func)
    print("Результат (lambda):", scaled_values_lambda)


if __name__ == "__main__":
    run_program()
