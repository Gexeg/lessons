from typing import List, Optional
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


class WrongCommandName(Exception):
    pass


class WrongCleanerMode(Exception):
    pass


class ModeNotSet(Exception):
    pass


class RobotCleaner:
    def __init__(self, command_separator: str = " "):
        self._x: int = 0
        self._y: int = 0
        self._angle: int = 0
        self._mode: Optional[CleanerModes] = None
        self._status: CleanerStatuses = CleanerStatuses.stopped
        
        self._command_separator: str = command_separator

    def get_status(self):
        print(
            f"""
                current point - (x={self._x}, y={self._y})
                current angle - {self._angle}
                current mode - {self._mode}
                current status - {self._status}
            """
        )

    def execute_command_list(self, command_list: List[str]):
        for command in command_list:
            self.execute_command(command)

    def execute_command(self, command: str):
        match command.split(sep=self._command_separator):
            case [CleanerCommands.move, distance]:
                self._move(distance=int(distance))
            case [CleanerCommands.turn, angle]:
                self._turn(int(angle))
            case [CleanerCommands.set_, state]:
                self._set(state)
            case [CleanerCommands.start]:
                self._start()
            case [CleanerCommands.stop]:
                self._stop()
            case unknown_command:
                raise WrongCommandName(f"Can't find the command '{command}' in existed commands")

    def _stop(self):
        self._status = CleanerStatuses.stopped
        print("STOP")

    def _start(self):
        if self._mode is None:
            raise ModeNotSet("You must set the mode with the 'set' command before starting")
        self._status = CleanerStatuses.active
        print(f"START WITH {self._mode}")

    def _turn(self, angle: int):
        self._angle = self._angle + angle
        print(f"ANGLE {self._angle}")

    def _move(self, distance: int):
        self._x = distance * cos(radians(self._angle))
        self._y = distance * sin(radians(self._angle))
        print(f"POS (x={self._x}, y={self._y})")

    def _set(self, mode):
        try:
            CleanerModes(mode)
        except ValueError:
            raise WrongCleanerMode(f"Can't find the mode '{mode}' in existed cleaner modes")
        self._mode = CleanerModes(mode)
        print(f"STATE {self._mode.value}")


if __name__ == "__main__":
    cleaner = RobotCleaner()
    commands = [
        'move 100',
        'turn -90',
        'set soap',
        'start',
        'move 50',
        'stop'
    ]
    cleaner.execute_command_list(commands)
    cleaner.get_status()
