insert_data = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки)\n: ')

insert_data_list = insert_data.split(" ")

print(insert_data_list)
data_dict = dict()

data_dict['Имя'] = insert_data_list[0]
data_dict['Фамилия'] = insert_data_list[1]
data_dict['Город'] = insert_data_list[2]
data_dict['Место учебы'] = insert_data_list[3]
data_dict['Фамилия'] = insert_data_list[4]
data_dict['Оценки'] = []
for data in insert_data_list[4:]:
    data_dict['Оценки'].append(int(data))

print(data_dict)
for i in data_dict:
    print(i, '-', data_dict[i])

