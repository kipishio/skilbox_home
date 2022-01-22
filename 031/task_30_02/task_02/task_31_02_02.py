import re

if __name__ == '__main__':


	text = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?'

	result = re.compile(r'\\wwood\+\?,')
	result = result.findall(text)
	print(result)
