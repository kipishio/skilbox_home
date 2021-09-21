def letter_case(strings_all):
    big_letters = 0
    small_letters: int = 0
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for i in strings_all:
        if i.lower() in alphabet:
            if i.isupper():
                big_letters += 1
            else:
                small_letters += 1

    # print('{0}____{1}'.format(big_letters, small_letters))

    if big_letters > small_letters:
        strings_all = strings_all.upper()
    else:
        strings_all = strings_all.lower()

    print('Результат: ', strings_all)


string = input('Введите строку: ')
letter_case(string)
