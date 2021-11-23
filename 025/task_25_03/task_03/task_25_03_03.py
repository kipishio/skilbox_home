import os

class My_DivisionError(Exception):
    pass


with open('numbers.txt', 'r', encoding='utf-8') as file:
    for i_line in file:
        list_numbers = i_line.split(' ')
        dividend = int(list_numbers[0].strip())
        divider = int(list_numbers[1].strip())
        if dividend < divider:
            raise My_DivisionError('Нельзя делить большее на меньшее пер dividend/divider = {} / {}'.format(dividend, divider))
        else:
            try:
                nn = dividend / divider
            except ZeroDivisionError:
                print('На ноль делить нельзя')

