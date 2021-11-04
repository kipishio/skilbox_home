import os


def ages_result(path):
    try:
        file = open(os.path.abspath(path), 'r', encoding='utf-8')
        name = 64
        file_write = open('result.txt', 'x', encoding='utf-8')

        for i_str in file:
            name += 1
            file_write.write('имя: {0} - возраст: {1}'.format(chr(name), i_str))

        file.close()
        file_write.close()

    except FileNotFoundError:
        print('Файл не найден!!!')
    except FileExistsError:
        print('Файл в который производится запись уже существует!!!')
    except PermissionError:
        print('Возможно вы пытаетесь открыть не файл а директорию!!!')


path_ = ('ages.txt')
ages_result(path_)
