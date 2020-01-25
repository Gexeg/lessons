'''
abstract class BoundedStack<T>

    public const int PUSH_NIL = 0; // push() ещё не вызывалась
    public const int PUSH_OK = 1; // последняя push() отработала нормально
    public const int PUSH_ERR = 2; // в стеке отсутствуют свободные слоты

    public const int POP_NIL = 0; // pop() ещё не вызывалась
    public const int POP_OK = 1; // последняя pop() отработала нормально
    public const int POP_ERR = 2; // стек пуст

    public const int PEEK_NIL = 0; // peek() ещё не вызывалась
    public const int PEEK_OK = 1; // последняя peek() вернула корректное значение 
    public const int PEEK_ERR = 2; // стек пуст

    // конструктор
    public Stack<T> Stack(int capacity = 32); 
    // постусловие: создан новый пустой стек с максимальной вместимостью = capacity
    // capacity - опциональный параметр, если он не передан, используется значение по умолчанию = 32

    // команды:
    // предусловие: в стеке есть свободный слот
    // постусловие: в стек добавлено новое значение
    public void push(T value); 

    // предусловие: стек не пустой
    // постусловие: из стека удалён верхний элемент
    public void pop(); 

    // постусловие: из стека удалятся все значения
    // статусы обновлены и установлены на *_NIL
    public void clear();

    // запросы:
    // предусловие: стек не пустой
    public T peek(); 

    public int size();

    public int capacity();

    // дополнительные запросы:
    public int get_push_status(); // возвращает значение PUSH_*
    public int get_pop_status(); // возвращает значение POP_*
    public int get_peek_status(); // возвращает значение PEEK_*
'''
from typing import Any

class BoundedStack():
    PUSH_NIL = 0
    PUSH_OK = 1
    PUSH_ERR = 2

    POP_NIL = 0
    POP_OK = 1
    POP_ERR = 2
    
    PEEK_NIL = 0
    PEEK_OK = 1 
    PEEK_ERR = 2

    def __init__(self, capacity: int = 32):
        self.__stack = []
        self.__push_status = self.PUSH_NIL
        self.__pop_status = self.POP_NIL
        self.__peek_status = self.PEEK_NIL
        self.__capacity = capacity

    def push(self, value: Any):
        if self.size() == self.capacity():
            self.__push_status = self.PUSH_ERR
            return
        self.__stack.append(value)
        self.__push_status = self.PUSH_OK

    def pop(self):
        if self.size() == 0:
            self.__pop_status = self.POP_ERR
            return
        self.__stack.pop()
        self.__pop_status = self.POP_OK

    def clear(self):
        self.__stack.clear()
        self.__push_status = self.PUSH_NIL
        self.__pop_status = self.POP_NIL
        self.__peek_status = self.PEEK_NIL

    def size(self):
        return len(self.__stack)

    def capacity(self):
        return self.__capacity

    def peek(self):
        if self.size() == 0:
            self.__peek_status = self.PEEK_ERR
            return 0
        self.__peek_status = self.PEEK_OK
        return self.__stack[-1]

    def get_push_status(self):
        return self.__push_status

    def get_peek_status(self):
        return self.__peek_status

    def get_pop_status(self):
        return self.__pop_status
