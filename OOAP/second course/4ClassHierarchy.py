"""
Задание 9.
Постройте в вашем языке программирования базовую иерархию из двух классов General и Any.
Унаследуйте General от универсального базового класса, если таковой имеется в языке или стандартной библиотеке/фреймворке,
и реализуйте семь фундаментальных операций для него, используя для этого по возможности возможности стандартных библиотек.
"""
from copy import copy, deepcopy
from json import JSONDecodeError
import json


class General(object):

    # С более сложными вещами такой способ не покатит, там могут помешать всякие дескрипторы.
    @classmethod
    def deserialize(cls, attrs: str):
        """ Создание объекта из сериализованного вида

        >>> first = General()
        >>> s = General.serialize(first)
        >>> b = General.deserialize(s)
        >>> isinstance(b, General)
        True

        >>> General.deserialize("str")
        Wrong data type str

        >>> General.deserialize(str({"value":"0"}).replace("'", '"'))
        Its not a serialized General

        :param attrs: словарь атрибутов в виде строки
        :type atrs: str
        """
        try:
            attrs = json.loads(attrs)
            attrs.pop(cls.__name__)
            new_one = cls()
            for attr, val in attrs.items():
                setattr(new_one, attr, val)
            return new_one
        except JSONDecodeError:
            print(f'Wrong data type {attrs}')
        except KeyError:
            print(f'Its not a serialized {cls.__name__}')

    @classmethod
    def serialize(cls, object):
        """ Сериализация объекта.

        >>> first = General()
        >>> General.serialize(first)
        '{"value": 0, "General": 1}'

        :param object: Объект для сериализации
        :type object: General
        :return: сериализованный объект
        :rtype: str
        """
        s_attrs = object.__dict__
        s_attrs[cls.__name__] = 1
        return str(s_attrs).replace('\'', '"')

    def __init__(self):
        self.value = 0

    def __str__(self):
        """ Отображение объекта при команде print(). """
        return f'{self.__dict__}'

    def __eq__(self, other) -> bool:
        """ Сравнение объекта с другим объектом `==`.
        
        >>> first = General()
        >>> first == first
        True
        
        :param other: другой объект
        :type other: General
        :return: объекты идентичны
        :rtype: bool
        """
        return self is other

    def __ne__(self, other) -> bool:
        """ Сравнение объекта с другим объектом `!=`.

        >>> first = General()
        >>> two = General()
        >>> first != two
        True

        :param other: другой объект
        :type other: General
        :return: объекты не идентичны
        :rtype: bool
        """
        return self is not other

    # Для следующих операций сравнения необходимо какое-то значение либо пилить какую-то сложную логику.
    # Упростим, представив, что у нашего класса есть поддающийся сравнению атрибут .value.

    def __lt__(self, other) -> bool:
        """ Сравнение объекта с другим объектом `<`.
        
        >>> first = General()
        >>> two = General()
        >>> two.value = 2
        >>> first < two
        True
        
        :param other: другой объект
        :type other: General
        :return: текущий объект меньше переданного
        :rtype: bool
        """
        return self.value < other.value

    def __gt__(self, other) -> bool:
        """ Сравнение объекта с другим объектом `>`.

        >>> first = General()
        >>> first.value = 2
        >>> two = General()
        >>> first > two
        True

        :param other: другой объект
        :type other: General
        :return: текущий объект меньше переданного
        :rtype: bool
        """
        return self.value > other.value

    def __le__(self, other) -> bool:
        """ Сравнение объекта с другим объектом `<=`.
        
        >>> first = General()
        >>> two = General()
        >>> first <= two
        True
        
        :param other: другой объект
        :type other: General
        :return: текущий объект меньше переданного
        :rtype: bool
        """
        return self.value <= other.value

    def __ge__(self, other) -> bool:
        """ Сравнение объекта с другим объектом `>=`.
        
        >>> first = General()
        >>> two = General()
        >>> first >= two
        True
        
        :param other: другой объект
        :type other: General
        :return: текущий объект меньше переданного
        :rtype: bool
        """
        return self.value >= other.value

    def __copy__(self):
        """ Поведение при копировании (метод copy), создает shallow копию объекта.

        При shallow копировании в атрибуты помещаются ссылки на те же объекты, что в атрибутах у оригинала

        >>> first = General()
        >>> first.a = [1]
        >>> two = copy(first)
        >>> two.a.append(2)
        >>> print(first.a)
        [1, 2]
        
        :return: копия объекта
        :rtype: General
        """
        copy = General()
        for name, val in self.__dict__.items():
            setattr(copy, name, val)
        return copy

    def __deepcopy__(self, memo: dict = None):
        """ Поведение при глубоком копировании (метод deepcopy), создает глубокую копию объекта.

        В отличии от shallow копии в атрибуты помещаются ссылки на копии объектов, находящихся в атрибутах у оригинала
       
        >>> first = General()
        >>> first.a = [1]
        >>> two = deepcopy(first)
        >>> two.a.append(2)
        >>> print(first.a)
        [1]

        :return: полная копия объекта
        :rtype: General
        """
        if memo is None:
            memo = {}

        dpc = type(self)()
        memo[id(self)] = dpc
        for name, val in self.__dict__.items():
            setattr(dpc, name, deepcopy(val, memo=memo))
        return dpc

    def copy(self, some_object):
        """ Насколько я понял из формулировки, в методах copy() и deepcopy(), 
        раз копирование происходит в уже существующий объект, значит он передается во входных данных.
        
        >>> first = General()
        >>> first.a = [1]
        >>> two = General()
        >>> first.copy(two)
        >>> two.a.append(2)
        >>> print(two.a)
        [1, 2]
        >>> print(first.a)
        [1, 2]

        :param some_object: другой объект
        :type some_object: General
        """
        for name, val in self.__dict__.items():
            setattr(some_object, name, val)

    def deepcopy(self, some_object):
        """Насколько я понял из формулировки, в методах copy() и deepcopy(),
        раз копирование происходит в уже существующий объект, значит он передается во входных данных.
        
        >>> first = General()
        >>> first.a = [1]
        >>> two = General()
        >>> first.deepcopy(two)
        >>> two.a.append(2)
        >>> print(two.a)
        [1, 2]
        >>> print(first.a)
        [1]

        :param some_object: другой объект
        :type some_object: General
        """
        for name, val in self.__dict__.items():
            setattr(some_object, name, deepcopy(val))
        
    def clone(self):
        """ Клонирование объекта, возвращает только что созданный новый объект с глубокой копией артибутов. 
        
        >>> first = General()
        >>> first.a = [1, 2]
        >>> two = first.clone()
        >>> two.a.append(3)
        >>> print(first.a)
        [1, 2]
        >>> print(two.a)
        [1, 2, 3]
        
        :return: новый объект
        :rtype: General
        """
        return deepcopy(self)

    def get_class(self):
        """  Получение реального типа объекта.

        >>> first = General()
        >>> type(first) == first.get_class()
        True
        
        :return: [description]
        :rtype: [type]
        """
        return self.__class__


# В Python класс уже является типом, для проверки его объектов. Поэтому можно ничего не переписывать
# если мы рассчитываем стандартные проверки isinstance(). Если хотим мимикрировать под другой класс, то
# есть методы __instancecheck__ и __subclasscheck__, которые можно переопределить в метаклассе.
# Проверку type() без сверхусилий переопределить нельзя, насколько я знаю.


"""
Задание 10.
Выясните, имеется ли в вашем языке программирования возможность запрета
переопределения методов в потомках, и приведите пример кода.
"""

# Насколько я знаю, в стандартных средствах простого способа запретить переопределение нет.
# Но метаклассы тут приходят на помощь) можно вот такой вариант попробовать.


class SealedMethod(Exception):
    pass


class MetaMethod(type):

    def __new__(mcls, name, bases, attrs):
        sealed_methods = set()
        for b in bases:
            sealed_methods = sealed_methods.union(b.sealed_methods)
        for attr in attrs:
            if attr in sealed_methods:
                raise SealedMethod(f'You cannot rewrite sealed method {attr}')
        
        return super().__new__(mcls, name, bases, attrs)


class Anc():
    sealed_methods = {
        'test_method'
    }

    def test_method(self):
        print('I working!')


class Child(Anc, metaclass=MetaMethod):
    def test_method(self):
        print('I know better!')
