"""
 Задание 19.

Приведите примеры кода, реализующие наследование вариаций, наследование с конкретизацией и структурное наследование.
"""


# Наследования вариаций
class Person():
    def run(self):
        print('I\'m running!')


# насколько я понял это наследование функциональной вариацией
class Sportsman(Person):
    def run(self):
        print('I\'m running faster!')


# а так будет выглядеть наследование с вариацией типа
class DopedSportsman(Person):
    def run(self, dope):
        print(f'I\'m drinking {dope}')
        print('I\'m the fastest, but WADA wants to disqualify me')


# Наследование с конкретизацией (reification inheritance)
class Room():
    def meet_a_hero(self, hero):
        raise NotImplementedError


class BattleRoom(Room):
    def meet_a_hero(self, hero):
        print('battle occurred')
        print(f'{hero} won!')
        print(f'{hero} takes treasure')


class ScenarioRoom():
    def meet_a_hero(self, hero):
        print(f'{hero} trapped')
        print('Puzzle was solwed')
        print(f'{hero} takes treasure')


# Структурное наследование (structure inheritance)

# если я правильно понимаю, то таким примером могут служить "статусы", взаимодействующие с "существами"
# предположим у нас есть статус, который принимает объект, проверяет его сопротивляемость и наносит урон за каждый ход

class DamageOverTime():
    def __init__(self, element, duration, damage):
        self.element = element
        self.duration = duration
        self.damage = damage

    def tick(self, creature):
        resistance = creature.resistances.get(self.element, 0)
        creature.hp -= (self.damage - resistance)
        self.duration -= 1

    def __str__(self):
        return f'{self.element}'

    def __repr__(self):
        return f'{self.element}'


# полученный класс мы сможем применять на любое создание с показателем hp. Механизм реализующий такие статусы можно
# расположить в самом базовом классе Creature, а можно вынести отдельно. Тогда любое существо становилось по
# сути открытой структурой отличающейся лишь наборами атрибутов,
# содержащих другие классы. В таком разрезе оказывалось, что между главным героем и гоблином гораздо больше общего)
class Creature():
    def __init__(self):
        self.hp = 80
        self.resistances = {}
        self.statuses = []

    def end_turn(self):
        for status in self.statuses.copy():
            status.tick(self)
            if status.duration <= 0:
                self.statuses.remove(status)


"""
>>> hero = Creature()
>>> poisoned = DamageOverTime('poison', 1, 15)
>>> hero.statuses.append(poisoned)
>>> print(hero.statuses)
[poison]
>>> hero.end_turn()
>>> print(hero.hp)
65
>>> print(hero.statuses)
[]
"""
