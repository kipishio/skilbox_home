from typing import Callable, Any

import time


def test_time_work(func: Callable, *args, **kwargs)->str:
    time_start = time.time()
    func(*args, **kwargs)
    time_end = time.time()
    time_result = time_end - time_start
    return 'Время работы программы {time_work}'.format(time_work=round(time_result, 3))


def kil_time(numb: int)->None:
    result = sum([i ** 10 for i in range(1, numb)])

    print('сумма чисел списка {}'.format(result, 2))


print(test_time_work(kil_time, 99999))


my_ddd = test_time_work(kil_time, 2)

print('')


input()