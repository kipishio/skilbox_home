print('Текущие контакты на телефоне:\n')
print('<Пусто>')
kontakt = {}

while True:
    for kont in kontakt:
        print(kont, kontakt[kont])
    print()
    name = input('Введите имя: ')
    if name == 'end':
        print('Завершение программы!')
        break

    if name in kontakt:
        print('Ошибка: такое имя уже существует.')
        continue
    else:
        phone_number = input('Введите номер телефона: ')
        kontakt[name] = phone_number

    print()
    print('Текущие контакты на телефоне: ')
