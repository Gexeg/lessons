from typing import NamedTuple
import pure_robot


def wrapped_move(arg):
    def m(state):
        return pure_robot.move(pure_robot.transfer_to_cleaner, arg, state)
    return m


def wrapped_set_state(arg):
    def m(state):
        return pure_robot.set_state(pure_robot.transfer_to_cleaner, arg, state)
    return m


def wrapped_start():
    def m(state):
        return pure_robot.start(pure_robot.transfer_to_cleaner, state)
    return m


def wrapped_stop():
    def m(state):
        return pure_robot.stop(pure_robot.transfer_to_cleaner, state)
    return m


def wrapped_turn(arg):
    def m(state):
        return pure_robot.turn(pure_robot.transfer_to_cleaner, arg, state)
    return m


class M:
    __slots__ = ("state")

    def __init__(self, state=None):
        self.state = state or pure_robot.RobotState()


    def bind(self, wrapped_cmd):
        self.state = wrapped_cmd(self.state)
        return self

    def unwrap(self):
        return self.state


if __name__ == "__main__":
    print((
        M()
        .bind(wrapped_move(100))
        .bind(wrapped_turn(-90))
        .bind(wrapped_set_state("soap"))
        .bind(wrapped_start())
        .bind(wrapped_move(50))
        .bind(wrapped_stop())
        .unwrap()
    ))
