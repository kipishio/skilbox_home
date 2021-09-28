print('Текущие контакты на телефоне:\n')
print('<Пусто>\n')
kontakt = {}

for i in kontakt:
    print('Привет')

while True:
    for kont in kontakt:
        print(kont, kontakt[kont])

    name = input('Введите имя: ')
    if name == 'end':
        print('Завершение программы!')
        break

    if name in kontakt:
        print('Ошибка: такое имя уже существует.')
        continue
    else:
        phone_number = int(input('Введите номер телефона: '))
        kontakt[name] = phone_number

    print('Текущие контакты на телефоне: ')