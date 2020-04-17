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


# В классе Any у нас не было реализовано метода сложения, чтобы не дублировать код из предыдущего упражнения
# создам здесь потомка с новым методом.
class Any2(Any):
    def __add__(self, other):
        """ Сложение.
     
        >>> a = Any2()
        >>> a.value = 3
        >>> b = Any2()
        >>> b.value = 5
        >>> (a + b).value
        8
        
        """
        if isinstance(other, Any2):
            sum = self.value + other.value
            result = Any2()
            result.value = sum
            return result
        else:
            return Void


class Vector():

    def __init__(self, storage= None):
        """ Конструктор класса.
        
        :param storage: Список элементов для хранилища, defaults to None
        :type storage: List[Any], optional
        """
        self.storage = storage or []
    
    def size(self):
        return len(self.storage)

    def __add__(self, other):
        """ Сложение 2 объектов.
        
        Для наглядности большая часть примеров со стандартными типами.
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

        А вот пример с нашим кастомным Any, наследником General
        Получаем 2 значения Any2 типа, с атрибутами value = 6, 10
        >>> a = Any2()
        >>> a.value = 3
        >>> b = Any2()
        >>> b.value = 5
        >>> c = Vector([a, b])
        >>> d = c
        >>> k = c + d
        >>> k.storage[0].value
        6
        >>> k.storage[1].value
        10

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
