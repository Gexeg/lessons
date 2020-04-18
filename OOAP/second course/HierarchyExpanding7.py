"""
 Задание 14.
Приведите пример небольшой иерархии, где вместо некоторого поля родительского класса с набором предопределённых
значений (как в случае с полем female) применяется наследование.
"""


class Bread():
    time_to_bake_min = 10
    temperature = 150

    def get_baking_settings(self):
        return self.time_to_bake_min, self.temperature


# Предположим у нас есть хлебопечка, которая в зависимости от класса хлеба должна выставлять таймер и температуру
# Мы могли бы сделать атрибут bread_type и хранить всю информацию о настройках в печке в словаре, например.
# Можем решить этот вопрос наследованием. Тогда печка будет просто получать необходимые настройки от наследников.

class BurntBread(Bread):
    time_to_bake_min = 15
    temperature = 200


class HalfBakedBread(Bread):
    time_to_bake_min = 5
    temperature = 100


"""
 Задание 15.

Если используемый вами язык программирования это допускает,
напишите примеры полиморфного и ковариантного вызовов метода.
"""

# Полиморфный вызов. Представим, у нас есть класс:


class Person():
    def walk(self):
        print('Yes, i can walk...')


# и есть его наследник, расширяющий функционал класса-предка новыми методами
class Baker(Person):
    def bake(self):
        print('and bake!')


somebody = Baker()

# Насколько я понял, с полиморфным вызовом все достаточно просто и вызов метода,
# не представленного у класса-наследника, но определенного у предка будет полиморфным. Т.к. тип Baker
# ведет себя как тип Person при вызове этого метода.
somebody.walk()

# С ковариантным вызовом все как всегда сложнее. Возьмем пример с ящиком из прошлых модулей.
from typing import Generic, TypeVar, Callable

animal = TypeVar('animal', covariant=True)


# у нас есть небольшая иерархия классов
class Animal():
    def make_sound(self):
        raise NotImplementedError


class Cat(Animal):
    def make_sound(self):
        print('Meow!')


class Dog(Animal):
    def make_sound(self):
        print('Woof!')


# ящик на вход принимает любой объект типа животное.
class Box(Generic[animal]):
    def __init__(self, content: animal) -> None:
        self._content = content

    def make_sound(self):
        self._content.make_sound()


# Метод взаимодействует с ящиком, который хранит некое значение, принадлежащее к иерархии Animal.
# Насколько я понял, так и будет выглядеть ковариантный вызов метода
def shake_box(box: Box[Animal]):
    box.make_sound()


# Проблемы могут возникнуть при более сложных иерархиях и многократных вызовах присваивания some_animal
# мы не можем быть уверены на какой именно класс животных ссылается переменная и чей метод будет вызван
# если учитывать полиморфизм.
some_animal = Cat()
box = Box(some_animal)
shake_box(box)
