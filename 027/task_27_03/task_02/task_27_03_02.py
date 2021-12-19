from typing import Callable
import time


def measure_time(func: Callable) -> Callable:
    def wrapped(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        time_result = time_end - time_start
        return round(time_result, 3)

    return wrapped


@measure_time
def sum_cube_numbers(numbers: int, name: str):
    print('Привет {}'.format(name))
    result = sum([i ** 3 for i in range(1, numbers)])
    print('Сумма всех кубов от 1 до числа {numb}: {sum_result}'.format(numb=numbers-1, sum_result=result))


ert = sum_cube_numbers(10000000, "Иван")
print('Время роботы функции {}'.format(ert))
