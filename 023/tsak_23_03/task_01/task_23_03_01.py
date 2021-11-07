def try_except(path):
    try:
        f = open(path, 'x', encoding='utf-8')
        my_input = input('Введите текст: ')
        my_input = int(my_input)
        my_input = str(my_input)
        f.write(my_input)
    except FileExistsError:
        print('Файл в который производится запись уже существует!!!')
    except ValueError:
        print('Нельзя преобразовать данные в целое.')
    except:
        print('Неожиданная ошибка')
    else:
        print('Запись в файл прошла успешно')
    finally:
        f.close()








path_ = 'test.txt'
try_except(path_)