'''
abstract class LinkedList<T>

    public const int PUSH_NIL = 0; // push() ещё не вызывалась
    public const int PUSH_OK = 1; // последняя push() отработала нормально
    public const int PUSH_ERR = 2; // в стеке отсутствуют свободные слоты


    // конструктор
    // постусловие: создан новый пустой связный список. 
    public LinkedList<T> LinkedList(); 
    // конец конструктора


    // КОМАНДЫ
    // установить курсор на начало списка
    public void head()

    // установить курсор в конец списка
    public void tail()

    // сдвинуть курсор вправо
    public void right()

    // получить значение текущего узла
    public void get()

    // вставить следом за текущим узлом узел со значением
    public void put_right(T value)

    // вставить перед текущим узлом узел со значением
    public void put_left(T value)

    // Удалить текущий узел.
    // Если есть сосед справа, курсор смещается к нему
    // Иначе курсор смещается к левому соседу, если он есть
    public void remove()

    // очистить список
    public void clear()

    // посчитать количество узлов в списке
    public size()

    // добавить новый узел в хвост списка 
    public void add_tail(T value)

    // заменить значение текущего узла
    public void replace (T value)

    // установить курсор на следующий (по отношению к текушему) узел с искомым значением
    public void find(T value)

    // удалить в списке все узлы с заданным значением 
    public void remove_all(T value)

    // ЗАПРОСЫ
    // курсор находится в начале списка?
    public void is_head()
    // курсор находится в конце списка?
    public void is_tail()
    // установлен ли курсор на какой-либо узел в списке (равносильно "есть ли список?")
    public void is_value()

'''
