import random

def change(nums):
    nums = list(nums)
    index = random.randint(0, 5)
    value = random.randint(100, 1000)
    nums[index] = value

    return nums, value


my_nums = 1, 2, 3, 4, 5
new_nums, rand_val = change(my_nums)

print(new_nums, rand_val)

result = change(new_nums)
print(result[1])
new_nums = result[0]
rand_val += result[1]

print(new_nums, rand_val)
