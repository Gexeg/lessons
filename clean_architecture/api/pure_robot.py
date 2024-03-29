import math
from typing import List, Optional
from dataclasses import dataclass
from collections import namedtuple


@dataclass
class RobotState:
    x: int = 0
    y: int = 0
    angle: int = 0
    state: Optional[str] = None

# режимы работы устройства очистки
WATER = 1 # полив водой
SOAP  = 2 # полив мыльной пеной
BRUSH = 3 # чистка щётками


# взаимодействие с роботом вынесено в отдельную функцию
def transfer_to_cleaner(message):
    print (message)

# перемещение
def move(transfer,dist,state):
    angle_rads = state.angle * (math.pi/180.0)   
    new_state = RobotState(
        state.x + dist * math.cos(angle_rads),
        state.y + dist * math.sin(angle_rads),
        state.angle,
        state.state)  
    transfer(('POS(',new_state.x,',',new_state.y,')'))
    return new_state

# поворот
def turn(transfer,turn_angle,state):
    new_state = RobotState(
        state.x,
        state.y,
        state.angle + turn_angle,
        state.state)
    transfer(('ANGLE',state.angle))
    return new_state

# установка режима работы
def set_state(transfer,new_internal_state,state):
    if new_internal_state=='water':
        self_state = WATER  
    elif new_internal_state=='soap':
        self_state = SOAP
    elif new_internal_state=='brush':
        self_state = BRUSH
    else:
        return state  
    new_state = RobotState(
        state.x,
        state.y,
        state.angle,
        self_state)
    transfer(('STATE',new_state))
    return new_state

# начало чистки
def start(transfer,state):
    transfer(('START WITH',state.state))
    return state

# конец чистки
def stop(transfer,state):
    transfer(('STOP',))
    return state


# интерпретация набора команд
def make_command_list(transfer,code,state):
    for command in code:
        cmd = command.split(' ')
        if cmd[0]=='move':
            state = move(transfer,int(cmd[1]),state) 
        elif cmd[0]=='turn':
            state = turn(transfer,int(cmd[1]),state)
        elif cmd[0]=='set':
            state = set_state(transfer,cmd[1],state) 
        elif cmd[0]=='start':
            state = start(transfer,state)
        elif cmd[0]=='stop':
            state = stop(transfer,state)
    return state


def make(transfer, command, state):
    cmd = command.split(' ')
    if cmd[0]=='move':
        state = move(transfer,int(cmd[1]),state) 
    elif cmd[0]=='turn':
        state = turn(transfer,int(cmd[1]),state)
    elif cmd[0]=='set':
        state = set_state(transfer,cmd[1],state) 
    elif cmd[0]=='start':
        state = start(transfer,state)
    elif cmd[0]=='stop':
        state = stop(transfer,state)
    return state


# 10 functional DI
# Как-то максимально сложно идет. Вроде у нас все возможные зависимости уже вынесены вне функциq. Единственное, что
# придумал, это вынесение `transfer` для получения команд предназначенных под конкретный тип роботов и дальнейшее их использование.


def get_maker(transfer=transfer_to_cleaner):
    def maker(code, state):
        return make(transfer, code, state)
    return maker

def get_mover(transfer=transfer_to_cleaner):
    def mover(dist,state):
        return move(transfer, dist, state)
    return mover

