"""
 Задание 14.
Приведите пример небольшой иерархии, где вместо некоторого поля родительского класса с набором предопределённых
значений (как в случае с полем female) применяется наследование.
"""


# У нас есть классы отвечающий за приготовление хлеба и булочек и хлебопечка, которая их задействует.
class Bread():
    def __init__(self):
        # Изначально идея была в том, что атрибуты хранящие рецепт хлеба не будут меняться и будут одинаковы для
        # всех экземпляров класса Bread, поэтому поместил их в атрибуты класса а не экземпляра. 
        self.time_to_bake_min = 10
        self.temperature = 180
        self.dough_ingridients = ['eggs', 'flour']

    def make_the_dough(self):
        self._mix_ingridients()
        self._get_dough()

    def _mix_ingridients(self):
        for ing in self.dough_ingridients:
            print(f'{ing} added')

    def _get_dough(self):
        print('What a strange dough!')

    def make_bread(self):
        self._bake()
        self._get_bread()

    def _bake(self):
        print(f'Baked {self.time_to_bake_min} min on {self.temperature}C')

    def _get_bread(self):
        print(f'What a wonderful bread!')


class BurntBun(Bread):
    def __init__(self):
        self.time_to_bake_min = 15
        self.temperature = 200
        self.dough_ingridients = ['eggs', 'flour', 'sugar']

    def _get_dough(self):
        print('Tasty dough, will we bake buns?')

    def _get_bread(self):
        print(f'We got a burnt buns! Not good!')


# Предположим у нас есть хлебопечка, которая в зависимости от класса хлеба должна выпекать хлеб.
# Мы могли бы сделать атрибут bread_type и хранить всю информацию о настройках в печке в словаре, например. Но
# это привело бы к конфликтам в таксономии.
class BreadMachine():
    """ Примеры использования класса.

    >>> a = BreadMachine()
    >>> bread = Bread()
    >>> a.set_prepack(bread)
    >>> a.make_bread()
    eggs added
    flour added
    What a strange dough!
    Baked 10 min on 180C
    What a wonderful bread!
    
    >>> bun = BurntBun()
    >>> a.set_prepack(bun)
    >>> a.make_bread()
    eggs added
    flour added
    sugar added
    Tasty dough, will we bake buns?
    Baked 15 min on 200C
    We got a burnt buns! Not good!
    """
    
    def __init__(self):
        self._bread = None

    def set_prepack(self, prepack):
        self._bread = prepack

    def make_bread(self):
        self._bread.make_the_dough()
        self._bread.make_bread()


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
