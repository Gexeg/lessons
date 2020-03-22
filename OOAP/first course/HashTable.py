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
'''

class HashTable():

    PUT_NONE = 0
    PUT_OK = 1
    PUT_ERR = 2
    
    REMOVE_NONE = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.clear()
    
    def clear(self):
        self.storage = [None] * self.capacity
        self.size = 0

        self.status_put = self.PUT_NONE
        self.status_remove = self.REMOVE_NONE

    def put(self, value):
        if self.size < self.capacity:
            for slot in self.__next_slot(value):
                if self.storage[slot] is None:
                    self.status_put = self.PUT_OK
                    self.size += 1
                    self.storage[slot] = value
                    return
            self.status_put = self.PUT_ERR
            raise Exception('Cannot found empty slot')
        else:
            self.status_put = self.PUT_ERR

    def __hash_fun(self, value, incr=0):
        return (id(value)+incr) % self.capacity

    def __next_slot(self, value):
        return (self.__hash_fun(value, ind) for ind in range(self.capacity))

    def remove(self, value):
        if self.size > 0:
            for slot in self.__next_slot(value):
                if self.storage[slot] is None:
                    break
                if self.storage[slot] == value:
                    self.status_remove = self.REMOVE_OK
                    self.storage[slot] = None
                    return
            self.status_put = self.REMOVE_ERR
        else:
            self.status_remove = self.REMOVE_ERR

    def in_table(self, value):
        if self.size > 0:
            for slot in self.__next_slot(value):
                if  self.storage[slot] == value or self.storage[slot] is None:
                    break
            return self.storage[slot] == value
        else:
            return False

    def get_max_size(self):
        return self.capacity

    def get_size(self):
        return self.size

    def get_remove_status(self):
        return self.status_remove

    def get_put_status(self):
        return self.status_put
