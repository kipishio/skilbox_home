server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i_name, i_data in server_data.items():
    print(i_name, ':\n')
    # print(i_data)
    for name, data in i_data.items():
        print('----{0} : {1}\n'.format(name, data))



