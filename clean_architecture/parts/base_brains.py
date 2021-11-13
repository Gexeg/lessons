from enum import Enum

class Statuses(Enum):
    active = (0, "active")
    stopped = (1, "stopped")

    def __init__(self, id, title):
        self.id = id
        self.title = title


class ModeNotSet(Exception):
    pass


def stop(instance):
    instance.status = Statuses.stopped
    print("STOP")

def start(instance):
    if instance.mode is None:
        raise ModeNotSet("You must set the mode with the 'set' command before starting")
    instance.status = Statuses.active
    print(f"START WITH {instance.mode}")
