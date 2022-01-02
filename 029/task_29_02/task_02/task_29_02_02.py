from collections.abc import Iterable
from contextlib import contextmanager
import os


@contextmanager
def in_dir(path) -> Iterable:
	"""
	Функция генератор, задекорированная для того чтоб еще ее сделать и контекстным менеджером
	Args:
		path: str путь к директориям или файлам

	Returns: None
	"""
	try:
		yield
	except Exception as my_ex:
		print('Описение ошибки {my_ex}'.format(my_ex=my_ex))
	finally:
		if os.path.exists(path):
			print('тут все папки из указанного пути {path}: {list_dir}'.format(path=path, list_dir=os.listdir(path)))
		else:
			print('Пути который вы указали {path}, не существует'.format(path=path))
			print("Текущий путь {my_path}".format(my_path=os.path.abspath('')))
			print('Внутри файлы и папки: {list_dir}'.format(list_dir=os.listdir(os.path.abspath(''))))


with in_dir('C:\\') as dir_1:
	pass
