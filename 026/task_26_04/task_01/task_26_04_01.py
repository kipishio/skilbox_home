class Сount_iterator:
    def __init__(self):
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.result = self.__counter
        self.__counter += 1
        return self.result


my_iter = Сount_iterator()

for i_elem in my_iter:

    print(i_elem)
