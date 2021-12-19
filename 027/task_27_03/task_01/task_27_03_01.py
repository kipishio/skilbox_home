from typing import Callable, Any


def do_twice(func: Callable) -> Callable:
    """
    Декоратор, выполняет декорируемую функцию два раза
    :param func: Callable
    :return: Calable
    """
    def wrapper(*args: Any, **kwargs: Any) -> None:
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@do_twice
def greeting(name: str) -> None:
    """
    Функция получает текст и выводит его в консоль
    :param name: str
    :return: str
    """
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
print(do_twice.__doc__)
