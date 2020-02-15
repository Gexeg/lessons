'''
abstract class Queue<T>

    public const int DEQUEUE_NONE = 0; // dequeue() ещё не вызывалась
    public const int DEQUEUE_OK = 1; // последняя dequeue() отработала нормально
    public const int DEQUEUE_ERR = 2; // в очереди отсутствуют значения

    public const int GET_VALUE_NONE = 0; // get_value() ещё не вызывалась
    public const int GET_VALUE_OK = 1; // последняя get_value() отработала нормально
    public const int GET_VALUE_ERR = 2; // в очереди отсутствуют значения


    // КОНСТРУКТОР
    // постусловие: создана новая пустая очередь
    public Queue<T> Queue();


    // КОМАНДЫ 
    // добавить значение в очередь
    // постусловие: значение помещено в очередь
    public enqueue(T value)

    // удалить крайнее в очереди значение
    // предусловие: очередь не пустая
    // постусловие: крайнее значение удалено
    public dequeue()

    // очистить очередь
    // постусловие: очередь очищена
    public clear()

    //ЗАПРОСЫ

    // получить крайнее в очереди значение
    // предусловие: очередь не пустая
    // постусловие: получено крайнее значение в очереди
    public get_value()

    // получить количество элементов в очереди
    public get_size()

    // дополнительные запросы:
    public get_dequeue_status()     // возвращает значение DEQUEUE_*
    public get_value_status()   // возвращает значение GET_VALUE_*
'''

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Queue():

    DEQUEUE_NONE = 0
    DEQUEUE_OK = 1
    DEQUEUE_ERR = 2

    GET_VALUE_NONE = 0
    GET_VALUE_OK = 1
    GET_VALUE_ERR = 2

    def __init__(self):
        self.clear()

    def clear(self):
        self._head = None
        self._tail = None
        self._size = 0

        self.status_dequeue = 0
        self.status_get_value = 0

    def enqueue(self, value):
        node = Node(value)
        if self.get_size() == 0:
            self._tail = node
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1

    def dequeue(self):
        if self.get_size() == 1:
            self.clear()
            self.status_dequeue = self.DEQUEUE_OK
        elif self._tail:
            self._tail = self._tail.prev
            self.status_dequeue = self.DEQUEUE_OK
            self._size -= 1
        else:
            self.status_dequeue = self.DEQUEUE_ERR

    def get_value(self):
        if self._tail:
            self.status_get_value = self.GET_VALUE_OK
            return self._tail.value
        self.status_get_value = self.GET_VALUE_ERR
        return 0

    def get_size(self):
        return self._size

    def get_dequeue_status(self):
        return self.status_dequeue

    def get_value_status(self):
        return self.status_get_value
