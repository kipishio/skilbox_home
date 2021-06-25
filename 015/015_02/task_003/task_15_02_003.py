nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

maximum = nums_list[0]
maximum_i = 0

minimum = nums_list[0]
minimum_i = 0

for i in nums_list:

    if maximum < i:
        maximum = i

    if minimum > i:
        minimum = i

for i_list in range(N):
    if nums_list[i_list] == maximum:
        maximum_i = i_list
    elif nums_list[i_list] == minimum:
        minimum_i = i_list

nums_list[maximum_i], nums_list[minimum_i] = minimum, maximum

print(nums_list)
