from typing import Callable, Any

def func_1(x:int)-> int:
    return x + 10

def pr_my(text: str, number: int)-> str:
    t_my = text * number
    print(type(t_my))
    return t_my

def  func_2(func: Callable, *args, **kwargs)-> Any:
    result = func(*args, **kwargs)
    if  type(result) == int:
        return result * result
    elif type(result) == str:
        return result


print(func_2(func_1, 9))

print(func_2(pr_my, 'привет ', 5))


