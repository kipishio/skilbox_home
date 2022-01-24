import requests
import re
import json

if __name__ == '__main__':
	rq = requests.get('https://swapi.dev/api/people/3/')
	#
	# print(rq)
	# print(rq.text)

	data = json.loads(rq.text)  # Десериализация JSON
	data['name'] = 'Роман'
	# print(data['name'])
	# print(data['homeworld'])
	# print(data)
	with open('my_request_file.json', 'w') as file:
		json.dump(data, file, indent='    ')  # Сериализация JSON


	with open('my_request_file.json', 'r') as file:
		data = json.load(file)
		print(data)

