import os
from builtins import sorted


def palendrom(my_str):
    if my_str == ''.join(reversed(my_str)):
        return True
    else:
        return False
count_palindrom = 0
stroka = 0
st = ''

f = open('words.txt', 'r', encoding='utf-8')

for i_str in f:
    stroka += 1
    try:
        if str(sorted(i_str.strip())[0]).isdigit():
            st = i_str
            raise ValueError('Среди текста есть числа')
        else:
            if i_str.endswith('\n'):
                if palendrom(i_str[:-1]):
                    count_palindrom += 1
                    print('Строка №{0}, "{1}" это палиндром. Общее количество палендромов: {2}'.format(stroka, i_str[:-1], count_palindrom))
            else:
                if palendrom(i_str):
                    count_palindrom += 1
                    print('Строка №{0}, "{1}" это палиндром. Общее количество палендромов: {2}'.format(stroka, i_str, count_palindrom))
    except ValueError:
        if os.path.exists('errors.log'):
            f_log = open('errors.log', 'a', encoding='utf-8')
            f_log.write('Ошибка в строке №{0}, в имени {1} есть числа\n'.format(stroka, st.rstrip()))
            f_log.close()
            print('Запись в лог')
        else:
            f_log = open('errors.log', 'w', encoding='utf-8')
            f_log.write('Ошибка в строке №{0}, в имени {1} есть числа\n'.format(stroka, st.rstrip()))
            f_log.close()
            print('Запись в лог')
f.close()
