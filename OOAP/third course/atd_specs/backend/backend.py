"""
Принимает запросы от фронта и занимается менеджментом запущенных сценариев

class Backend:

    public const int START_NONE = 0; // start_scenario() ещё не вызывалась
    public const int START_OK = 1; // последняя start_scenario() отработала нормально
    public const int START_ERR = 2; // последняя start_scenario() отработала нормально

    public const int REMOVE_NONE = 0; // remove_scenario() ещё не вызывалась
    public const int REMOVE_OK = 1; // последняя remove_scenario() отработала нормально
    public const int REMOVE_ERR = 2; // последняя remove_scenario() отработала нормально

    // КОНСТРУКТОР
    // постусловие: создан бэкенд
    def __init__()
        self.scenario_fabric
        self.scenario_storage
    // конец конструктора

    // КОМАНДЫ
    // Начать сценарий
    // предусловие: сценарий ещё не начат
    // постусловие: создан новый сценарий и сохранен под id
    public start_scenario(client_id: str, scenario_name: str)

    // Удалить текущий сценарий
    // предусловие: существует начатый сценарий с подобным идентификатором
    // постусловие: сценарий удален
    public remove_scenario(client_id: str, scenario_name: str)

    // Сделать ход
    // предусловие: существует начатый сценарий с подобным идентификатором
    // предусловие: передан корректный ход
    // постусловие: совершен ход, в сценарии появилось описание результата и следующие действия
    public make_move(client_id: str, move: str)

    // ЗАПРОСЫ
    // описание результата и список возможных ходов
    // предусловие: сценарий начат
    public get_scene_info(client_id: str) -> Tuple[str, list[str]]

    // Получить список возможных сценариев
    // предусловие: нет начатого сценария
    public get_scenarios_list(client_id: str) -> list[str]

    // текущий сценарий завершен?
    public is_game_over(client_id: str) -> bool

    // есть действующий сценаирй?
    public is_game_started(client_id: str) -> bool

    // дополнительные запросы:
    public get_start_scenario_status() -> int // возвращает значение START_*
    public get_remove_scenario_status() -> int // возвращает значение REMOVE_*
    public get_move_status() -> int // возвращает значение MOVE_*
"""
