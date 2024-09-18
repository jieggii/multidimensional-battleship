import argparse
import random

from mdbattleship.field import Field
from mdbattleship.battleship import Battleship
from mdbattleship.exceptions import BattleshipCollisionException


BATTLESHIPS = [
    Battleship([(0, 0, 0), (0, 1, 0)]),
    Battleship([(0, 0, 0), (0, 1, 0)]),
    Battleship([(0, 0, 0), (0, 1, 0)]),
    Battleship([(0, 0, 0), (0, 1, 0)]),
]


def parse_args():
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def main():
    shape = (10, 10, 10)

    # initialize fields:
    field1 = Field(shape)
    field2 = Field(shape)

    print("placing battleships...")
    for battleship in BATTLESHIPS:
        x, y, z = random.randint(0, shape[0]), random.randint(0, shape[1]), random.randint(0, shape[2])
        while True:
            try:
                field1.append_battleship(battleship, (x, y, z))
            except BattleshipCollisionException:
                continue
        while True:
            try:
                field2.append_battleship(battleship, (x, y, z))
            except BattleshipCollisionException:
                continue
    field1.print()
    field2.print()

if __name__ == '__main__':
    main()
