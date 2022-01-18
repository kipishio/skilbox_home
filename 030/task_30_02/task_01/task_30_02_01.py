import functools

# import locale
# from typing import Callable

counter = dict()


def log_decor(func):
    # global counter
    counter = dict()
    print(locals())
    print(globals())

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal counter
        result = func(*args, **kwargs)

        if func.__name__ in counter:
            counter[func.__name__] += 1
        else:
            counter[func.__name__] = 1

        return result

    return wrapper


@log_decor
def hello():
    print('Hello')


hello()
hello()
hello()
hello()
hello()
print(counter, '***')
print(dir())
