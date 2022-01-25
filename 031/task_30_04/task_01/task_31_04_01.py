import requests
import re
import json

if __name__ == '__main__':
    my_request = requests.get('https://swapi.dev/api/people/3/')

    data = json.loads(my_request.text)  # Десериализация JSON
    data['name'] = 'Roman'

    with open('my_request_file.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent='    ')  # Сериализация JSON

    with open('my_request_file.json', 'r', encoding='utf-8') as file:
        data = json.load(file)          # Десериализация JSON
        data['height'] = 599999
        data_in_str = json.dumps(data, indent='    ') # Сериализация

    print(data)
    print(data_in_str)
    print('\n\n')


    my_request = requests.get('https://swapi.dev/api/films/?search=A New Hope')
    data = json.loads(my_request.text)

    print(data)

    str_data = json.dumps(data, indent='    ')
    print('тут инфа по вильму:\n',str_data)
    print('\n\n')
    print('Тут текст и пред история по фильму', data['results'][0]['opening_crawl'])
