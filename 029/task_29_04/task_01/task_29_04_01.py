from typing import Callable
from datetime import datetime
import functools


def my_decorator(cls: Callable):
    """
    Декоратор класса, который выдаёт дату и время создания, а также список всех методов объекта класса каждый раз,
    когда объект класса создаётся в основном коде.
    Args:
        cls: Callable

    Returns: Callable

    """
    @functools.wraps(cls)
    def wrapped(*args, **kwargs)->Callable:
        result = cls(*args, **kwargs)
        count = 1
        for i in dir(cls):
            if count % 10 == 0:
                print()
            count +=1
            print(i, end=' |   ')

        print('\n')
        do_time = datetime.now()
        print(do_time)
        return result

    return wrapped


@my_decorator
class My_Klass:
    def __init__(self):
        self.text = "Примет я класс {}".format(self.__class__.__name__)

    def test1(self):
        print('test1')

    def test2(self):
        print('test2')


my_klass1 = My_Klass()
print('*' * 140)
my_klass2 = My_Klass()