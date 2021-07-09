count_staff = int(input("Кол-во сотрудников: "))
list_staff = []
count_staff_0 = 0
for i_staff in range(count_staff):
    print("Зарплата {0} сотрудника: ".format(i_staff+1), end='')
    salary = int(input())
    list_staff.append(salary)

for i_staff in range(len(list_staff)):
    if list_staff[i_staff] == 0:
        count_staff_0 += 1

for _ in range(count_staff_0):
    list_staff.remove(0)

print("\nОсталось сотрудников: ", len(list_staff))
print("Зарплата", list_staff)

