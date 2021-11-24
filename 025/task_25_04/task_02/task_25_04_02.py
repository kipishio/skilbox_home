class Can_Fly:
    def __init__(self):
        self.__height = 0
        self.__speed = 0

    def take_off(self): # Взлететь
        pass

    def fly(self): # Лететь
        pass

    def to_land(self):
        self.__height = 0
        self.__speed = 0

    def get_hight(self):
        return self.__height

    def set_hight(self, hight):
        self.__height = hight

    def get__speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed += speed



class Butterfly(Can_Fly):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'Бабочка, Скорость: {}, Высота: {}'.format(self.get__speed(), self.get_hight())

    def take_off(self):
        self.set_hight(1)

    def fly(self):
        self.set_speed(0.5)


class Rocket(Can_Fly):
    def __str__(self):
        return 'Ракета, Скорость: {}, Высота: {}'.format(self.get__speed(), self.get_hight())

    def take_off(self):
        self.set_hight(500)
        self.set_speed(1000)


    def to_land(self):
        super().to_land()
        print('Взрыв ракеты')


butterfly = Butterfly()
print(butterfly)

butterfly.take_off()
print(butterfly)

butterfly.fly()
print(butterfly)

butterfly.to_land()
print(butterfly)
print()

rocket = Rocket()
print(rocket)

rocket.take_off()
print(rocket)

rocket.to_land()
print(rocket)


