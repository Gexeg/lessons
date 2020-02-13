'''
class DynArray<T>

    public const int INSERT_NONE = 0; // insert() ещё не вызывалась
    public const int INSERT_OK = 1; // последняя insert() отработала нормально
    public const int INSERT_ERR = 2; // индекс отсутствует в массиве

    public const int REMOVE_NONE = 0; // remove() ещё не вызывалась
    public const int REMOVE_OK = 1; // последняя remove() отработала нормально
    public const int REMOVE_ERR = 2; // индекс отсутствует в массиве

    public const int GET_VALUE_NONE = 0; // get_value() ещё не вызывалась
    public const int GET_VALUE_OK = 1; // последняя get_value() отработала нормально
    public const int GET_VALUE_ERR = 2; // индекс отсутствует в массиве

    // КОНСТРУКТОР
    // постусловие: создан новый пустой массив 
    public DynArray<T> DynArray();
    // конец конструктора


    // КОМАНДЫ
    // поместить значение в слот под указанным индексом
    // предусловие: указанный индекс присутствует в массиве
    // постусловие: в слот под указанным индексом помещено значение
    // постусловие: все остальные значения после помещенного сдвинуты на 1 индекс вперед
    public void insert(T value, int index)

    // удалить значение из слота под указанным индексом
    // предусловие: указанный индекс присутствует в массиве
    // постусловие: удалить значение из массива
    // постусловие: все остальные значения после удаленного сдвинуты на 1 индекс назад
    public void remove(int index)

    // поместить значение в конец массива
    // постусловие: в последний незанятый слот массива помещено значение
    public void append(T value)

    // очистить список
    // постусловие: из списка удалены все элементы
    // постусловие: статусы установлены на 0
    public void clear()


    // ЗАПРОСЫ
    // получить значение из слота
    // предусловие: указанный индекс присутствует в массиве
    public void get_value(int index)

    // получить текущий размер списка
    public void get_size()

    // дополнительные запросы:
    public int get_insert_status(); // возвращает значение INSERT_*
    public int get_remove_status(); // возвращает значение REMOVE_*
    public int get_get_value_status(); // возвращает значение GET_VALUE_*
'''

class DynArray():

    INSERT_NONE = 0
    INSERT_OK = 1
    INSERT_ERR = 2

    REMOVE_NONE = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    GET_VALUE_NONE = 0
    GET_VALUE_OK = 1
    GET_VALUE_ERR = 2

    def __init__(self):
        self.clear()

    def clear(self):
        self.storage = []

        self.status_insert = 0
        self.status_remove = 0
        self.status_get_value = 0

    def append(self, value):
        self.storage.append(value)

    def insert(self, value, index):
        if self.storage and index < len(self.storage):
            self.storage.insert(index, value)
            self.status_insert = self.INSERT_OK
            return
        self.status_insert = self.INSERT_ERR

    def remove(self, index):
        if self.storage and index < len(self.storage):
            self.storage.pop(index)
            self.status_remove = self.REMOVE_OK
            return
        self.status_remove = self.REMOVE_ERR

    def get_value(self, index):
        if self.storage and index < len(self.storage):
            self.status_get_value = self.GET_VALUE_OK
            return self.storage[index]
        self.status_get_value = self.GET_VALUE_ERR
        return 0

    def get_size(self):
        return len(self.storage)

    def get_insert_status(self):
        return self.status_insert

    def get_remove_status(self):
        return self.status_remove

    def get_get_value_status(self):
        return self.status_get_value