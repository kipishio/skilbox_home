from typing import Callable, Dict, Optional
import functools

PLAGINS: Dict[str, Callable] = dict()


def register_api(func: Optional) -> Callable:
    PLAGINS[func.__name__] = func
    return func


def doo_any(func: Optional) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Optional, **kwargs: Optional):
        print('Привет Дед Мороз!')
        result = func(*args, **kwargs)
        return result

    return wrapper


@register_api
@doo_any
def hello_all(name):
    return 'Привет {name}!!!'.format(name=name)


@register_api
def bye_all(name):
    return "Всем {name}!!!".format(name=name)


print(PLAGINS)

print(hello_all('Петя'))
print(bye_all('Вася'))
