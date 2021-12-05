def reade_file():
    with open('readmе.text', 'r', encoding='utf-8') as file:
        for i_line in file:
            data = i_line.strip().split(' ')
            if len(data) == 1 and data[0] == '':
                pass
            else:
                yield len(data)


print('Всего чисел в файле {count}'.format(count=sum(reade_file())))
