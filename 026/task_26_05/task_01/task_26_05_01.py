import math


# def fibonacci(number):
#     cur_val = 0
#     next_val = 1
#     for _ in range(number):
#         yield cur_val
#         cur_val, next_val = next_val, cur_val + next_val
#         if cur_val > 10 ** 6:
#             return
#
#
# def square(nums):
#     for num in nums:
#         yield num ** 2
#
#
# print(sum(square(fibonacci(6))))

def count_iterator():
    counter = 1

    def prime_number(numb_iter):
        number_of_divisors = math.ceil(math.sqrt(numb_iter))
        if numb_iter < 2:
            return numb_iter
        elif numb_iter == 2 or numb_iter == 3:
            return 'Простое число {}'.format(numb_iter)

        elif numb_iter > 3:
            for i in range(2, number_of_divisors + 1):
                if numb_iter % i == 0:
                    return numb_iter
            else:
                return 'Простое число {}'.format(numb_iter)

    while True:
        yield prime_number(counter)
        counter += 1


for i in count_iterator():
    print(i)
