
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f'{self.name} говорит: Гав-Гав!')


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f'{self.name} говорит: Мяу!')


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)

    def get_all_animals(self):
        return self.__animals


def animal_sound(animal):
    animal_sound(animal)

# полиморфизм это потому что этот медот сам решает
# что ему выводить исходя из контекста,
# то есть вызываем один и тотже метод,
# но для разных вводных он работает по разному


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)

zoo = Zoo("Городской зоопарк")

zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)

print(zoo.get_animals_count())

for animal in zoo.get_all_animals():
    animal.make_sound()

# # 11) Попробуйте создать объект Animal() напрямую — объясните в комментарии,
# что произошло и почему
# # tiger1 = Animal("tiger", 3)
# # я надеюсь ты это имел ввиду, но таелать то не можем же,
# потомучто класс Animal не принимает у нас атрибуты это абстрактный класс
