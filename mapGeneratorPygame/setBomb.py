from mapGeneratorPygame.emptyMatrix import emptyMatrix
import random

mergedMatrix = emptyMatrix()
bombProp = []

# Ścieżki dla 6 przykładowych bomb
bomb1Path = '../neuralNetwork/images/test1.png'
bomb2Path = '../neuralNetwork/images/test2.png'
bomb3Path = '../neuralNetwork/images/test3.png'
bomb4Path = '../neuralNetwork/images/test4.png'
bomb5Path = '../neuralNetwork/images/test5.png'
bomb6Path = '../neuralNetwork/images/test6.png'

# Lista ścieżek do bomb
bombPathArray = ['empty', 'saper', bomb1Path, bomb2Path, bomb3Path, bomb4Path, bomb5Path, bomb6Path]

def randBombPos():
    i = 0
    while i <= 9:
        x = random.randrange(0, 9)
        y = random.randrange(0, 9)
        bomb = random.randrange(2, 7)

        if(mergedMatrix[x][y] == 0):
            mergedMatrix[x][y] = bomb
            i += 1
            bombProp.append((x, y, bomb, bombPathArray[bomb], x * 64, y * 64, i))

def printBombAndPos():
    randBombPos()
    # print('\nBomb properties:\n', bombProp)
    # print('\nSet bomb:')
    # for row in mergedMatrix:
    #     print(row)
    return bombProp, mergedMatrix


