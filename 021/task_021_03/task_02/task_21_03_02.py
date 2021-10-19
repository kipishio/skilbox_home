import ast
data_type = input('Введите данные: ')

data_type = ast.literal_eval(data_type)
# print(data_type)

if type(data_type) == str:
    print('Тип данных: str (строка)'.format(type(data_type)))
    print('Неизменяемый (immutable)')
    print('Id объекта: ', id(data_type))
elif type(data_type) == int:
    print('Тип данных: int (целое число)'.format(type(data_type)))
    print('Неизменяемый (immutable)')
    print('Id объекта: ', id(data_type))
elif type(data_type) == float:
    print('Тип данных: float (дробное число)'.format(type(data_type)))
    print('Неизменяемый (immutable)')
    print('Id объекта: ', id(data_type))
elif type(data_type) == tuple:
    print('Тип данных: tuple (кортеж)'.format(type(data_type)))
    print('Неизменяемый (immutable)')
    print('Id объекта: ', id(data_type))
elif type(data_type) == bool:
    print('Тип данных: bool (логический тип данных)'.format(type(data_type)))
    print('Неизменяемый (immutable)')
    print('Id объекта: ', id(data_type))

elif type(data_type) == list:
    print('Тип данных: list (список)'.format(type(data_type)))
    print('Изменяемый (mutable)')
    print('Id объекта: ', id(data_type))
elif type(data_type) == dict:
    print('Тип данных: dict (словарь)'.format(type(data_type)))
    print('Изменяемый (mutable)')
    print('Id объекта: ', id(data_type))
elif type(data_type) == set:
    print('Тип данных: set (множество)'.format(type(data_type)))
    print('Изменяемый (mutable)')
    print('Id объекта: ', id(data_type))

# print(type(data_type))
