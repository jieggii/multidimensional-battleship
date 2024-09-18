from mdbattleship.field import Field, Dot
from mdbattleship.battleship import Battleship


FIELD_SHAPE = (10, 10)
BATTLESHIPS = [
    Battleship([(0, 0)]),
    Battleship([(0, 0)]),
]

player1_field = Field(FIELD_SHAPE)
player1_field.set_dot((0, 0), Dot.BATTLESHIP)

player2_field = Field(FIELD_SHAPE)
player2_field.set_dot((0, 0), Dot.BATTLESHIP)


