import time
from collections.abc import Callable
from typing import Optional
import functools


def time_stop_sek(_func: Optional[Callable] = None, *, count_stop_sek: int = 3) -> Callable:
	"""
	Функция декоратор позволяет передать в декаратор переменную или запусить декоратор без скобок
	Args:
		_func: Optional[Callable] = None принимает сразу ссылку на декорируемую функцию если декоратор вызвать без аргументов, и делат аргумент None если в декараторе был передан аргумент
		count_stop_sek: int параметр для указания секунд задержки аыполнения программы

	Returns:Callable

	"""
	def time_decorator(func) -> Callable:
		@functools.wraps(func)
		def wrapped(*args, **kwargs) ->Callable:
			time.sleep(count_stop_sek)
			print('Отрабатывает декоратор до')
			result = func(*args, **kwargs)
			print('Отрабатывает декоратор после')
			return result
		return wrapped
	if _func is None:
		return time_decorator
	return time_decorator(_func)


@time_stop_sek
def my_print(my_txt: str = None):
	print('Функция выводит любую переданную строку: {my_txt}'.format(my_txt=my_txt))





@time_stop_sek(count_stop_sek= 5)
def your_print(my_txt: str = None):
	print('Функция your_print выводит любую переданную строку: {my_txt}'.format(my_txt=my_txt))

@time_stop_sek(count_stop_sek=1)
def roman(qq):
	print('Функция roman ', qq)


my_print('Бам')
print()

your_print('Programmer')
print()
roman(55)
