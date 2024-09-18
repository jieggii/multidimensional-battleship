from mdbattleship.dot import Dot
from mdbattleship import md_utils


class Map:
    _shape: tuple[int, ...]
    _order: int
    _map: list

    def __init__(self, shape: tuple[int, ...]):
        self._shape = shape
        self._order = len(shape)
        self._field = md_utils.init_multidimensional_list(shape, Dot.EMPTY.value)

