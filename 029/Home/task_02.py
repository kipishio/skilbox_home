from typing import Callable
import functools

app = {}


def callback(key: str) -> Callable:
	"""
	Декоратор функция с аргументом, декорирует при инициализации функции и заносит декорируемые функции в словарь,
	где аргумент декоратора играет роль ключа в словаре
	Args:
		key: str

	Returns: Callable

	"""
	def check(func) -> Callable:
		app[key] = func

		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			return func(*args, **kwargs)

		return wrapper

	return check


@callback('//')
def example():
	print('Пример функции, которая возвращает ответ сервера')
	return 'OK'


@callback('/')
def example():
	print('Пример функции, которая возвращает ответ сервера')
	return 'Отказ'


@callback('*')
def example():
	print('Пример функции, которая возвращает ответ сервера')
	return 'Отлично'




for key, route in app.items():
	if route:
		response = route()
		print('Для ключа-"{key}":'.format(key=key, route=route ))
		print('Ответ:', response)
		print()

	else:
		print('Такого пути нет')

print()
print(example())
