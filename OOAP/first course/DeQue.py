'''
abstract class ParentQueue<T>

    public const int REMOVE_TAIL_NONE = 0; // remove_tail() ещё не вызывалась
    public const int REMOVE_TAIL_OK = 1; // последняя remove_tail() отработала нормально
    public const int REMOVE_TAIL_ERR = 2; // в очереди отсутствуют значения

    public const int GET_TAIL_NONE = 0; // get_tail() ещё не вызывалась
    public const int GET_TAIL_OK = 1; // последняя get_tail() отработала нормально
    public const int GET_TAIL_ERR = 2; // в очереди отсутствуют значения


    // КОНСТРУКТОР
    // постусловие: создана новая пустая очередь
    public Queue<T> Queue();


    // КОМАНДЫ 
    // добавить значение в начало очереди
    // постусловие: значение помещено в начало очереди
    public void add_head(T value)

    // удалить крайнее в очереди значение
    // предусловие: очередь не пустая
    // постусловие: крайнее значение удалено
    public void remove_tail()

    // очистить очередь
    // постусловие: очередь очищена
    public void clear()

    //ЗАПРОСЫ

    // получить крайнее в очереди значение
    // предусловие: очередь не пустая
    // постусловие: получено крайнее значение в очереди
    public <T> get_tail()

    // получить количество элементов в очереди
    public int get_size()

    // дополнительные запросы:
    public int get_remove_tail_status()     // возвращает значение REMOVE_TAIL_*
    public int get_tail_status()   // возвращает значение GET_TAIL_*


class Queue(ParentQueue)<T>:
    pass


class Deque(ParentQueue)<T>:

    public const int REMOVE_HEAD_NONE = 0; // remove_head() ещё не вызывалась
    public const int REMOVE_HEAD_OK = 1; // последняя remove_head() отработала нормально
    public const int REMOVE_HEAD_ERR = 2; // в очереди отсутствуют значения

    public const int GET_HEAD_NONE = 0; // get_head() ещё не вызывалась
    public const int GET_HEAD_OK = 1; // последняя get_head() отработала нормально
    public const int GET_HEAD_ERR = 2; // в очереди отсутствуют значения

    // КОМАНДЫ
    // добавить значение в конец очереди
    // постусловие: в конец очереди добавлено значение
    public void add_tail(T value)

    // удалить первое значение в очереди
    // предусловие: очередь не пустая
    // постусловие: удалено первое в очереди значение
    public void remove_head(T value)
    

    // ЗАПРОСЫ
    // предусловие: получить первое в очереди значение
    // постусловие: в конец очереди добавлено значение
    public <T> get_head(T value)

    // дополнительные запросы
    public int get_head_status()       // возвращает GET_HEAD_*
    public int get_remove_head_status  // возвращает REMOVE_HEAD_*

'''

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class ParentQueue():

    REMOVE_TAIL_NONE = 0
    REMOVE_TAIL_OK = 1
    REMOVE_TAIL_ERR = 2

    GET_TAIL_NONE = 0
    GET_TAIL_OK = 1
    GET_TAIL_ERR = 2

    def __init__(self):
        self.clear()

    def clear(self):
        self._head = None
        self._tail = None
        self._size = 0

        self.status_remove_tail = self.REMOVE_TAIL_NONE
        self.status_get_tail = self.GET_TAIL_NONE

    def add_head(self, value):
        node = Node(value)
        if self.get_size() == 0:
            self._tail = node
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1

    def remove_tail(self):
        if self.get_size() == 1:
            self.clear()
            self.status_remove_tail = self.REMOVE_TAIL_OK
        elif self._tail:
            self._tail = self._tail.prev
            self.status_remove_tail = self.REMOVE_TAIL_OK
            self._size -= 1
        else:
            self.status_remove_tail = self.REMOVE_TAIL_ERR

    def get_tail(self):
        if self._tail:
            self.status_get_tail = self.GET_TAIL_OK
            return self._tail.value
        self.status_get_tail = self.GET_TAIL_ERR
        return 0

    def get_size(self):
        return self._size

    def get_remove_tail_status(self):
        return self.status_remove_tail

    def get_tail_status(self):
        return self.status_get_tail


class Queue(ParentQueue):
    pass

class Deque(ParentQueue):
    REMOVE_HEAD_NONE = 0
    REMOVE_HEAD_OK = 1
    REMOVE_HEAD_ERR = 2

    GET_HEAD_NONE = 0
    GET_HEAD_OK = 1
    GET_HEAD_ERR = 2

    def clear(self):
        super().clear()
        self.status_remove_head = self.REMOVE_HEAD_NONE
        self.status_get_head = self.GET_HEAD_NONE

    def add_tail(self, value):
        node = Node(value)
        if self.get_size() == 0:
            self._tail = node
            self._head = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._size += 1

    def remove_head(self):
        if self.get_size() == 1:
            self.clear()
            self.status_remove_head = self.REMOVE_HEAD_OK
        elif self._head:
            self._head = self._head.next
            self.status_remove_head = self.REMOVE_HEAD_OK
            self._size -= 1
        else:
            self.status_remove_head = self.REMOVE_HEAD_ERR

    def get_head(self):
        if self._head:
            self.status_get_head = self.GET_HEAD_OK
            return self._head.value
        self.status_get_head = self.GET_HEAD_ERR
        return 0

    def get_head_status(self):
        return self.status_get_head

    def get_remove_head_status(self):
        return self.status_remove_head
