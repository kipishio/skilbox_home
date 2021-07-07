line_list = list(input('Введите строку: '))
count = 0
count_sym = 0
sym_search = ":"
sym_replace = ";"


for sym in line_list:
    if sym == sym_search:
        line_list[count] = sym_replace
        count_sym += 1
        count += 1
    else:
        count += 1

for i in line_list:
    print(i, end='')

print('\nКоличество замен = ', count_sym)
