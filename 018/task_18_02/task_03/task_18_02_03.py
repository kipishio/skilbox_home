def proverka(numbs, number):
    if numbs == 1:
        if number > 255 or number < 1:
            numbs -= 1
            print("не верный диапазон укажите число снова")
            return numbs
        else:
            number_list.append(number)
            return numbs
    else:
        if number > 255 or number < 0:
            numbs -= 1
            print("не верный диапазон укажите число снова")
            return numbs
        else:
            number_list.append(number)
            return numbs


print("Введите ip адрес:")
print('IP-адрес компьютера состоит из 4 чисел, разделённых точкой. \n'
      'Каждое число находится в диапазоне от 0 до 255 (включительно).')
number_list = []
number_ip = 0
numb = 1
print()

while numb <= 4:
    number = int(input("Введите {0}-е число: ".format(numb)))
    numb = proverka(numb, number)
    numb += 1

print("ip равен {0}.{1}.{2}.{3} ".format(number_list[0], number_list[1], number_list[2], number_list[3]))

