"""
- Герой: структура, содержит основные игровые метрики.

class Hero:

    public const int HP_CHANGED_NONE = 0; // change_hp() ещё не вызывалась
    public const int HP_CHANGED_OK = 1; // последняя change_hp() отработала нормально
    public const int HP_CHANGED_ERR = 2; // последняя change_hp() отработала с ошибкой

    public const int ADD_TAG_NONE = 0; // add_tag() ещё не вызывалась
    public const int ADD_TAG_OK = 1; // последняя add_tag() отработала нормально
    public const int ADD_TAG_ERR = 2; // последняя add_tag() отработала с ошибкой

    public const int REMOVE_TAG_NONE = 0; // remove_tag() ещё не вызывалась
    public const int REMOVE_TAG_OK = 1; // последняя remove_tag() отработала нормально
    public const int REMOVE_TAG_ERR = 2; // последняя remove_tag() отработала с ошибкой

    // КОНСТРУКТОР
    // постусловие: создан новый герой с указанным именем
    def __init__(name: str)
    // конец конструктора

    // КОМАНДЫ
    // Изменить количество хитпоинтов
    // предусловие: увеличить количество хп можно, если персонаж не мертв
    // постусловие: хитпоинты персонажа изменены на указанное количество
    public change_hp(hp: int)

    // Добавить метку
    // предусловие: у героя нет такой метки
    // постусловие: герой получает новую метку.
    public add_tag(tag: str)

    // Удалить метку
    // предусловие: у героя есть метка
    // постусловие: удаляем метку
    public remove_tag(tag: str)

    // ЗАПРОСЫ
    // герой ещё жив?
    public is_alive() -> bool

    // У героя есть подобная метка?
    public has_tag(tag: str) -> bool

    // дополнительные запросы:
    public change_hp_status() -> int // возвращает значение HP_CHANGED_*
    public add_tag_status() -> int // возвращает значение ADD_TAG_*
    public remove_tag_status() -> int // возвращает значение REMOVE_TAG_*
"""
