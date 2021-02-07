"""
class SceneFabric:

    public const int SCENE_CHANGED_NONE = 0; // change_scene() ещё не вызывалась
    public const int SCENE_CHANGED_OK = 1; // последняя change_scene() отработала нормально
    public const int SCENE_CHANGEDERR = 2; // последняя change_scene() отработала с ошибкой

    // КОНСТРУКТОР
    // постусловие: создана новая фабрика сцен
    def __init__()
    // конец конструктора

    // КОМАНДЫ
    // изменить текущую сцену
    // предусловие: есть следующая сцена
    // постусловие: переключить сцену на следующую
    public change_scene()

    // ЗАПРОСЫ
    // Есть следующая сцена?
    public has_next_scene() -> bool

    // Получить текущую сцену
    public get_scene() -> Scene

    // дополнительные запросы:
    public change_scene_status() -> int // возвращает значение SCENE_CHANGED_*
"""
