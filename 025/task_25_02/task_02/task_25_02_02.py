class Human:
    __count_human = 0

    def __init__(self, name, age=0):
        self.set_name(name)
        self.set_age(age)

    def __str__(self):
        return 'Класс Human. Имя {}, Возраст {}'.format(self.__name, self.__age)

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception('Ошибка имя должно состоять только из букв')

    def set_age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            raise Exception('Возраст должен быть в пределах от 0 до 100')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

hum_1 = Human('Иван', 99)

print(hum_1)
print(hum_1.get_name())
