import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


from mdbattleship.field import Field, Dot
from mdbattleship.battleship import Battleship


field_size = (5, 5, 5)

field = Field(field_size)

bs = Battleship([(0, 1, 0), (0, 1, 0)])
field.append_battleship(bs, (1, 1, 0))

ax = plt.axes(projection="3d")
ax.scatter([0], [0], [1], marker="v", alpha=0.95)
plt.show()