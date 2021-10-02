text = input('Введите строку: ')
text_set = set(text)

new_text = ''
for i in text_set:
    if '0' <= i <= '9':
        new_text += i

print('Различные цифры строки:', new_text)
