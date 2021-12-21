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
        self.__name = name
        self.__color = color
        self.__speed = speed

    def print_info(self):
        print('Транспорт {name}, цвет {color}, скорость {speed}.'.format(name=self.__name, color=self.__color,
                                                                         speed=self.__speed))

    @abstractmethod
    def to_ride(self) -> None:
        """Декорируемый абстрактный метод выбора езды в зависимости от класса транспорта"""
        print('Выбери свой путь!')

    def signal(self):
        """Функция вызова сигнала"""
        print("Сигнал")


class MusicMixed:
    def play_music(self) -> None:
        '''Класс примесь для расширения возможности дочерних классов'''
        print('Играет музыка!!!')


class Terrestrial(Transport):
    def to_ride(self) -> None:
        '''функция заменяет родительскую и указывает образ передвижение (ехать, плыть, ехать-плыть) в зависимости от класса'''
        print('Это наземный транспорт: ехать!')


class Water(Transport):
    def to_ride(self) -> None:
        '''функция заменяет родительскую и указывает образ передвижение (ехать, плыть, ехать-плыть) в зависимости от класса'''
        print('Это водный транспорт: плыть')


class Amphibian(Transport, MusicMixed):
    def to_ride(self) -> None:
        '''функция заменяет родительскую и указывает образ передвижение (ехать, плыть, ехать-плыть) в зависимости от класса'''
        super().to_ride()
        print('Это амфибия: ехать-плыть')


kia_rio = Terrestrial(name='Kia Rio', color='Мокрый асфальт', speed=250)
kia_rio.print_info()
kia_rio.to_ride()
kia_rio.signal()
print()

kater = Water(name='Катер', color='Красный', speed=50)
kater.print_info()
kater.to_ride()
kater.signal()
print()

amfib_drozd = Amphibian(name='Амфибия Дрозд', color='Черный', speed=70)
amfib_drozd.print_info()
# amfib_drozd.to_ride()
amfib_drozd.signal()
amfib_drozd.play_music()

print('Вывод MRO дл я класса {class_name}, MRO = {mro_print}'.format(class_name=amfib_drozd.__class__.__name__,
                                                                     mro_print=amfib_drozd.__class__.__mro__))
