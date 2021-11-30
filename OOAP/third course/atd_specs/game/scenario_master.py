"""
- Сценарий:
- основная логика тут.
— формирует список возможных ходов. (содержит в себе системные ходы, доступные всегда и получает возможные ходы от "сцены")
— переключает сцены по мере их прохождения
— отслеживает конец игры
— получает команды  и возвращает ему реакцию (описание и список новых доступных команд)

class ScenarioMaster:

    // КОНСТРУКТОР
    // постусловие: создан новый сценарий.
    def __init__()
        self.scene_fabric
        self.hero
    // конец конструктора

    // КОМАНДЫ
    // выполнить ход
    // предусловие: игра не закончилась
    // предусловие: ход есть в списке допустимых
    // постусловие: появляется описание результатов хода и новый набор действий
    public make_move(move: str)

    // ЗАПРОСЫ
    // Получить описание ситуации и возможные ходы
    public get_scene_info() -> Tuple[str, list[str]]

    // Игра закончилась?
    public is_game_over() -> bool

    // Получить концовку
    public get_ending() -> str

    // дополнительные запросы:
    public get_move_status() -> int // возвращает значение MOVE_*
"""