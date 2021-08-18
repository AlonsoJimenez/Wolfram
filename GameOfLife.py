from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm



def ruleCalculator(array):
    countLife = 0
    result = array.copy()
    for rowIndex in range(3):
        for columnIndex in range(3):
            if columnIndex == 1 and rowIndex == 1:
                countLife += 0
            elif array[rowIndex][columnIndex] == 1:
                countLife += 1
    if (countLife >= 4) or (countLife <= 1):
        result[1,1] = 0
    elif countLife == 3:
        result [1,1] = 1
    return result


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



def updater(x):
    global grid
    newGrid = grid.copy()
    for i in range(1, 99):
      for j in range(1, 99):
          newGrid[i-1: i+2, j-1: j+2] = ruleCalculator(newGrid[i-1: i+2, j-1: j+2])
    mat.set_data(newGrid)
    grid = newGrid
    return [mat]


grid = createGliderGun()
fig, ax = plt.subplots()
ax.axis('off')
mat = ax.matshow(grid, cmap='Greys')
ani = animation.FuncAnimation(fig,  updater, interval=10, save_count=50, frames=600)
plt.show()



