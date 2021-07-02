num_list = [5, 6, 8, 12, 85, 99]
#num_list = [99, 85, 12, 8, 6, 5]

new_num_list = []
for i_nums_list in range(len(num_list)-1, -1, -1):
    new_num_list.append(num_list[i_nums_list])
    print(num_list[i_nums_list])
num_list = new_num_list
print(num_list)
