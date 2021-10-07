def index_alpha(my_str):
    print('Ответ: ', end='')
    for i_ind, i_alpha in enumerate(my_str):
        if i_alpha == '~':
            print('{0}'.format(i_ind), end=' ')


my_str = input('Строка: ')
index_alpha(my_str)




