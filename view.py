import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


from mdbattleship.field import Field, Dot
from mdbattleship.battleship import Battleship


field_size = (10, 10, 10)

field = Field(field_size)

bs = Battleship([(0, 1, 0), (0, 1, 0)])
field.append_battleship(bs, (1, 1, 0))


axes = list(field_size)

# Create Data
data = np.array(field.field, dtype=bool)

# Plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.voxels(data, edgecolors='black')
# ax.view_init(0, 45)
# fig.show()
plt.show()
