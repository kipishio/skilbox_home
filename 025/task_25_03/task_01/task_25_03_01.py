class Ship:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return 'Модель корабля {model}'.format(model=self.__model)

    def get_model(self):
        return self.__model


    def walk_on_water(self):
        print('Корабль {} идет по воде '.format(self.__model))



class Warship(Ship):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.__weapon = weapon

    def attack(self):
        print('Корабль {} атакует'.format(self.get_model(), self.__weapon))


class Cargo_Ship(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.__fullness = 0

    def submerge(self):
        self.__fullness += 1
        print('В корабль {} погрузили, загруженность: {}'.format(self.get_model(),self.__fullness))

    def unload(self):
        if  self.__fullness > 0:
           self.__fullness -= 1
        print('Корабль {} разгружают загруженность: {}'.format(self.get_model(), self.__fullness))


war_ship = Warship('QWER3', 'Пушки')
print(war_ship)
cargo_ship = Cargo_Ship('H72')
print(cargo_ship)

war_ship.attack()
cargo_ship.submerge()