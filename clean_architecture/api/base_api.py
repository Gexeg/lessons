from pure_robot import make, transfer_to_cleaner, RobotState

#client_id : state
CLEANERS_STORAGE = {}

def handle_cleaner_command_list(command_list, client_id):
    match CLEANERS_STORAGE.get(client_id):
        case RobotState() as state:
            new_state = make(transfer_to_cleaner, commands, state)
            CLEANERS_STORAGE[client_id] = new_state
            return new_state
        case _:
            return "some exception"


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
    handle_cleaner_command_list(commands, client_id)
