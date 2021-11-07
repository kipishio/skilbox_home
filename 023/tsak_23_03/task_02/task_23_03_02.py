# task_20_04_01.py
try:
    incomes = {
        'apple': 5600.20,
        'orange': 3500.45,
        'banana': 5000.00,
        'bergamot': 3700.56,
        'durian': 5987.23,
        'peach': 10000.50,
        'pear': 1020.00,
        'persimmon': 310.00,
    }

    for i_name, i_price in incomes.items():
        print('{name} -- {price}\n'.format(
            name=i_name,
            price=i_price
        ))
except SyntaxError:
    print('проверьте код на синтаксические ошибки')
except NameError:
    print('Переменная похоже не существует')
finally:
    print('Спасибо за внимание')
