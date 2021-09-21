import random
laine = 20
list_my = [random.randint(5, 15) for i in range(random.randint(1, laine))]

a_my = random.randint(0, len(list_my))
b_my = random.randint(0, len(list_my))

if a_my > b_my:
    a_my, b_my = b_my, a_my

print(list_my,'\n')
print("Длина списка ", len(list_my))
print("Диапазон равен от {0} до {1}".format(a_my, b_my))


list_my = [(0 if a_my <= i <= b_my else list_my[i]) for i in range(len(list_my))]

print('Результат обработки списка:')
print(list_my)

