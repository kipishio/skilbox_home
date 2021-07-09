def coun_litter(first_list_count, second_list_count):
    first_list_count = list(first_list_count)
    second_list_count = list(second_list_count)
    count_1 = 0
    count_1 += first_list_count.count('!')
    count_1 += first_list_count.count('?')
    count_2 = 0
    count_2 += second_list_count.count('!')
    count_2 += second_list_count.count('?')

    if count_1 > count_2:
        first_list_count.append(' ')
        first_list_count.extend(second_list_count)
        return first_list_count
    elif count_1 < count_2:
        second_list_count.append(' ')
        second_list_count.extend(first_list_count)
        return second_list_count
    else:
        text_ = ['Ой']
        return text_


first_messege = input("Первое сообщение: ")
second_messege = input("Второе сообщение: ")

result = coun_litter(first_messege, second_messege)
print("Третье сообщение: ", end='')
for i_litter in range(len(result)):
    print(result[i_litter], end='')
