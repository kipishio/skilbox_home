# Пример:
#
# Введите текст: У нас пошёл снег !
#
# Исправленный текст: У нас пошёл снег !

text = input('Введите текст: ')
edit_text = text.split()
edit_text = ' '.join(edit_text)
print(edit_text)
