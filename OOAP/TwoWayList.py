'''
class ParentList<T>

    public const int RIGHT_NONE = 0; // right() ещё не вызывалась
    public const int RIGHT_OK = 1; // последняя right() отработала нормально
    public const int RIGHT_ERR = 2; // достинут конец списка либо в списке отсутствуют узлы

    public const int GET_NONE = 0; // get() ещё не вызывалась
    public const int GET_OK = 1; // последняя get() отработала нормально
    public const int GET_ERR = 2; // в списке отсутствуют узлы

    public const int PUT_NONE = 0; // put() ещё не вызывалась
    public const int PUT_OK = 1; // последняя put() отработала нормально
    public const int PUT_ERR = 2; // в списке отсутствуют узлы

    public const int REMOVE_NONE = 0; // remove() ещё не вызывалась
    public const int REMOVE_OK = 1; // последняя remove() отработала нормально
    public const int REMOVE_ERR = 2; // в списке отсутствуют узлы

    public const int REPLACE_NONE = 0; // replace() ещё не вызывалась
    public const int REPLACE_OK = 1; // последняя replace() отработала нормально
    public const int REPLACE_ERR = 2; // в списке отсутствуют узлы

    public const int FIND_NONE = 0; // find() ещё не вызывалась
    public const int FIND_OK = 1; // последняя find() отработала нормально
    public const int FIND_ERR = 2; // достинут конец списка либо в списке отсутствуют узлы

    // КОНСТРУКТОР
    // постусловие: создан новый пустой связный список. 
    public LinkedList<T> LinkedList(); 
    // конец конструктора


    // КОМАНДЫ
    // установить курсор на начало списка
    // предусловие: список не пустой
    // постусловие: изменено положение курсора
    public void head()

    // установить курсор в конец списка
    // предусловие: список не пустой
    // постусловие: изменено положение курсора
    public void tail()

    // сдвинуть курсор вправо
    // предусловие: курсор установлен на какой-либо узел
    // предусловие: курсор расопложен не в хвосте
    // постусловие: изменено положение курсора
    public void right()

    // вставить следом за текущим узлом узел со значением
    // предусловие: курсор установлен на какой-либо узел
    // постусловие: в список добавлен узел. Если курсор был расположен в хвосте, то узел становится новым хвостом
    public void put_right(T value)

    // вставить перед текущим узлом узел со значением
    // предусловие: курсор установлен на какой-либо узел
    // постусловие: в список добавлен узел. Если курсор был расположен в голове, то узел становится новой головой
    public void put_left(T value)

    // удалить текущий узел.
    // предусловие: курсор установлен на какой-либо узел
    // постусловие: узел удален из списка
    // постусловие: если есть сосед справа, курсор смещается к нему, иначе курсор смещается к левому соседу, если он есть.
    // если это был последний узел, курсор больше не показывает на какой-либо узел
    public void remove()

    // очистить список
    // постусловие: из списка удаляются все значения, все статусы устанавливаются на *_NONE
    public void clear()

    // добавить новый узел в хвост списка
    // постусловие: в хвост списка добавлен узел
    public void add_tail(T value)

    // заменить значение текущего узла
    // предусловие: курсор установлен на какой-либо узел
    // постусловие: значение этого узла заменено на входящее
    public void replace (T value)

    // установить курсор на следующий (по отношению к текушему) узел с заданным значением
    // предусловие: курсор установлен на какой-либо узел
    // предусловие: после этого узла есть следующий узел с заданным значением
    // постусловие: курсор перемещен на следующий узел с заданным значением
    public void find(T value)

    // удалить в списке все узлы с заданным значением 
    // постусловие: в списке удалены все узлы с заданным значением
    public void remove_all(T value)


    // ЗАПРОСЫ
    // курсор находится в начале списка?
    public void is_head()

    // курсор находится в конце списка?
    public void is_tail()

    // установлен ли курсор на какой-либо узел в списке (равносильно "есть ли список?")
    public void is_value()

    // посчитать количество узлов в списке
    public size()

    // получить значение текущего узла
    // предусловие: курсор установлен на какой-либо узел
    public void get()

    // дополнительные запросы:
    public int get_right_status(); // возвращает значение RIGHT_*
    public int get_put_status(); // возвращает значение PUT_*
    public int get_get_status(); // возвращает значение GET_*
    public int get_remove_status(); // возвращает значение REMOVE_*
    public int get_replace_status(); // возвращает значение REPLACE_*
    public int get_find_status(); // возвращает значение FIND_*

class LinkedList(ParentList)<T>:
    pass

class TwoWayList(ParentList)<T>:
    public const int LEFT_NONE = 0; // left() ещё не вызывалась
    public const int LEFT_OK = 1; // последняя left() отработала нормально
    public const int LEFT_ERR = 2; // курсор расположен в начале списка либо в списке отсутствуют узлы

    // КОМАНДЫ
    // сдвинуть курсор влево
    // предусловие: курсор установлен на какой-либо узел
    // предусловие: курсор расопложен не в голове
    // постусловие: изменено положение курсора
    public void left()

    // ЗАПРОСЫ
    public int get_left_status(); // возвращает значение LEFT_*



'''

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class ParentList():
    RIGHT_NONE = 0   # right() ещё не вызывалась
    RIGHT_OK = 1     # последняя right() отработала нормально
    RIGHT_ERR = 2    # достинут конец списка либо в списке отсутствуют узлы

    GET_NONE = 0     # get() ещё не вызывалась
    GET_OK = 1       # последняя get() отработала нормально
    GET_ERR = 2      # в списке отсутствуют узлы

    PUT_NONE = 0     # put() ещё не вызывалась
    PUT_OK = 1       # последняя put() отработала нормально
    PUT_ERR = 2      # в списке отсутствуют узлы

    REMOVE_NONE = 0  # remove() ещё не вызывалась
    REMOVE_OK = 1    # последняя remove() отработала нормально
    REMOVE_ERR = 2   # в списке отсутствуют узлы

    REPLACE_NONE = 0 # replace() ещё не вызывалась
    REPLACE_OK = 1   # последняя replace() отработала нормально
    REPLACE_ERR = 2  # в списке отсутствуют узлы

    FIND_NONE = 0    # find() ещё не вызывалась
    FIND_OK = 1      # последняя find() отработала нормально
    FIND_ERR = 2     # достинут конец списка либо в списке отсутствуют узлы

    def __init__(self):
        self.clear()

    def clear(self):
        self._head = None
        self._tail = None
        self._cursor = None

        self.status_right = self.RIGHT_NONE
        self.status_get = self.GET_NONE
        self.status_put = self.PUT_NONE
        self.status_remove = self.REMOVE_NONE
        self.status_replace = self.REPLACE_NONE
        self.status_find = self.FIND_NONE

    def head(self):
        if self._head:
            self._cursor = self._head

    def tail(self):
        if self._tail:
            self._cursor = self._tail

    def right(self):
        if self._cursor and self._cursor != self._tail:
            self._cursor = self._cursor.next
            self.status_right = self.RIGHT_OK
        else:
            self.status_right = self.RIGHT_ERR

    def put_right(self, value):
        if self._cursor:
            node = Node(value)
            node.prev = self._cursor
            if self._cursor.next:
                self._cursor.next.prev = node
                node.next = self._cursor.next
            self._cursor.next = node
            if self.is_tail():
                self._tail = node
            self.status_put = self.PUT_OK
        else:
            self.status_put = self.PUT_ERR
    
    def put_left(self, value):
        if self._cursor:
            node = Node(value)
            node.next = self._cursor
            if self._cursor.prev:
                self._cursor.prev.next = node
                node.prev = self._cursor.prev
            self._cursor.prev = node
            if self.is_head():
                self._head = node
            self.status_put = self.PUT_OK
        else:
            self.status_put = self.PUT_ERR
    
    def remove(self):
        if self._cursor:
            if self.size() == 1:
                self.clear()
                return
            cursor = self._cursor 
            if self.is_head():
                cursor.next.prev = None
                self._cursor = cursor.next
                self._head = self._cursor
            elif self.is_tail():
                cursor.prev.next = None
                self._cursor = cursor.prev
                self._tail = self._cursor
            elif cursor.prev and cursor.next:
                cursor.prev.next = cursor.next
                cursor.next.prev = cursor.prev
                self._cursor = cursor.next
            self.status_remove = self.REMOVE_OK
        else:
            self.status_remove = self.REMOVE_ERR

    def add_tail(self, value):
        node = Node(value)
        if self._head is None:
            self._head = node
        if self._tail:
            self._tail.next = node
            node.prev = self._tail
        self._tail = node
        if not self.is_value():
            self._cursor = self._tail
    
    def replace(self, value):
        if self._cursor:
            self._cursor.value = value
            self.status_replace = self.REPLACE_OK
        else:
            self.status_replace = self.REPLACE_ERR

    def find(self, value):
        if self._cursor:
            current_node = self._cursor
            while current_node.next:
                current_node = current_node.next
                if current_node.value == value:
                    self._cursor = current_node
                    self.status_find = self.FIND_OK
                    return
        self.status_find = self.FIND_ERR

    def remove_all(self, value):
        if self._cursor:
            self._cursor = self._head
            while True:
                if self.get() == value:
                    self.remove()
                    continue
                self.find(value)
                if self.get_find_status() == self.FIND_OK:
                    self.remove()
                else:
                    break

    def is_head(self):
        if self._cursor:
            return self._cursor == self._head
        return False

    def is_tail(self):
        if self._cursor:
            return self._cursor == self._tail
        return False

    def is_value(self):
        return self._cursor is not None

    def size(self):
        size = 0
        if self._head:
            current_pos = self._head
            size += 1
            while current_pos.next:
                current_pos = current_pos.next
                size += 1
        return size

    def get(self):
        if self._cursor:
            self.status_get = self.GET_OK
            return self._cursor.value
        self.status_get = self.GET_ERR
        return 0

    def get_right_status(self):
        return self.status_right

    def get_put_status(self):
        return self.status_put

    def get_get_status(self):
        return self.status_get

    def get_remove_status(self):
        return self.status_remove
    
    def get_replace_status(self):
        return self.status_replace

    def get_find_status(self):
        return self.status_find 


class LinkedList(ParentList):
    pass

class TwoWayList(ParentList):
    
    LEFT_NONE = 0
    LEFT_OK = 1
    LEFT_ERR = 2

    def clear(self):
        super().clear()
        self.status_left = self.LEFT_NONE

    def left(self):
        if self._cursor and self._cursor != self._head:
            self._cursor = self._cursor.prev
            self.status_left = self.LEFT_OK
        else:
            self.status_left = self.LEFT_ERR
    
    def get_left_status(self):
        return self.status_left
