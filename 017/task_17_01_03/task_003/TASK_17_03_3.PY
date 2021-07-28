import random

damage_1 = [random.randint(50, 80) for _ in range(10)]
damage_2 = [random.randint(30, 60) for _ in range(10)]

damage_3 = [("Погиб" if damage_1[i] + damage_2[i] > 100 else "Выжил") for i in range(10)]

print('Первый список монстров', damage_1)
print('Второй список монстров', damage_2)
print('Третий список монстров', damage_3)
