def cipher(message, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    encrypted_message = [(alphabet[(alphabet.index(i) + shift) % 33]) if i != ' ' else i for i in message]
    print('Зашифрованное сообщение:', ''.join(encrypted_message))


message = input("Введите сообщение: ").islower()
shift = int(input("Введите сдвиг: "))
cipher(message, shift)
