from collections.abc import Callable


def check_permission(permission: str) -> Callable:
	"""
	Декоратор функция, принимает аргумент str статус, и сверяет со списком которым разрешен доступ на выполнение
	декорируемой функции
		permission: str статус доступа к декорируемой функции

	Returns: Callable

	"""
	user_permissions: tuple = ('admin', 'super admin')

	def check_funk(func: Callable):
		def wrapper(*args, **kwargs):
			if permission in user_permissions:
				return func(*args, **kwargs)
			else:
				print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func_name}'.format(
					func_name=func.__name__))

		return wrapper

	return check_funk


@check_permission('admin')
def delete_site() -> None:
	print('Удаляем сайт')


@check_permission('user_1')
def add_comment() -> None:
	print('Добавляем комментарий')


print('Результат')

delete_site()
add_comment()

delete_site()
add_comment()
