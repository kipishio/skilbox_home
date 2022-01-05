from collections.abc import Callable
import functools
# from datetime import datetime
import time


def time_work(func):
	# print('начал работу time_work')

	def wrapped(*args, **kwargs):
		# print('начал работу wrapped от time_work')
		start_time = time.time()
		result = func(*args, **kwargs)
		time_work = time.time() - start_time
		print('Время работы программы {time_work}'.format(time_work=time_work))
		return result

	return wrapped


def decor_work(_cls=None, *, decorator: Callable) -> Callable:
	"""
	Декоратор передает в декоратор функцию через аргумент decorator, и возвращает настоящую уже декорирующую функцию
	re_adress()
	Args:
		_cls:
		decorator: Callable

	Returns:

	"""
	# print('Начал работу декоратор decor_work')
	# print('_cls= ', _cls)

	def re_adress(cls: Callable) -> Callable:
		"""
		Декоратор функция декорирует класс, изменяет его функции которые не начинаются с "__" декорирует их и заворачивает
		в них счетчик времени из функции time_work и передает ссылку в работу в функцию wrapped()
		Args:
			cls: Callable принимает ссылку на класс

		Returns: Callable ничего не возвращает

		"""
		# print('Начал работу re_adress, принял класс от {cls}'.format(cls=cls))
		for i_named_method in dir(cls):
			if i_named_method.startswith('__') is False:
				get_func = getattr(cls, i_named_method)
				# print('присваиваем декоратор классу')
				decorated_func = decorator(get_func)
				setattr(cls, i_named_method, decorated_func)
				# print('присвоили')

		@functools.wraps(decorator)
		def wrapped(*args, **kwargs) -> Callable:
			"""
			декоратор функция принимает класс(сылка) с измененными методами класса, и заворачивает ссылку на класс в
			обявление объекта через эту ссылку и принимает и передает объекты в этот класс
			Args:
				*args: если есть аргументы то при объявлении объекта передает эти аргументы ему
				**kwargs: если есть аргументы то при объявлении объекта передает эти аргументы ему

			Returns: Callable возвращает объект класса

			"""
			# print('Начал работу wrapped от re_adress')
			result = cls(*args, **kwargs)

			# print('Результат: ', result)
			return result

		return wrapped

	if _cls is None:
		return re_adress
	return re_adress(_cls)


@decor_work(decorator=time_work)
class MyKlass:
	log = 1

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

print()
print('*' * 140)
my_klass2 = MyKlass()
my_klass2.test1()
my_klass2.test2()
my_klass2.test3()

print()
print('*' * 140)
my_klass3 = MyKlass()
my_klass3.test1()
my_klass3.test2()
my_klass3.test3()

print()
print(id(my_klass1))
print(id(my_klass2))
print(id(my_klass3))

print()
print(my_klass1)
print(my_klass2)
print(my_klass3)
print(my_klass3.log)
