from typing import NamedTuple
import pure_robot

# Как понимаю главным образом нам нужен какой-то транслятор, чтобы вылавливать из стрима команды и складывать их в стек.
# Когда дана команда к исполнению или стрим закончился, мы достаем команды из стека и исполняем их. Команды должны исполняться
# только по сигналу и в обратном порядке, так что собирал их в отдельные объекты.



COMMANDS = {
    "move": pure_robot.move,
    "set": pure_robot.set_state,
    "start": pure_robot.start,
    "stop": pure_robot.stop,
    "turn": pure_robot.turn,
}


class Command:
    __slots__ = ("cmd", "arg")

    def __init__(self):
        self.cmd = None
        self.arg = None

    def __call__(self, state, transfer):
        if self.arg:
            self._try_int()
            return self.cmd(transfer, self.arg, state)
        return self.cmd(transfer, state)

    def _try_int(self):
        try:
            self.arg = int(self.arg)
        except ValueError:
            return

def translator(stream):
    tokenized_stream = stream.split()
    command_stack = []
    cmd = Command()
    while tokenized_stream:
        el = tokenized_stream.pop()
        if el in COMMANDS:
            if cmd.cmd is not None:
                command_stack.append(cmd)
                cmd = Command()
            cmd.cmd = COMMANDS[el]
            continue
        cmd.arg = el
    command_stack.append(cmd)
    return command_stack


if __name__ == "__main__":
    cmd_stream = "100 move -90 turn soap set start 50 move stop"
    state = pure_robot.RobotState()
    stack = translator(cmd_stream)
    while stack:
        cmd = stack.pop()
        state = cmd(state, pure_robot.transfer_to_cleaner)
    print(state)
