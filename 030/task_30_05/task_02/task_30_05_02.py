"""
Введеный текст фильтруется, он должен быть без чисел и без букв в верхнем регистре.
"""
var = sorted(list(filter(lambda elem: elem.isalpha() and elem.islower(), (input('Введите строку: ')))))
print(var)

# var = 'qWe456rtY'
