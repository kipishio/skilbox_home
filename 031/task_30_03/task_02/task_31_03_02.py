import re

if __name__ == "__main__":
	text = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'

	pattern = r'\d+[-]\d+[-]\d+'

	my_re_com_pa = re.compile(pattern)

	result = my_re_com_pa.findall(text)

	print(result)
