import os
import random


def search(abs_path, name_f):
    if os.path.exists(abs_path):
        list_path = os.listdir(abs_path)
        if name_f in list_path:
            list_path_cash.append(os.path.join(abs_path, name_f))
            list_path.remove(name_f)
        for search_path in list_path:
            if os.path.isdir(os.path.join(abs_path, search_path)):
                search(os.path.join(abs_path, search_path), name_f)


def vivio_data_file(path_):
    if os.path.isfile(path_[0]):
        path_search_file = random.choice(path_)
        file = open(path_search_file, 'r', encoding='utf-8')
        data = file.read()
        print('Содержимое файла {0} \n\n{1}'.format(path_search_file, data))
        file.close()


list_path_cash = []
name_file = input('Введите имя файла для поиска и ввода: ')
path = os.path.abspath(os.path.join('..', '..', '..', '..', 'skilbox'))

print('Ищем тут {0}'.format(path))

search(path, name_file)

if len(list_path_cash) > 0:
    vivio_data_file(list_path_cash)
else:
    print('ни один файл не найден')
