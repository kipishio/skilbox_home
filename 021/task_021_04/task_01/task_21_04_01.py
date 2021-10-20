def working_file(question, message="Неверный ввод. Пожалуйста, введите 'да' или 'нет'.", number=3):
    while number != 0:
        print(question)
        answer = input('Ответ: ').lower()
        if answer == 'да':
            return 1
        elif answer == 'нет':
            return 0
        else:
            print(message)
            number -= 1
            print('Осталось попыток: ', number)


working_file('Вы действительно хотите выйти?')
print()
working_file('Вы действительно хотите выйти?', "Так удалить или нет? ")
print()
working_file('Вы действительно хотите выйти?', number=2)
