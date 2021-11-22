class Robot:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return 'Модель робота {}'.format(self.__model)


class Hoover(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.__garbage_bag = 0

    def operate(self):
        self.__garbage_bag += 1
        print('Робот пылесосит, заполняемость {}'.format(self.__garbage_bag))


class Military_Robot(Robot):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.__weapon = weapon

    def operate(self):
        print('Защита объекта с помощью оружия {}'.format(self.__weapon))

    def get_weapon(self):
        return self.__weapon


class Submarine(Military_Robot):
    def __init__(self, model, weapon, rude):
        super().__init__(model, weapon)
        self.__rude = rude

    def operate(self):
        print('Защита объекта с помощью оружия {}. Охрана ведется под водой на глубине {}'.format(self.get_weapon(),
                                                                                                  self.__rude))


vacuum_cleaner = Hoover('Пылесос')
vacuum_cleaner.operate()

military_robot = Military_Robot('Военный робот РБ34', 'ПушкиБушки')
military_robot.operate()

submarine = Submarine('Подводный военный робот ЕЕЕ98', 'Торпеды', 8)
submarine.operate()



