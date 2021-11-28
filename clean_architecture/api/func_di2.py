import pure_robot

# В pure_robot немного изменил make для работы с одной командой и вынес её параметризацию transfer на уровень выше. 
# Не уверен, что get_maker правильное решение в данном случае, 
# но это позволяет поддерживать чуть меньшее количество параметров при дальнейших вызовах функции.

# def get_maker(transfer=transfer_to_cleaner):
#     def maker(code, state):
#         return make(transfer, code, state)
#     return maker

# def make(transfer, command, state):
#     cmd = command.split(' ')
#     if cmd[0]=='move':
#         state = move(transfer,int(cmd[1]),state) 
#     elif cmd[0]=='turn':
#         state = turn(transfer,int(cmd[1]),state)
#     elif cmd[0]=='set':
#         state = set_state(transfer,cmd[1],state) 
#     elif cmd[0]=='start':
#         state = start(transfer,state)
#     elif cmd[0]=='stop':
#         state = stop(transfer,state)
#     return state


class RobotApi:

    def setup(self, maker):
        self.maker = maker
        self.cleaner_state = None

    def make(self, command):
        if not self.cleaner_state:
            self.cleaner_state = pure_robot.RobotState(0.0, 0.0, 0, pure_robot.WATER)
        self.cleaner_state = self.maker(command, self.cleaner_state)

    def __call__(self, command):
        return self.make(command)


if __name__ == "__main__":
    api = RobotApi()    
    api.setup(pure_robot.get_maker(pure_robot.transfer_to_cleaner))

    api('move 100')
    api('turn -90')
    api('set soap')
    api('start')
    api('move 50')
    s = api('stop')