file = open('task\group_1.txt', 'r', encoding='utf-8')

summa = 0
diff = 0

for i_line in file:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])
file.close()

file_2 = open('Additional_info\group_2.txt', 'r', encoding='utf-8')

compose = 1
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])
file_2.close()

print(summa)
print(diff)
print(compose)

