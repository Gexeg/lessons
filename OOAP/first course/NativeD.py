'''
abstract class NativeDictionary<T>

    public const int GET_NONE = 0; // get() ещё не вызывалась
    public const int GET_OK = 1;   // последняя get() отработала нормально
    public const int GET_ERR = 2;  // передан некорректный ключ

    public const int REMOVE_NONE = 0; // remove() ещё не вызывалась
    public const int REMOVE_OK = 1;   // последняя remove() отработала нормально
    public const int REMOVE_ERR = 2;  // ключ отсутствует в словаре

    // КОНСТРУКТОР
    // постусловие: создан новый пустой словарь
    public HashTable<T> NativeDictionary();

    // КОМАНДА
    // поместить значение в словарь под переданным ключом
    // постусловие: значение помещено в словарь под переданным ключом
    public void put(T value, str key)

    // удалить значение из словаря по переданныму ключу
    // предусловие: значение присутствует в словаре
    // постусловие: значение удалено из словаря
    public void remove(str key)

    // очистить словарь
    // постусловие: словарь очищен
    public void clear()

    // ЗАПРОС
    // ключ присутствует в словаре?
    public bool in_dict(str key)

    // получить значение по ключу
    // предусловие: ключ присутствует в словаре
    public T get_value(str key)

    // дополнительные статусы
    public int get_get_value_status() // возвращаяет GET_*
    public int get_remove_status() // возвращает REMOVE_* 
'''

class NativeDictionary():

    PUT_NONE = 0
    PUT_OK = 1
    PUT_ERR = 2

    GET_NONE = 0
    GET_OK = 1
    GET_ERR = 2
    
    REMOVE_NONE = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    def __init__(self):
        self.clear()

    def clear(self):
        self.storage = {}

        self.status_put = self.PUT_NONE
        self.status_get_value = self.GET_NONE
        self.status_remove = self.REMOVE_NONE

    def put(self, value, key):
        self.storage[key] = value

    def remove(self, key):
        if key in self.storage:
            self.storage.pop(key)
            self.status_remove = self.REMOVE_OK
        else:
            self.status_remove = self.REMOVE_ERR

    def in_dict(self, key):
        return key in self.storage

    def get_value(self, key):
        if key in self.storage:
            self.status_get_value = self.GET_OK
            return self.storage[key]
        else:
            self.status_get_value = self.GET_ERR
            return 0

    def get_get_value_status(self):
        return self.status_get_value

    def get_remove_status(self):
        return self.status_remove
