import re


if __name__ == '__main__':
	text = "Even if they are djinns, I will get djinns that can outdjinn them."

	pattern = r"\b[AaEeIiOoUuYy]\w*"

	result = re.findall(pattern, text)
	print(result)

	pattern1 = r"\b[^AaEeIiOoUuYy]\w*"

	my_re_comp = re.compile(pattern1)
	result1 = my_re_comp.findall(text)

	print(result1)
#123456