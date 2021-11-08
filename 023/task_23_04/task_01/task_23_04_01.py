
count_str = 0

try:
    f = open('people.txt', 'r', encoding='utf-8')
    for i_str in f:
        count_str += 1
        if i_str.endswith('\n'):
            if len(i_str) - 1 < 3:
                raise BaseException('Длина имени в строке {0} меньше 3-х символов'.format(count_str))
            print('Имя {0} длина {1}'.format(i_str[:-1], len(i_str)-1))

except FileNotFoundError:
    print('problem file ne naiden!!!')
except BaseException:
    print('Poimal iskluchenie!!! имя {0} длина {1}'.format(i_str[:-1], len(i_str)-1))
    raise
finally:
    f.close()
    print('Файл закрыт.')

