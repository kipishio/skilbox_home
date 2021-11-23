import os

def print_dirs(path_abs):
    print('Содержимое директории ', path_abs)
    for name_elem in os.listdir(path_abs):
        print(name_elem)


intrasting_dir = ['python_basic', 'skilbox_home']

for i_elem in intrasting_dir:
    path = os.path.abspath(os.path.join('..', '..', '..', '..', i_elem))
    print_dirs(path)




