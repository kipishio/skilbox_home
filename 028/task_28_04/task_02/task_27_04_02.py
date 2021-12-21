from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, coordinate_x: int, coordinate_y: int, length: int, width: int):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.length = length
        self.width = width

    def print_info(self):
        print('Класс {class_}, точка координат({x};{y}), длина = {length}, ширина = {width}'.format(
            class_=self.__class__.__name__,
            x=self.coordinate_x, y=self.coordinate_y,
            length=self.length, width=self.width))

    def move(self, edit_x: int, edit_y: int):
        self.coordinate_x = edit_x
        self.coordinate_y = edit_y


class Resize_Mixed_Square:
    def resize(self, size: int):
        self.length = size
        self.width = size

class Resize_Mixed_Rectangle:
    def resize(self, length: int, width: int):
        self.length = length
        self.width = width

class Rectangle(Figure, Resize_Mixed_Rectangle):
    """ Прямоугольник. Родительский класс: Figure """
    pass


class Square(Figure, Resize_Mixed_Square):
    """ Квадрат. Родительский класс: Figure """

    def __init__(self, coordinate_x: int, coordinate_y: int, size: int):
        super().__init__(coordinate_x, coordinate_y, size, size)


kvadrat = Square(coordinate_x=1, coordinate_y=2, size=5)
kvadrat.print_info()
kvadrat.move(edit_x=12, edit_y=16)
kvadrat.resize(size=8)
kvadrat.print_info()
print()

pryamougolnik = Rectangle(coordinate_x=3,coordinate_y=3, length=8, width=4)
pryamougolnik.print_info()
pryamougolnik.move(edit_x=4, edit_y=7)
pryamougolnik.resize(length=5, width=2)
pryamougolnik.print_info()
