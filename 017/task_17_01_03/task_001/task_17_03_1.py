import random

first_int = int(input("Укажите первое число: "))
second_int = int(input("Укажите второе число: "))

list_square = [x ** 2 for x in range(first_int, second_int) if x % 2 == 0]
print(list_square)
