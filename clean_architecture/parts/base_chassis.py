from math import sin, cos, radians


def turn(instance, angle: int):
    instance.angle = instance.angle + angle
    print(f"ANGLE {instance.angle}")

def move(instance, distance: int):
    instance.x = distance * cos(instance.angle)
    instance.y = distance * sin(instance.angle)
    print(f"POS (x={instance.x}, y={instance.y})")
