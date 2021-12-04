import math


class Primes:
    def __init__(self, number):
        self.__count_number = number
        self.__start = 2

    def __iter__(self):
        self.__start = 2
        return self

    def __prime_number(self, numb_iter):
        self.__numb_iter = numb_iter
        self.__number_of_divisors = math.ceil(math.sqrt(self.__numb_iter))
        if self.__numb_iter == 2 or self.__numb_iter == 3:
            return True

        for i in range(2, self.__number_of_divisors + 1):
            if self.__numb_iter % i == 0:
                return False

        else:
            return True

    def __next__(self):
        self.__result = 0
        while True:
            if self.__start <= self.__count_number:
                if self.__prime_number(self.__start):
                    self.__result = self.__start
                    self.__start += 1
                    return self.__result
                else:
                    self.__start += 1

            else:
                raise StopIteration


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')

print()

for i_elem in prime_nums:
    print(i_elem, end=' ')
