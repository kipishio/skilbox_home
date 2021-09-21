import random

first_int = int(input("Укажите первое число: "))
second_int = int(input("Укажите второе число: "))
i = 0
list_square = [i for i in
               (random.randint(first_int, second_int) for _ in range(10))
               if i % 2 == 0]
print(list_square)

li = [i for i in range(first_int, second_int) if i % 2 == 0]
print(li)
