numb = int(input('Введите целое число: '))
my_dict = dict()
for i in range(1, numb+1):
    my_dict[i] = i**2

print('Результат: ', my_dict)
