"""
Хранит запущенные сценарии

class ScenarioStorage:

    public const int SAVE_NONE = 0; // make_move() ещё не вызывалась
    public const int SAVE_OK = 1; // последняя make_move() отработала нормально
    public const int SAVE_ERR = 2; // последняя make_move() отработала нормально

    public const int REMOVE_NONE = 0; // remove_scenario() ещё не вызывалась
    public const int REMOVE_OK = 1; // последняя remove_scenario() отработала нормально
    public const int REMOVE_ERR = 2; // последняя remove_scenario() отработала нормально

    // КОНСТРУКТОР
    // постусловие: создан объект хранилища сценариев
    def __init__()
    // конец конструктора

    // КОМАНДЫ
    // Начать сценарий
    // предусловие: сценарий ещё не присутствует в хранилище
    // постусловие: сценарий сохранен
    public save(scenario_id: str)

    // Удалить сценарий
    // предусловие: в хранилище существует сценарий с этим ид
    // постусловие: сценарий удален
    public remove(scenario_id: str)

    // ЗАПРОСЫ
    // получить сценарий
    // предусловие: сценарий присутствует в хранилище
    public get_scenario(scenario_id: str) -> Scenario

    // сценарий присутствует в хранилище?
    public is_game_over(scenario_id: str) -> bool

    // дополнительные запросы:
    public get_save_status() -> int // возвращает значение SAVE_*
    public get_remove_status() -> int // возвращает значение REMOVE_*
"""
