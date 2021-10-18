data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

series = int(input('Укажите номер паспорта: '))
number = int(input('Укажите серию паспорта: '))

for i_key, i_data in data.items():
    if series in i_key and number in i_key:
        fam, name = i_data[0], i_data[1]
        print('{0} {1}'.format(fam, name))
