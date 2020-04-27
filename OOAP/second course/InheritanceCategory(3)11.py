"""
 Задание 20.

Приведите пример кода, где выполняется наследование реализации и льготное наследование.

Отправьте выполненное задание на сервер.
"""
# Наследование реализации (implementation inheritance)


# вернемся к классу "Существо".
class Creature():
    def __init__(self, hp):
        self.hp = hp
        self.resistances = {}
        self.statuses = []

    def end_turn(self):
        for status in self.statuses.copy():
            status.tick(self)
            if status.duration <= 0:
                self.statuses.remove(status)


# Предположим мы захотим создать новое существо. Геймдизайнер решил, что идеальной будет раса, которая накапливает
# статусы и не расходует их перенося в своем теле. В какой-то момент они могут "переключить рубильник" и начать получать
# позитивные и негативные эффекты
class AnotherCreature(Creature):
    def __init__(self, hp):
        super().__init__(hp)
        self.suppress = True

    def end_turn(self):
        if not self.suppress:
            super().end_turn

# реализация достаточно ужасна, но вроде передает смысл.
# вместе с характеристиками мы притащили за собой реализацию хранилища статусов в виде стандартного Python list.
# Это будет накладывать определенные ограничения и на количество переносимых статусов. Если такой герой всю игру
# будет собирать различные статусы, а под конец просто их активирует, то мы будем ооочень долго ждать их отработку.
# возможным решением была бы смена реализации например накопления статусов (собирать их в стеки по типам хотя бы).


# Льготное наследование (facility inheritance)

# Возможно подходящим примером будет класс-концовка игры. Мы создаем класс-событие, вызывающее концовку игры и можем
# наследоваться от неё, задавая новое описание. Таким образом, если потребуется создать тупиковую ветку приводящую к
# концу игры, мы просто отнаследуемся от корневого завершения и зададим описание. Возможно тут подойдут атрибуты класса,
# т.к. у нас не подразумевается несколько экземпляров разных концовок с разными описаниями.
class GameOver():
    same_text = ''

    def __init__(self):
        print(self.same_text)
        print('Game Over!')


class HappyEnding(GameOver):
    same_text = 'And they lived happily ever after'


class BadEnding(GameOver):
    same_text = 'And died on the same day. Today.'


"""
>>> first = HappyEnding()
And they lived happily ever after
Game Over!
>>> second = BadEnding()
And died on the same day. Today.
Game Over!
"""
