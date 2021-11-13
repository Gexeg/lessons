from enum import Enum


class Modes(str, Enum):
    water = "water"
    soap = "soap"
    brush = "brush"


class WrongMode(Exception):
    pass

def set_mode(instance, mode):
    try:
        Modes(mode)
    except ValueError:
        raise WrongMode(f"Can't find the mode '{mode}' in existed cleaner modes")
    instance.mode = Modes(mode)
    print(f"STATE {instance.mode}")
