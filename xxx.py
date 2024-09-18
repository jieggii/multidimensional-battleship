import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

# Define the size of the field
field_size = (10, 10, 10)

# Create a 3D numpy array to represent the field
field = np.zeros(field_size, dtype=bool)

# Define the position and shape of the battleship
ship_position = (1, 1, 0)
ship_shape = (1, 2, 1)  # Example battleship of size 1x2x1

# Place the battleship on the field
field[ship_position[0]:ship_position[0]+ship_shape[0],
      ship_position[1]:ship_position[1]+ship_shape[1],
      ship_position[2]:ship_position[2]+ship_shape[2]] = True

# Plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the battleship
ax.voxels(field, edgecolors='black')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Battleship Game')

# Show plot
plt.show()
