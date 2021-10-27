import os


def path_check(name):
    name = os.path.abspath(name)
    if os.path.exists(name):

        if os.path.isdir(name):
            print('Путь {0} указывает на дирикторию'.format(name))

        elif os.path.isfile(name):
            print('Путь {0} указывает на файл.'.format(name))
            print('Размер файла {0} байт'.format(os.path.getsize(name)))

    else:
        print('Пути не существует')


path_end_name = os.path.join('eame', 'eame2', 'eew_text.txt')
path_check(path_end_name)
