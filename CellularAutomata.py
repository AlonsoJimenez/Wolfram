import numpy as np
import matplotlib.pyplot as plt

def generateRulePattern(rule):
    pattern = np.binary_repr(rule, width = 8)
    patternSlice = []
    for x in range(8):
        patternSlice += [int(pattern[x])]
    return patternSlice

def createMesh(columns, rows):
    if((columns%2) != 0 ):
        columns += 1
    mesh = np.zeros([rows, columns])
    mesh[0, int(columns/2)+1] = 1
    return mesh

def ruleCalculator(rule, array):
    result = [0]
    for index in range(len(array)+1):
        arraySlice = array[index: index+3]
        if np.array_equal(arraySlice, [1,1,1]):
            result += [rule[0]]
        elif np.array_equal(arraySlice, [1,1,0]):
            result += [rule[1]]
        elif np.array_equal(arraySlice, [1,0,1]):
            result += [rule[2]]
        elif np.array_equal(arraySlice, [1,0,0]):
            result += [rule[3]]
        elif np.array_equal(arraySlice, [0,1,1]):
            result += [rule[4]]
        elif np.array_equal(arraySlice, [0,1,0]):
            result += [rule[5]]
        elif np.array_equal(arraySlice, [0,0,1]):
            result += [rule[6]]
        elif np.array_equal(arraySlice, [0,0,0]):
            result += [rule[7]]
    result += [0]
    return result

def executeCA():
    rule = int(input("Number between 0-256: "))
    columns = int(input("Colums: "))
    rows = int(input("Rows: "))
    rule = generateRulePattern(rule)
    mesh = createMesh(columns, rows)
    for row in range(rows-1):
        newArray = ruleCalculator(rule, mesh[row, :])
        mesh[row+1, :] = newArray
    plt.imshow(mesh[:, 1:columns], cmap='Greys', interpolation= 'nearest')
    plt.show()

executeCA()
        



