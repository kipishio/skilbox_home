class Avto:
    name = 'Toyota'
    color = "Red"
    price = '1 милльион'
    maximum_speed = '200 km'
    current_speed = '0'

    def info_avto(self):
        print('Модель автомобиля: {}\nЦвет: {}\nСтоимость: {}\nМаксимальная скорость:{}\nТекущая скорость: {}'.format(
            self.name, self.color, self.price, self.maximum_speed, self.current_speed))

    def edit_current_speed(self, speed):
        self.current_speed = speed
        print('Изменилась текущая скорость {}'.format(self.current_speed))


avto_01 = Avto()
avto_01.info_avto()
avto_01.edit_current_speed(120)
avto_01.info_avto()