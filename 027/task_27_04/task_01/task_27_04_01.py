from typing import Callable, Optional


def sandwich_buns(func: Callable) -> Callable:
    def wrapped(*args: Optional, **kwargs: Optional)->None:
        print('/----------\\')
        func(*args, **kwargs)
        print('<\______/>')

    return wrapped


def sandwich_ingredients(func: Callable) -> Callable:
    def wrapper(*args: Optional, **kwargs: Optional)->None:
        print('Помидор')
        func(*args, *kwargs)
        print('салат')

    return wrapper


@sandwich_buns
@sandwich_ingredients
def sandwich_meat()->None:
    print('Mykolas')


my_f = sandwich_meat()
