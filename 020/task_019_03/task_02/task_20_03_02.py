import random

first_list_alpha = [chr(random.randint(1072, 1103)) for _ in range(10)]
second_list_alpha = [chr(random.randint(1072, 1103)) for _ in range(10)]

first_dict_alpha = {i_ind: i_alpha for i_ind, i_alpha in enumerate(first_list_alpha)}

second_dict_alpha = dict()
for i_ind, i_alpha in enumerate(second_list_alpha):
    second_dict_alpha[i_ind] = i_alpha

print('Первый список: {0}'.format(first_list_alpha))
print('Второй список: {0}'.format(second_list_alpha))
print('Первый словарь: {0}'.format(first_dict_alpha))
print('Второй словарь: {0}'.format(second_dict_alpha))
