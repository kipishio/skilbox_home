BRUCE_WILLIS = 42



input_data = input('Введите строку: ')
try:
    try:
        leeloo = int(input_data[4])
    except ValueError:
        print('невозможно преобразовать к числу')
    except IndexError:
        print('выход за границы списка')

    try:
        result = BRUCE_WILLIS * leeloo
    except ZeroDivisionError:
        print('На ноль делить нельзя')


    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except:
    print('Что то пошло не так')