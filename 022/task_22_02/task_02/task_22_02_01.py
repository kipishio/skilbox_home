import os

def search(abs_path, name_f):
    if os.path.exists(abs_path):
        list_path = os.listdir(abs_path)
        if name_f in list_path:
            list_path_cash.append(os.path.join(abs_path, name_f))
            list_path.remove(name_f)
        for search_path in list_path:
            if os.path.isdir(os.path.join(abs_path, search_path)):
                search(os.path.join(abs_path, search_path), name_f)


list_path_cash = []
name_file = '111.txt'
path = os.path.abspath(os.path.join('..', '..', '..', '..', 'skilbox'))

print('Ищем тут {0} \n'.format(path))

search(path,name_file)

if len(list_path_cash) > 0:
    print('Найдены следующие фалы:')
    for i_path in list_path_cash:
        print(i_path)
else:
    print('ни один файл не найден')