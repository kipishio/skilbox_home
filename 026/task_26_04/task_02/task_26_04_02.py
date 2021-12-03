import random

class MyIter:
    def __init__(self, number):
        self.__start_number = 0
        self.__end_number = 0
        self.__count = number
        self.__counter = 0

    def __iter__(self):
        self.__start_number = 0
        self.__end_number = 0
        self.__counter = 0
        return self



    def __next__(self):
        if self.__counter < self.__count:
            self.__counter += 1
            self.__start_number = random.uniform(0, 1)
            self.__end_number, self.__start_number = self.__start_number + self.__end_number, self.__start_number
            return self.__end_number
        else:
            raise StopIteration


cou = int(input('Введите количество элементов: '))
my_iter = MyIter(cou)

for i_iter in my_iter:
    print(i_iter)

