import requests

response = requests.get('https://api.github.com/search/repositories', params={'q': 'requests+language:python'}, )
# response = requests.get('https://yandex.ru/search/?text=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD+%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%B0+request+%D0%BE%D0%BD%D0%BB%D0%B0%D0%BD%D0%B9&lr=55')
# print(response.text)

json_response = response.json()
repository = json_response['items'][0]
# print(json_response['items'][0])
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')
