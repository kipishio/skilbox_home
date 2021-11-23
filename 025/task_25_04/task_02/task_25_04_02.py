class Can_Fly:
    def __init__(self):
        self.__height = 0
        self.__speed = 0

    def take_off(self):
        pass

    def fly(self):
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

    def take_off(self):
        self.set_hight(1)

    def fly(self):
        self.set_speed(0.5)

    def land(self):
        self.__height = 0
        self.__speed = 0