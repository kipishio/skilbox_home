line_list = list(input('Введите строку: '))
number_sym = int(input('Номер символа: '))
number_sym -= 1

count = 0
count_sym = 0

for sym in line_list:
    if line_list[number_sym] == sym:
        count_sym += 1
    count += 1

if number_sym > 0:
    print("Номер символа с лево:", line_list[number_sym - 1])
else:
    print('Нет символов с лево')

if number_sym == count:
    print("Символов с право нет")
else:
    print("Символ с право", line_list[number_sym+1])

if count_sym > 1:
    print('Таких же символов ровно', count_sym-1)
else:
    print('Таких же символов нет.')

