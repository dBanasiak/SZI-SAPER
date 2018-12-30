import random as rand
from neuralNetwork.imagerec import whatBombIsThis, createExamples

# Ścieżka do danych tekstowych dla AI
exPath = '../neuralNetwork/numArEx.txt'
# Ścieżka do bazy przykładów dla AI
bombsPath = '../neuralNetwork/images/bombs/'
# Ścieżki dla 6 przykładowych bomb
bomb1Path = '../neuralNetwork/images/test1.png'
bomb2Path = '../neuralNetwork/images/test2.png'
bomb3Path = '../neuralNetwork/images/test3.png'
bomb4Path = '../neuralNetwork/images/test4.png'
bomb5Path = '../neuralNetwork/images/test5.png'
bomb6Path = '../neuralNetwork/images/test6.png'

# Lista ścieżek do bomb
bombPathArray = [bomb1Path, bomb2Path, bomb3Path, bomb4Path, bomb5Path, bomb6Path]
# Tablica randomowych liczb
randArray = []
# Tablica typów bomb
bombTypeArray = []

createExamples(bombsPath, exPath)

def randBomb(x):
    for i in range(0, x):
        randNum = rand.randint(0, 5)
        randArray.append((bombPathArray[randNum]))
    return randArray

def bombType(x):
    for i in range(0, x):
        bombTypeArray.append(whatBombIsThis(randArray[i], exPath))
    return bombTypeArray


