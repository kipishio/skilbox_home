import time
from contextlib import contextmanager
from collections.abc import Iterable


@contextmanager
def timer() -> Iterable:
    """
    Функция генератор, задекорированная для того чтоб еще ее сделать и контекстным менеджером
    Returns: None

    """
    start = time.time()
    try:
        yield
    except Exception as test_ex:
        print("Поймали исключение: {ex}".format(ex=test_ex))
    finally:
        end_time = time.time() - start
        print("Время работы программы: {time_work}".format(time_work=end_time))
        print("Финальный код который выполниться всегда.\n")


with timer() as t1:
    var_1 = 100 * 100 ** 1000000
    # еще какой-то код
    # mye_test_ex = 'Десять' + 10

with timer() as t2:
    var_2 = 200 * 200 ** 1000000
    # еще какой-то код

with timer() as t3:
    var_3 = 300 * 300 ** 1000000
    # еще какой-то код
