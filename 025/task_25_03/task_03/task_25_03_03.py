import os

class DivisionError(Exception):
    pass


with open('numbers.txt', 'r', encoding='utf-8') as file:
    try:
        for i_line in file:
            list_int = i_line.split(' ')
            if list_int[0] < list_int[1]:
                raise DivisionError('нельзя делить большее на меньшее')
            nn = int(list_int[0]) / int(list_int[1])
    except ZeroDivisionError:
        print('На ноль делить нельзя')

