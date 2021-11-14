class Avto:
    def __init__(self, name, color, price, maximum_speed, current_speed=0):
        self.name = name
        self.color = color
        self.price = price
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed

    def info_avto(self):
        print('Модель автомобиля: {}\nЦвет: {}\nСтоимость: {}\nМаксимальная скорость:{}\nТекущая скорость: {}'.format(
            self.name, self.color, self.price, self.maximum_speed, self.current_speed))

    def edit_current_speed(self, speed):
        self.current_speed = speed
        print('Изменилась текущая скорость {}'.format(self.current_speed))


avto_01 = Avto('Toyota', "Red", '1 милльион', '200 km')
avto_01.info_avto()
print('\n')
avto_01.edit_current_speed(120)
avto_01.info_avto()
