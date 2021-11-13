from typing import List, Optional
from dataclasses import dataclass
from enum import Enum
from math import sin, cos, radians

import parts.base_body as body
import parts.base_brains as brains
import parts.base_chassis as chassis

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
    mode: Optional[body.Modes] = None
    status: brains.Statuses = brains.Statuses.stopped
    command_separator: str = " "

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
            chassis.move(instance, distance=int(distance))
        case [CleanerCommands.turn, angle]:
            chassis.turn(instance, int(angle))
        case [CleanerCommands.set_, state]:
            body.set_mode(instance, state)
        case [CleanerCommands.start]:
            brains.start(instance)
        case [CleanerCommands.stop]:
            brains.stop(instance)
        case unknown_command:
            raise WrongCommandName(f"Can't find the command '{command}' in existed commands")


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
