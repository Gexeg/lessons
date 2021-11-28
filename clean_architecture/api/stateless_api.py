import json
from dataclasses import asdict
from pure_robot import make, transfer_to_cleaner, RobotState

# Не совсем понимаю смысл в данной ситуации разбивать апи на множество команд, если мы принимаем от пользователя строку,
# которая в итоге разбирается на стороне движка. Под stateless понимаю пример системы, в котором состояние отделено 
# на слой хранилища, а логику его изменяющую (условно бизнес-логику) в другой слой. Получается мы оформляем логику в виде конвеера фукнций, 
# возвращающих нам новое состояние для сохранения в хранилище.  

#client_id : state
CLEANERS_STORAGE = {}


class ClientApi:
    def get_state(self, client_id):
        match CLEANERS_STORAGE.get(client_id):
            case RobotState() as state:
                return { "result": ResultCodes.SUCCESS, "state": json.dumps(asdict(state))}
            case _:
                return { "result": ResultCodes.ERROR, "state": "some_exception" }

    def handle_cleaner_command_list(self, command_list, client_id):
        match CLEANERS_STORAGE.get(client_id):
            case RobotState() as state:
                new_state = make(transfer_to_cleaner, commands, state)
                CLEANERS_STORAGE[client_id] = new_state
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
    cleaner_api = ClientApi()
    cleaner_api.handle_cleaner_command_list(commands, "1")
    print(cleaner_api.get_state("1"))

