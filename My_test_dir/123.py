from collections.abc import Callable
import functools
from datetime import datetime
import time


def first(cls):
	print('начал работу first')
	def wrapped(*args, **kwargs):
		print('начал работу wrapped wrapped от first')
		inst = cls(*args, **kwargs)
		print('Время создани инстанса: ', datetime.utcnow())
		return inst

	return wrapped


def time_work(func):
	print('начал работу time_work')

	def wrapped(*args, **kwargs):
		print('начал работу wrapped от time_work')
		start_time = time.time()
		result = func(*args, **kwargs)
		time_work = time.time() - start_time
		print('Время работы программы {time_work}'.format(time_work=time_work))
		return result

	return wrapped


def decor_work(decorator: Callable):
	print('Начал работу декоратор decor_work')

	@functools.wraps(decorator)
	def wrapped(cls):
		print('Начал работу wrapped от decor_work')
		for i_named_method in dir(cls):
			if i_named_method.startswith('__') is False:
				get_func = getattr(cls, i_named_method)
				print('присваиваем декоратор классу')
				decorated_func = decorator(get_func)
				setattr(cls, i_named_method, decorated_func)
				print('присвоили')

		result = cls
		print('результат', result)
		return result

	return wrapped


# @first
@decor_work(decorator=time_work)
class MyKlass:

	def __init__(self):
		self.text = "Примет я класс {}".format(self.__class__.__name__)

	def test1(self):
		numb = 2000 * 10000 ** 1000000
		print('test1')
		return numb

	def test2(self):
		numb = 2000 * 10000 ** 1000000
		print('test2')
		return numb

	def test3(self):
		numb = 2000 * 10000 ** 100000
		print('test3')
		return numb


print()

my_klass1 = MyKlass()
print('*' * 140)
my_klass1.test1()
my_klass1.test2()
my_klass1.test3()
#
print()
print('*' * 140)
my_klass2 = MyKlass()
my_klass2.test1()
my_klass2.test2()
my_klass2.test3()
#
# print()
# print('*' * 140)
# my_klass3 = MyKlass()
# my_klass3.test1()
# my_klass3.test2()
# my_klass3.test3()
#
# my_klass1.test3()
# print(id(my_klass1))
# print(id(my_klass2))
# print(id(my_klass3))
#
# print(my_klass1)
# print(my_klass2)
# print(my_klass3)
