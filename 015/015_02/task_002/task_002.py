count_number = int(input("Кол-во чисел в списке: "))
print()

list_number = []

for i_list_number in range(count_number):
    print("Введите {0} число: ".format(i_list_number + 1), end=' ')
    number = int(input())
    list_number.append(number)
print("\n")
divider = int(input("Введите делитель: "))

print(list_number)
print()

for i_list_number in range(count_number):
    if list_number[i_list_number] % divider == 0:
        print("Индекс числа {0}: {1}".format(list_number[i_list_number], i_list_number+1))
