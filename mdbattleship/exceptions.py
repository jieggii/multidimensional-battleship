from enum import Enum


class ObjectKind(str, Enum):
    COORDINATES = "coordinates"
    BATTLESHIP = "a battleship"
    VECTOR = "a vector"


class UnexpectedOrderException(Exception):
    def __init__(self, object_kind: ObjectKind, expected_order: int, actual_order: int):
        super().__init__(
            f"unexpected order of {object_kind.value}: expected order {expected_order}, got {actual_order}",
        )


class BattleshipCollisionException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)
