start_l = int(input("Левая граница: "))
end_l = int(input("Правая граница: "))


list_a = [i**3 for i in range(start_l, end_l+1)]
list_b = [i ** 2 for i in range(start_l, end_l + 1)]

print("Список кубов чисел в диапазоне от {0} до {1}: {2}".format(start_l, end_l, list_a))
print('Список квадратов чисел в диапазоне от {0} до {1}: {2}'.format(start_l, end_l, list_b))
