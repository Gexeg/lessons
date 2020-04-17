"""
Сформируйте тип (класс) Vector<Any> (линейный массив значений типа Any, наследуемого от General),
над которым допустима операция сложения, реализуемая как сложение соответствующих значений типа Any
двух векторов одинаковой длины. Если длины векторов различны, возвращайте Void/null в качестве результата работы
операции сложения. Выясните, как в используемом вами языке программирования элегантнее всего реализовать
поддержку сложения элементов произвольных типов.
Проверьте, насколько корректно будет работать сложение объектов типа Vector<Vector<Vector<Any>>>.
"""

from ClassHierarchy4 import General, Any
from HierarchyClojure5 import Void
from typing import TypeVar, Generic, List


class Vector(General):

    def __init__(self, storage: List[Any] = None):
        """ Конструктор класса.

        Чтобы реализовать сложение, нам нужно как-то и где-то хранить данные, поэтому тип value
        переопределяем на список. Так же нужно будет переопределить методы сравнения.
        
        :param storage: Список элементов для хранилища, defaults to None
        :type storage: List[Any], optional
        """
        self.storage: List[Any] = storage or []

    def __lt__(self, other) -> bool:
        """ Сравнение объекта с другим объектом `<`.
        
        >>> first = Vector([1,2])
        >>> two = Vector([2])
        >>> first < two
        True
        
        :param other: другой объект
        :type other: Vector
        :return: текущий объект меньше переданного
        :rtype: bool
        """
        return self.storage < other.storage

    def __gt__(self, other) -> bool:
        """ Сравнение объекта с другим объектом `>`.

        >>> first = Vector([1,2])
        >>> two = Vector([2])
        >>> first > two
        False

        :param other: другой объект
        :type other: Vector
        :return: текущий объект меньше переданного
        :rtype: bool
        """
        return self.storage > other.storage

    def __le__(self, other) -> bool:
        """ Сравнение объекта с другим объектом `<=`.
        
        >>> first = Vector([2])
        >>> two = Vector([2])
        >>> first <= two
        True
        
        :param other: другой объект
        :type other: Vector
        :return: текущий объект меньше переданного
        :rtype: bool
        """
        return self.storage <= other.storage

    def __ge__(self, other) -> bool:
        """ Сравнение объекта с другим объектом `>=`.
        
        >>> first = Vector([2])
        >>> two = Vector([2])
        >>> first >= two
        True
        
        :param other: другой объект
        :type other: General
        :return: текущий объект меньше переданного
        :rtype: bool
        """
        return self.storage >= other.storage
    
    def size(self):
        return len(self.storage)

    def __add__(self, other):
        """ Сложение 2 объектов.
        
        >>> a = Vector([1, 2])
        >>> b = Vector([3, 4])
        >>> c = a + b
        >>> c.storage
        [4, 6]

        >>> a = Vector([1, 'str', None])
        >>> b = Vector([2, 'Type', 3])
        >>> (a + b).storage
        [3, 'strType', <class 'HierarchyClojure5.Void'>]

        >>> a = Vector([1, 'str', None])
        >>> b = Vector([2])
        >>> a + b
        <class 'HierarchyClojure5.Void'>

        >>> a = Vector([1, 'str'])
        >>> b = Vector([Vector([Vector([a])])])
        >>> c = b
        >>> sum = c + b
        >>> sum.storage[0].storage[0].storage[0].storage
        [2, 'strstr']

        :param other: другой объект
        :type other: Vector
        :return: объект класса Vector или тип Void
        :rtype: Vector or Void
        """
        if isinstance(other, Vector) and self.size() == other.size():
            storage = []
            for a, b in zip(self.storage, other.storage):
                try:
                    storage.append(a + b)
                except TypeError:
                    storage.append(Void)
            return Vector(storage)
        else:
            return Void


if __name__ == "__main__":
    import doctest
    doctest.testmod()
