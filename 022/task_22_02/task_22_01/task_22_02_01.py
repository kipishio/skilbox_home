import os


def path_check(name):
    path = os.path.abspath(name)
    if os.path.exists(path):
        if os.path.islink(name):
            print('Путь {0} является символьной ссылкой.'.format(path))
        if os.path.isdir(path):
            print('Путь {0} указывает на дирикторию'.format(path))
        elif os.path.isfile(path):
            print('Путь {0} указывает на файл.'.format(path))
            print('Размер файла {0}'.format(os.path.getsize(path)))
    else:
        print('Пути не существует')



print(os.listdir(os.path.abspath('')))

path_end_name = 'new_text.txt'
path_check(path_end_name)

