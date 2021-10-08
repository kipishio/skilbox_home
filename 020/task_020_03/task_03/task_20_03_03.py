def universal_programm(data):
    print('Результат: ', end='')
    result = [i_data for i_ind, i_data in enumerate(data) if i_ind % 2 == 0]
    print(result)


my_str = 'О Дивный Новый мир!'
my_list = [100, 200, 300, 'буква', 0, 2, 'а']
my_dict = {'крот': 2345, 'том': 893, 876: 'енот', 'софт': 'победа'}
my_tuple = 'ура', 'google', 'work', 'my', 444, 'money'

universal_programm(my_str)
universal_programm(my_list)
universal_programm(my_dict)
universal_programm(my_tuple)

