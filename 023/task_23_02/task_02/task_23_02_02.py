import os


def ages_result(path):
    file = open(os.path.abspath(path), 'r', encoding='utf-8')
    name = 64
    age = 0
    try:
        file_write = open('result.txt', 'x', encoding='utf-8')
        for i_str in file:
            try:
                name += 1
                age = int(i_str)
            except (TypeError, ValueError):
                print('Неверный тип данных')
                file_write.write('имя: {0} - возраст: {1}\n'.format(chr(name), str(age)))
        file_write.close()
        print(file_write.closed)

    except FileNotFoundError:
        print('Файл не найден!!!')
    except FileExistsError:
        print('Файл в который производится запись уже существует!!!')
    except PermissionError:
        print('Возможно вы пытаетесь открыть не файл а директорию!!!')
    finally:
        file.close()



    file.close()



path_ = ('ages.txt')
ages_result(path_)
