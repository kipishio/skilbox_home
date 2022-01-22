import re
from re import search

if __name__ == '__main__':
	text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'


	result = re.match(r'wo', text)
	print('01 ', result)

	pattern = re.compile('wo')
	result = pattern.match(text)
	print('01 ',result)

	print()

	result = re.search(r'wo', text)
	print('02 ', result)
	print('02 ', result.group(0))
	print('02 ', result.start())
	print('02 ', result.end())

	print()

	pattern = re.compile('wo')
	result = pattern.search(text)
	print('03 ', result)
	print('03 ', result.group(0))
	print('03 ', result.start())
	print('03 ', result.end())
	print()



	result = re.findall(r'wo', text)
	print('04 ', result)
	print()

	result = re.search(r'wo', text)
	print('05 ', result)
	print(result.group(0))

	result = re.sub(r'wo', 'Замена', text)
	print('06 ', result)
