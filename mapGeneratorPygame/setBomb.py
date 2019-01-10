from mapGeneratorPygame.emptyMatrix import emptyMatrix
import random

mergedMatrix = emptyMatrix()

def randBombPos():
    i = 0
    while i < 9:
        x = random.randrange(0, 9)
        y = random.randrange(0, 9)

        bomb = random.randrange(2, 7)

        if(mergedMatrix[x][y] == 0):
            mergedMatrix[x][y] = bomb
            i += 1
            print('Position - X: ', x, ' Y: ', y, ' Bomb: ', bomb)
        else:
            print('Field is not empty')

def returnBombAndPos():
    randBombPos()
    return mergedMatrix
