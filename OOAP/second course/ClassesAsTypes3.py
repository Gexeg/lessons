"""
Задание 7.
Приведите пример кода с комментариями, где применяется динамическое связывание. 
"""

# В Python, насколько я понимаю в принципе нет статического связывания. В обычном случае, не ввязываясь в магию
# метаклассов мы даже не можем запретить переопределение методов. Так же предполагается, что в нормальных условиях мы не
# будем реботать с компилятором.


class A():
    def some_method(self):
        print('A method')


class B():
    def some_method(self):
        print('B method')


inst = B()
# применяем метод класса B(), переопределенный от A()
inst.some_method()

"""
Задание 8.
Приведите примеры кода с ковариантностью и контравариантностью, если ваш язык программирования это позволяет. 
"""

# До этого задания не копался с mypy так глубоко, но оказывается там и такое есть :)
# Получается, что мы можем определять общие типы и на их основании выстраивать поведение.
# Один из самых частых для ковариации примеров - контейры. В документации в примерах часто упоминаются list, tuple. 

from typing import Generic, TypeVar, Callable

animal = TypeVar('animal', covariant=True)


class Animal():
    pass


class Cat(Animal):
    pass


# ящик на вход принимает любой объект типа животное
class Box(Generic[animal]):
    def __init__(self, content: animal) -> None:
        self._content = content


# мы можем проверить ящик с животным, а значит и с котом, как частным случаем животного.
def check_box(box: Box[Animal]):
    pass


box = Box(Cat())
check_box(box)

# с контравариантностью немного сложнее. Здесь я не совсем понял как прикрутить Generic в mypy.
# Ковариантным типом по документации является Callable. Подразумевается, что если нам доступна операция над потомком,
# значит нам доступна эта же операция над предком, но не наоборот.


class Person():
    pass


# У нас есть 2 наследника класса Person.
class Sportsman(Person):
    pass


class Policeman(Person):
    pass


def person_run(person: Person) -> None:
    print('Person running')


# Они оба в том или ином виде могут бегать. 
def sportsman_run(sportsman: Sportsman) -> None:
    print('Sportsman running. So fast!')


def policeman_run(policeman: Policeman) -> None:
    print('The policemen don\'t run. He shoots.')


# Функция ожидает метод, взаимодействующий со Sportsman
def make_sportsman_run(sportsman: Sportsman, run_func: Callable[[Sportsman], None]):
    print('Shoot in the air with gun!')
    run_func(sportsman)


# но и обычный Person подходит.
make_sportsman_run(Sportsman(), person_run)

# А вот Policeman уже более специализированная версия, с ним так просто не побегаешь. Mypy тут выдаст ошибку.
make_sportsman_run(Sportsman(), policeman_run)
