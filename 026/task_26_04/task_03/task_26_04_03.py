import math

class  Primes:
    def __init__(self, number):
        self.__number = number
        self.__start = 0
        self.result = 0
        self.count = int(math.sqrt(self.__number))+1
        self.list_number = [i for i in range(2, self.__number)]

        for i in range(2, self.count):
            for j in range(len(self.list_number)):
                if self.list_number[j] % i == 0:
                    if self.list_number[j] != i:
                        self.list_number[j] = 1
            self.list_number = set(self.list_number)
            self.list_number = list(self.list_number)
        self.list_number = sorted(self.list_number)
        self.len_list = len(self.list_number)


    def __iter__(self):
        self.__start = 0
        self.result = 0
        self.count = int(math.sqrt(self.__number)) + 1

        self.list_number = [i for i in range(2, self.__number)]

        for i in range(2, self.count):
            for j in range(len(self.list_number)):
                if self.list_number[j] % i == 0:
                    if self.list_number[j] != i:
                        self.list_number[j] = 1
            self.list_number = set(self.list_number)
            self.list_number = list(self.list_number)
        self.list_number = sorted(self.list_number)
        self.len_list = len(self.list_number)

        return self

    def __next__(self):
        if self.__start < self.len_list:
            self.result = self.list_number[self.__start]
            self.__start += 1
            return self.result
        else:
            raise StopIteration




prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')

# print()
#
# for i_elem in prime_nums:
#     print(i_elem, end=' ')