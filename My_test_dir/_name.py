# from typing import Optional
import functools


# __name_prv = 8
#
# def my_pr():
# 	print(__name_prv)
#
# 	# __name_prv = 9
# 	# print(__name_prv)
#
# my_pr()
#
# # print(__name__)
# # print(__main__)
#
#
# class FontS():
# 	def prt(self):
# 		print('prt')
#
# 	def _qwer(self):
# 		print('qwe')
# 		self.prt()
#
# 	def rt(self):
# 		self._qwer()

def decorator_maker_with_arguments(_func=None, *, decorator_arg1='001', decorator_arg2='002'):
    print("Я создаю декораторы! И я получил следующие аргументы: ", decorator_arg1, decorator_arg2)

    def my_decorator(func):
        print("Я - декоратор. И ты всё же смог передать мне эти аргументы: {} {}".format(
            decorator_arg1, decorator_arg2))

        @functools.wraps(func)
        def wrapped(function_arg1, function_arg2):
            print("Я - обёртка вокруг декорируемой функции.\n"
                  "И я имею доступ ко всем аргументам\n"
                  "\t- и декоратора: {0} {1}\n"
                  "\t- и функции: {2} {3}\n"
                  "Теперь я могу передать нужные аргументы дальше".
                  format(decorator_arg1, decorator_arg2, function_arg1, function_arg2))
            result = func(function_arg1, function_arg2)
            return result

        return wrapped

    if _func is None:
        return my_decorator
    return my_decorator(_func)


@decorator_maker_with_arguments(decorator_arg1="Леонард", decorator_arg2="Шелдон")
def decorated_function_with_arguments(function_arg1='003', function_arg2='004'):
    print("Я - декорируемая функция и я знаю только о своих аргументах: {} {}".format(function_arg1, function_arg2))


decorated_function_with_arguments("Раджеш", "Говард")

print()

print('тест 2 пошел')


@decorator_maker_with_arguments
def decorated_function_with_arguments2(function_arg1='003', function_arg2='004'):
    print("Я - декорируемая функция и я знаю только о своих аргументах: {0} {1}".format(function_arg1, function_arg2))


decorated_function_with_arguments2("Леша", "Петя")