from typing import List


class Person:

    def __init__(self, name: str, surname: str, age: int) -> None:
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname) -> None:
        self.__surname = surname

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        self.__age = age


user1 = Person('Матроскин', 'Иванов', 20)
user2 = Person('Шарик', 'Петров', 23)
user3 = Person('Лунтик', 'Сидоров', 18)
list_user = [user1, user2, user3]
list_sortd = sorted(list_user, key=lambda elem: elem.age)

for i_elem in list_sortd:
    print(i_elem.name)

