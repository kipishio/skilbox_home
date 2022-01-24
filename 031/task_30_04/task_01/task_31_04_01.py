import requests
import re


if __name__ == '__main__':
	rq = requests.get('https://swapi.dev/api/planets/3/')
	print(rq)
	print(rq.text)
