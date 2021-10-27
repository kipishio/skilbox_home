def check_path():

    while True:
        disk = ''
        path = ''
        extension = ''
        print('________')
        path = input("Укажите путь к файлу: ")
        disk = input('На каком диске должен лежать файл:')
        if not path.startswith(disk):
            print("Путь указан неверно. Не правильно указан диск!")
            continue
        extension = input('Требуемое расширение файла: ')
        if not path.endswith(extension):
            print("Путь указан неверно. проверьте расширение файла!")
            continue
        else:
            print('Путь корректен!')
            break

check_path()

