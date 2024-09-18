from enum import Enum


class Dot(int, Enum):
    EMPTY = 0
    BATTLESHIP = 1
    BATTLESHIP_DAMAGED = 2
    BATTLESHIP_DESTROYED = 3
