contact = dict()
name = ''

while True:
    name = input('Укажите имя: ')
    if name == 'exit':
        break
    surname = input('Укажите фамилию: ')
    phone = input('Укажите телефон: ')

    if name not in contact and surname not in contact:
        contact[(name, surname)] = phone
    else:
        print('Указанный контакт уже существует')
    print(contact)
print('Вы завершили добавление контактов')



