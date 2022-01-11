import functools

def dec(var):

	def my_var(cls):
		@functools.wraps(cls)
		def wrapper(*args, **kwargs):
			print('До')
			cls(*args, **kwargs)
			print('После')
			print(var)
			return cls(*args, **kwargs)

		return wrapper()
	return my_var

# @dec(777)
class A:
	def test1(self):
		print('Ура')


class B(A):
	def test1(self):
		print('Ура')

def test():
	print('EEE')

a = dec(234)(A)
a = dec(444)(A)
print('a', a)

# a()

# b = dec(999)(test)
# b()
# t = A()
# print('t', t)