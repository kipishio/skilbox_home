from typing import Callable
from datetime import datetime
import functools

def decor_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('До')
        result = func(*args, **kwargs)
        print('После')
        return result
    return wrapper

def log_methods(format):
    def decor_func(cls):
        for i_named_func in dir(cls):
            if i_named_func.startswith('__') == False:
                name_func = getattr(cls, i_named_func)

                print('/'*5, name_func)

                dec_func = decor_func(name_func)
                # dec_func(cls)
                setattr(cls, i_named_func, dec_func)

        @functools.wraps(cls)
        def wrapper(*arg, **kwargs):
            return cls
        return wrapper()
    return decor_func



@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):

    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()


# Результат:#
# - Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
# - Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
#
# Тут метод test_sum_1
# - Завершение 'A.test_sum_1', время работы = 0.187s
#
# Тут метод test_sum_1 у наследника
# - Завершение 'B.test_sum_1', время работы = 0.187s
#
# - Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 - 21:50:37
# Тут метод test_sum_2 у наследника
#
# - Завершение 'B.test_sum_2', время работы = 0.370s
