from functools import reduce
from typing import List, Union


def my_add(a: int, b: int) -> int:
    result = a + b

    print(f"{a} + {b} = {result}")

    return result


numbers: List[int] = [9, 1, 2, 3, 4]

print(reduce(my_add, numbers))

sentences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic",
             "because his mother was a Catholic", "or had been"]


def counts_meet(my_int: Union[str, int], my_list_z: str) -> int:
    """
    Функция принимает в первый аргумент строку или число, а во второй аргумент строку.
    :param my_int:
    :param my_list_z:
    :return:
    """
    elem = 'was'
    my_int = my_int
    if isinstance(my_int, str):
        count = 0
        for i_elem in my_int.split(' '):
            if i_elem == elem:
                count += 1

        for i_elem in my_list_z.split(' '):
            if i_elem == elem:
                count += 1
        return count
    else:
        for i_elem in my_list_z.split(' '):
            if i_elem == elem:
                my_int += 1
        return my_int


print(reduce(counts_meet, sentences))
