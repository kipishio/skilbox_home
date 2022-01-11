
# import functools
# from typing import Callable

import functools
def decor_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('До')
        result = func(*args, **kwargs)
        print('После')
        return result
    return  wrapper


def decor_cls(cls):
    print('1112', cls)
    for i_named_func in dir(cls):
        if i_named_func.startswith('__') is False:
            new_func = decor_func(getattr(cls, i_named_func))
            print('********',new_func)
            setattr(cls, i_named_func, new_func)

        @functools.wraps(cls)
        def wrapper(*args, **kwargs):
            print('11')
            print('1113', cls)
            # return cls

        return wrapper
    return decor_cls

@decor_cls
class A:

    def sest1(self):
        print('test1 в деле')

    def sest2(self):
        print('test2 в деле')

@decor_cls('man')
class  B(A):

    # def sest1(self):
    #     super(B, self).sest1()
    #     print('test1 в деле')

    def sest3(self):
        print('test3 в деле')

    def sest4(self):
        print('test4 в деле')

my_a = A()
my_a.sest1()
my_a.sest2()

my_b = B()
my_b.sest2()
my_b.sest4()
my_b.sest3()
# print(dir(B()))
print(B)
print(B())