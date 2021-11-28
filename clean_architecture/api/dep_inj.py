import json
from dataclasses import asdict
from pure_robot import get_cleaner_maker, RobotState

# вынес хранилище, обработку данных в отдельные зависимости.

#client_id : state
CLEANERS_STORAGE = {}


class ClientApi:
    def __init__(self, cleaner_storage, cleaner_maker):
        self.maker = cleaner_maker
        self.storage = cleaner_storage
    
    def get_state(self, client_id):
        match self.storage.get(client_id):
            case RobotState() as state:
                return { "result": ResultCodes.SUCCESS, "state": json.dumps(asdict(state))}
            case _:
                return { "result": ResultCodes.ERROR, "state": "Can't find robot state" }

    def handle_cleaner_command_list(self, command_list, client_id):
        match self.storage.get(client_id):
            case RobotState() as state:
                new_state = self.maker(commands, state)
                self.storage[client_id] = new_state
                return { "result": ResultCodes.SUCCESS, "state": "success"}
            case _:
                return { "result": ResultCodes.ERROR, "state": "some_exception" }


class ResultCodes:
    SUCCESS = 1
    ERROR = 2


if __name__ == "__main__":
    robot_cleaner = RobotState()
    client_id = "1"
    CLEANERS_STORAGE[client_id] = robot_cleaner
    commands = [
        'move 100',
        'turn -90',
        'set soap',
        'start',
        'move 50',
        'stop'
    ]
    cleaner_api = ClientApi(CLEANERS_STORAGE, get_cleaner_maker())
    print(cleaner_api.handle_cleaner_command_list(commands, "1"))
    print(cleaner_api.get_state("1"))

