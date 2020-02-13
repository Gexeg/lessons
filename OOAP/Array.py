'''
class DynArray<T>

    public const int INSERT_NONE = 0; // insert() ещё не вызывалась
    public const int INSERT_OK = 1; // последняя insert() отработала нормально
    public const int INSERT_ERR = 2; // текущий индекс

    public const int REMOVE_NONE = 0; // remove() ещё не вызывалась
    public const int REMOVE_OK = 1; // последняя remove() отработала нормально
    public const int REMOVE_ERR = 2; // в слоте отсутствует значение или нет слота по данному индексу

    public const int GET_VALUE_NONE = 0; // get_value() ещё не вызывалась
    public const int GET_VALUE_OK = 1; // последняя get_value() отработала нормально
    public const int GET_VALUE_ERR = 2; // в слоте отсутствует значение или нет слота по данному индексу

    // КОНСТРУКТОР
    // постусловие: создан новый пустой массив с вместимостью = 16 (минимальное неуменьшаемое значение). 
    public LinkedList<T> LinkedList();
        private int capacity = 16 
    // конец конструктора


    // КОМАНДЫ
    // поместить значение в слот под указанным индексом
    // предусловие: слот пуст
    // предусловие: указанный индекс присутствует в массиве
    // постусловие: в слот под указанным индексом помещено значение
    // постусловие: если заполнен последний свободный слот в массиве, вместимость увеличена в 2 раза
    public void insert(T value, int index)

    // удалить значение из слота под указанным индексом
    // предусловие: слот содержит значение
    // предусловие: указанный индекс присутствует в массиве
    // постусловие: в слот под указанным индексом помещено значение
    // постусловие: если в массиве заполнено меньше 1∕2 слотов, вместимость уменьшена в 1,5 раза
    public void remove(int index)


    // ЗАПРОСЫ
    // получить значение из слота
    // предусловие: слот содержит значение
    // предусловие: указанный индекс присутствует в массиве
    public void get_value(int index)

    // получить текущую вместимость списка
    public void get_capacity()

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
