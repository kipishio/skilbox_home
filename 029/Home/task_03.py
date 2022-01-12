from typing import Callable
from datetime import datetime
import functools


def time_work(func, format):
    # @functools.wraps(func)
    def wrapper(*args, **kwargs):

        start = datetime.now()
        print("- Запускается '{inf}' . Дата и время запуска: {dt}".format(inf=str(func).split()[1],
                                                                          dt=start.strftime(format)))

        result = func(*args, **kwargs)

        end = datetime.now() - start
        print("- Завершение '{inf}' , время работы = {dt}s".format(inf=str(func).split()[1],
                                                                          dt=round(end.total_seconds(), 3)))

        return result
    return wrapper

def log_methods(format_, var_func):

    def decor_func(cls):
        for i_named_func in dir(cls):
            if i_named_func.startswith('__') == False:
                dec_func = var_func(getattr(cls, i_named_func), format_)
                setattr(cls, i_named_func, dec_func)
        return cls
    return decor_func


@log_methods(format_="%b %d %Y - %H:%M:%S", var_func=time_work)
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods(format_="%b %d %Y - %H:%M:%S", var_func=time_work)
class B(A):

    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод Наследник test sum 1")

    def test_sum_2(self):
        print("Тут метод test sum 2")
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
