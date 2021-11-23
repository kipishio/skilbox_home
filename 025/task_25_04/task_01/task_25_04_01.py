class Unit:
    def __init__(self, hitpoint):
        self.__hitpoint = hitpoint
        self.__damage = 0

    def __str__(self):
        return 'Здоровье: {hitpoint} Урон: {damage}'.format(hitpoint=self.__hitpoint, damage=self.__damage)

    def set_damage(self):
        self.__damage = 0

    def get_damage(self):
        return self.__damage

    def get_hitpoint(self):
        return self.__hitpoint


class Soldier(Unit):
    def __init__(self, hitpoint):
        super().__init__(hitpoint)
        self.__damage = 0

    def set_damage(self, damage):
        self.__damage += damage

    def __str__(self):
        return 'Солдат: Здоровье: {hitpoint} Урон: {damage}'.format(hitpoint=self.get_hitpoint(), damage=self.__damage)


class Citizen(Unit):
    def __init__(self, hitpoint):
        super().__init__(hitpoint)
        self.__damage = 0

    def __str__(self):
        return 'Простой человек: Здоровье: {hitpoint}, Урон: {damage}'.format(hitpoint=self.get_hitpoint(),
                                                                              damage=self.__damage)

    def set_damage(self, damage):
        self.__damage += damage * 2


sold = Soldier(45)
print(sold)
sold.set_damage(55)
print(sold)

cit = Citizen(90)
print(cit)
cit.set_damage(20)
print(cit)
