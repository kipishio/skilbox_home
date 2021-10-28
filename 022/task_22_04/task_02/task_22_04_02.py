import os


def all_script_path_to_file(path_my_script):
    for i_path in os.listdir(path_my_script):

        if os.path.isfile(os.path.join(path_my_script, i_path)):
            if i_path[-2::] == 'py':
                my_scripts = open(os.path.join(path_my_script, i_path), 'r', encoding='utf-8')
                my_scripts_read = my_scripts.read()

                my_scripts_file = open('scripts.txt', 'a', encoding='utf-8')
                my_scripts_file.write('{0} \n {1}\n{2}\n\n'.format(os.path.join(path_my_script, i_path), my_scripts_read, '*' * 40))

                my_scripts.close()
                my_scripts_file.close()
        else:
            all_script_path_to_file(os.path.join(path_my_script, i_path))


path_my_script = os.path.abspath(os.path.join('..', '..', '..', '..', 'python_basic'))
print(path_my_script)

all_script_path_to_file(path_my_script)
