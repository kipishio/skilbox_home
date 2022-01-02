from abc import ABC, abstractmethod


class Transport(ABC):
    """Класс транспорт, абстрактный класс для всех видов транспорта"""

    def __init__(self, name: str, color: str, speed: int) -> None:
        """
        Конструктор класса инициализирует имя, цвет, скорость - транспортного средства
        :param name: str
        :param color: str
        :param speed: int
        """
        self.name = name
        self.color = color
        self.speed = speed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: str):
        self._color = color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed: int):
        self._speed = speed

    def __str__(self):
        return 'Транспорт {name}, цвет {color}, скорость {speed}.'.format(name=self._name, color=self._color,
                                                                          speed=self._speed)

    @abstractmethod
    def to_ride(self) -> None:
        """Декорируемый абстрактный метод выбора езды в зависимости от класса транспорта"""
        print('Выбери свой путь!')

    @classmethod
    def signal(cls) -> None:
        """Функция вызова сигнала"""
        print("Сигнал")


class MusicMixed:

    @classmethod
    def play_music(cls) -> None:
        """Класс примесь для расширения возможности дочерних классов"""
        print('Играет музыка!!!')


class Terrestrial(Transport):
    def to_ride(self) -> None:
        """функция заменяет родительскую и указывает образ передвижение (ехать, плыть, ехать-плыть) в зависимости от
        класса"""
        print('Это наземный транспорт: ехать!')


class Water(Transport):
    def to_ride(self) -> None:
        """функция заменяет родительскую и указывает образ передвижение (ехать, плыть, ехать-плыть) в зависимости от
        класса"""
        print('Это водный транспорт: плыть')


class Amphibian(Transport, MusicMixed):
    def to_ride(self) -> None:
        """функция заменяет родительскую и указывает образ передвижение (ехать, плыть, ехать-плыть) в зависимости от
        класса"""
        super().to_ride()
        print('Это амфибия: ехать-плыть')


kia_rio = Terrestrial(name='Kia Rio', color='Мокрый асфальт', speed=250)
print(kia_rio)
kia_rio.to_ride()
kia_rio.signal()
print()

kater = Water(name='Катер', color='Красный', speed=50)
print(kater)
kater.to_ride()
kater.signal()
print()

amfib_drozd = Amphibian(name='Амфибия Дрозд', color='Черный', speed=70)
print(amfib_drozd)
amfib_drozd.to_ride()
amfib_drozd.signal()
amfib_drozd.play_music()
print()
print('Вывод MRO дл я класса {class_name}, MRO = {mro_print}'.format(class_name=amfib_drozd.__class__.__name__,
                                                                     mro_print=amfib_drozd.__class__.__mro__))
print(kia_rio.speed)
print(kia_rio.color)
kia_rio.color = 'Супер красный'
kia_rio.speed = 300
print(kia_rio)
