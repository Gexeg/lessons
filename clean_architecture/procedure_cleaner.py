from typing import List, Optional
from dataclasses import dataclass
from enum import Enum
from math import sin, cos, radians


class CleanerModes(str, Enum):
    water = "water"
    soap = "soap"
    brush = "brush"


class CleanerStatuses(Enum):
    active = (0, "active")
    stopped = (1, "stopped")

    def __init__(self, id, title):
        self.id = id
        self.title = title


class CleanerCommands(str, Enum):
    move = "move"
    turn = "turn"
    set_ = "set"
    start = "start"
    stop = "stop"


@dataclass
class RobotCleaner:
    x: int = 0
    y: int = 0
    angle: int = 0
    mode: Optional[CleanerModes] = None
    status: CleanerStatuses = CleanerStatuses.stopped
    command_separator: str = " "


class WrongCommandName(Exception):
    pass


class WrongCleanerMode(Exception):
    pass


class ModeNotSet(Exception):
    pass


def get_status(instance):
    print(
        f"""
            current point - (x={instance.x}, y={instance.y})
            current angle - {instance.angle}
            current mode - {instance.mode}
            current status - {instance.status.title}
        """
    )

def execute_command_list(instance, command_list: List[str]):
    for command in command_list:
        execute_command(instance, command)

def execute_command(instance, command: str):
    match command.split(sep=instance.command_separator):
        case [CleanerCommands.move, distance]:
            _move(instance, distance=int(distance))
        case [CleanerCommands.turn, angle]:
            _turn(instance, int(angle))
        case [CleanerCommands.set_, state]:
            _set(instance, state)
        case [CleanerCommands.start]:
            _start(instance)
        case [CleanerCommands.stop]:
            _stop(instance)
        case unknown_command:
            raise WrongCommandName(f"Can't find the command '{command}' in existed commands")

def _stop(instance):
    instance.status = CleanerStatuses.stopped
    print("STOP")

def _start(instance):
    if instance.mode is None:
        raise ModeNotSet("You must set the mode with the 'set' command before starting")
    instance.status = CleanerStatuses.active
    print(f"START WITH {instance.mode}")

def _turn(instance, angle: int):
    instance.angle = instance.angle + angle
    print(f"ANGLE {instance.angle}")

def _move(instance, distance: int):
    instance.x = distance * cos(instance.angle)
    instance.y = distance * sin(instance.angle)
    print(f"POS (x={instance.x}, y={instance.y})")

def _set(instance, mode):
    try:
        CleanerModes(mode)
    except ValueError:
        raise WrongCleanerMode(f"Can't find the mode '{mode}' in existed cleaner modes")
    instance.mode = CleanerModes(mode)
    print(f"STATE {instance.mode}")


if __name__ == "__main__":
    robot_cleaner = RobotCleaner()
    commands = [
        'move 100',
        'turn -90',
        'set soap',
        'start',
        'move 50',
        'stop'
    ]
    execute_command_list(robot_cleaner, commands)
    get_status(robot_cleaner)
