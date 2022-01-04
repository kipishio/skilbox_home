from collections.abc import Callable
import functools

def repeat(count: int = 1) -> Callable:
	def do_twice(func: Callable) -> Callable:

		@functools.wraps(func)
		def wraper(*args, **kwargs) -> None:
			for i in range(count):
				func(*args, **kwargs)
		return wraper

	return do_twice


@repeat(8)
def my_print(text: str) -> None:
	print(text)


my_print('Privet')
