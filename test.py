# Description:
#
# A simple Python/matplotlib implementation of Conway's Game of Life.
################################################################################

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

N = 100
ON = 255
OFF = 0
vals = [ON, OFF]

def createGliderGun():
    mesh = np.zeros((100,100))
    mesh[5][1] = 1
    mesh[5][2] = 1
    mesh[6][1] = 1
    mesh[6][2] = 1
    mesh[5][11] = 1
    mesh[6][11] = 1
    mesh[7][11] = 1
    mesh[4][12] = 1
    mesh[8][12] = 1
    mesh[3][13] = 1
    mesh[9][13] = 1
    mesh[3][14] = 1
    mesh[9][14] = 1
    mesh[6][15] = 1
    mesh[4][16] = 1
    mesh[8][16] = 1
    mesh[5][17] = 1
    mesh[6][17] = 1
    mesh[7][17] = 1
    mesh[6][18] = 1
    mesh[3][21] = 1
    mesh[4][21] = 1
    mesh[5][21] = 1
    mesh[3][22] = 1
    mesh[4][22] = 1
    mesh[5][22] = 1
    mesh[2][23] = 1
    mesh[6][23] = 1
    mesh[1][25] = 1
    mesh[2][25] = 1
    mesh[6][25] = 1
    mesh[7][25] = 1
    mesh[3][35] = 1
    mesh[4][35] = 1
    mesh[3][36] = 1
    mesh[4][36] = 1
    return mesh


# populate grid with random on/off - more off than on
grid = createGliderGun()

def update(data):
  global grid
  # copy grid since we require 8 neighbors for calculation
  # and we go line by line 
  newGrid = grid.copy()
  for i in range(N):
    for j in range(N):
      # compute 8-neghbor sum 
      # using toroidal boundary conditions - x and y wrap around 
      # so that the simulaton takes place on a toroidal surface.
      total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
               grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
               grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
               grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255
      # apply Conway's rules

      if (total < 2) or (total > 3):
        newGrid[i, j] = OFF
      else:
        if total == 3:
          newGrid[i, j] = ON
  # update data
  mat.set_data(newGrid)
  grid = newGrid
  return [mat]

# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50,
                              save_count=50)
plt.show()