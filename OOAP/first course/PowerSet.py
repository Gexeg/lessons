'''
abstract class HashTable<T>

    public const int PUT_NONE = 0; // put() ещё не вызывалась
    public const int PUT_OK = 1; // последняя put() отработала нормально
    public const int PUT_ERR = 2; // таблица заполнена

    public const int REMOVE_NONE = 0; // remove() ещё не вызывалась
    public const int REMOVE_OK = 1; // последняя remove() отработала нормально
    public const int REMOVE_ERR = 2; // в таблице отсутствуют значения

    // КОНСТРУКТОР
    // постусловие: создана новая пустая хэш-таблица с максимальной вместимостью = capacity
    public HashTable<T> HashTable(int capacity);

    // КОМАНДА
    // поместить значение в таблицу
    // предусловие: в таблице присутствуют пустые слоты
    // постусловие: значение помещено в таблицу
    public void put(T value)

    // удалить значение из таблицы
    // предусловие: значение присутствует в таблице
    // постусловие: значение удалено из таблицы
    public void remove(T value)

    // очистить таблицу
    // постусловие: таблица очищена
    public void clear()

    // ЗАПРОС
    // значение присутствует в таблице?
    public bool in_table(T value)

    // размер таблицы
    public int size()

    // максимальное количество элементов в таблице
    public int capacity()

    // дополнительные статусы
    public int put_status() // возвращаяет PUT_*
    public int remove_status() // возвращает REMOVE_* 


class PowerSet(HashTable) <T>

    // КОМАНДА
    // поместить значение в таблицу
    // предусловие: подобного значения нет в таблице
    // предусловие: в таблице присутствуют пустые слоты
    // постусловие: значение помещено в таблицу
    public void put(T value)

'''

from HashTable import HashTable

class PowerSet(HashTable):

    def put(self, value):
        if not self.in_table(value):
            super().put(value)
        else:
            self.status_put = self.PUT_ERR
