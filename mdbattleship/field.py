import typing

from mdbattleship.battleship import Battleship
from mdbattleship.exceptions import UnexpectedOrderException, ObjectKind, BattleshipCollisionException
from mdbattleship.md_utils import init_multidimensional_list, print_multidimensional_list
from mdbattleship.dot import Dot
from mdbattleship import md_utils


class Field:
    _shape: tuple[int, ...]
    _order: int
    _field: list

    def __init__(self, shape: tuple[int, ...]):
        self._shape = shape
        self._order = len(shape)
        self._field = init_multidimensional_list(shape, Dot.EMPTY.value)

    @property
    def shape(self) -> tuple[int, ...]:
        return self._shape

    @property
    def order(self) -> int:
        return self._order

    @property
    def field(self) -> list:
        return self._field

    def print(self):
        print_multidimensional_list(self._field)

    def get_dot(self, coordinates: tuple[int, ...]) -> Dot | typing.NoReturn:
        # verify order consistency:
        coordinates_order = len(coordinates)
        if coordinates_order != self._order:
            raise UnexpectedOrderException(ObjectKind.COORDINATES, self._order, coordinates_order)

        # get the desired dot:
        target = self._field
        for index in coordinates:
            target = target[index]
        return Dot(target)

    def set_dot(self, coordinates: tuple[int, ...], value: Dot) -> None | typing.NoReturn:
        # verify order consistency:
        coordinates_order = len(coordinates)
        if coordinates_order != self._order:
            raise UnexpectedOrderException(ObjectKind.COORDINATES, self._order, coordinates_order)

        # update the desired dot:
        target = self._field
        for index in coordinates[:-1]:
            target = target[index]
        target[coordinates[-1]] = value.value

    def battleships_around(self, coordinates: tuple[int, ...]) -> bool:
        # verify order consistency:
        coordinates_order = len(coordinates)
        if coordinates_order != self._order:
            raise UnexpectedOrderException(ObjectKind.COORDINATES, self._order, coordinates_order)

        # find coordinates of existing neighbours:
        delta_vectors = md_utils.generate_delta_vectors(self._order)
        neighbours: list[tuple[int, ...]] = []  # list of coordinates of existing neighbours
        for vector in delta_vectors:
            skip_vector = False

            # calculate neighbours coordinates:
            neighbour_coordinates = list(coordinates)
            for i, vec_coord in enumerate(vector):
                neighbour_coordinate = neighbour_coordinates[i] + vec_coord
                neighbour_coordinates[i] = neighbour_coordinate

                # skip the current vector if it leads to a dot which is out of bounds:
                if neighbour_coordinate < 0 or neighbour_coordinate > self._shape[i]:
                    skip_vector = True
                    break

            if not skip_vector:
                neighbours.append(tuple(neighbour_coordinates))

        # check neighbours:
        for dot in neighbours:
            if self.get_dot(dot) in (Dot.BATTLESHIP.value, Dot.BATTLESHIP_DAMAGED.value, Dot.BATTLESHIP_DESTROYED.value):
                return True
        return False

    def append_battleship(self, battleship: Battleship, coordinates: tuple[int, ...]) -> typing.NoReturn | None:
        # verify order consistency:
        coordinates_order = len(coordinates)
        if coordinates_order != self._order:
            raise UnexpectedOrderException(ObjectKind.COORDINATES, self._order, coordinates_order)

        if (battleship.order is not None) and (battleship.order != self._order):
            raise UnexpectedOrderException(ObjectKind.BATTLESHIP, self._order, battleship.order)

        # fill the dots:
        current_dot: list[int] = list(coordinates)
        for vec in battleship.vectors:
            # calculate current dot coordinates:
            for i in range(self._order):
                current_dot[i] += vec[i]

            # fill the current dot:
            if self.get_dot(tuple(current_dot)) == Dot.BATTLESHIP:
                raise BattleshipCollisionException(f"there is already a battleship in {tuple(current_dot)}")
            self.set_dot(tuple(current_dot), Dot.BATTLESHIP)

    def get_map(self):
        pass
