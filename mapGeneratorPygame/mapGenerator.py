import pygame
import sys
from mapGeneratorPygame.setBomb import printBombAndPos
from neuralNetwork.imagerec import whatBombIsThis, createExamples
from mapGeneratorPygame.dataRandomGenerator import getTime, getCost
from decisionTree.decisionTree import build_default_tree, simple_classify

bombProp = printBombAndPos()[0]
mapMatrix = printBombAndPos()[1]

bombsForUCS = []
allBombs = []
i = 0
for i in range(10):
    allBombs.append(pygame.image.load(bombProp[i][3]))

def returnMapWithBombs():
    for i in range(10):
        bombsForUCS.append((bombProp[i][0], bombProp[i][1], bombProp[i][2]))
    return bombsForUCS, mapMatrix, bombProp

def app():
    # Kolory
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Saper
    saper = pygame.image.load('saper/saper.png')
    x = 0
    y = 0

    # Szerokość i wysokość okna aplikacji
    WINDOW_SIZE = [640, 640]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Automatyczny Saper - Mapa")
    pygame.init()
    pygame.font.init()
    done = False
    clock = pygame.time.Clock()
    FPS = 15
    myFont = pygame.font.SysFont('Comic Sans MS', 30)
    textSurface = []

    counter, counterText = [], []

    counterFont = pygame.font.SysFont('Consolas', 30)

    # Ścieżka do danych tekstowych dla AI
    exPath = '../neuralNetwork/numArEx.txt'
    # Ścieżka do bazy przykładów dla AI
    bombsPath = '../neuralNetwork/images/bombs/'

    allBombs = []
    i = 0
    for i in range(10):
        allBombs.append(pygame.image.load(bombProp[i][3]))
    bombType = []
    priority = []

    neuralNetworkStop = False

    # Główna pętla
    while not done:

        if neuralNetworkStop == False:
            i = 0
            createExamples(bombsPath, exPath)
            tree = build_default_tree()
            for i in range(10):
                whatBombIsIt = whatBombIsThis(bombProp[i][3], exPath)
                bombType.append((whatBombIsIt, getTime(whatBombIsIt), getCost(whatBombIsIt), bombProp[i][2], bombProp[i][4],
                                 bombProp[i][5]))
                print('Progres skanowania pola minowego: ', 10 * len(bombType), '%')
            for row in bombType:
                priorityVal = simple_classify(row, tree)
                textSurface.append(myFont.render(str(priorityVal), False, (0, 255, 17)))
                priority.append(priorityVal)
                print(row, ' => ', priorityVal)
                counter.append(row[1])
                if row[1] != sys.maxsize:
                    counterText.append(str(row[1]).rjust(2))
                else:
                    counterText.append(str('').rjust(2))
            neuralNetworkStop = True
            pygame.time.set_timer(pygame.USEREVENT, 1000)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.USEREVENT:
                for i in range(10):
                    if counter[i] != sys.maxsize:
                        counter[i] -= 1
                        counterText[i] = str(counter[i]).rjust(2) if counter[i] > 0 else ' X'
        screen.fill(WHITE)

        for row in mapMatrix:
            for col in row:
                if col == 1:
                    screen.blit(saper, (x * 64, y * 64))
                    x += 1
                if x == 10:
                    y += 1
                    x = 0
            if y == 10 and x == 9:
                x = 0
                y = 0

        i = 0
        for i in range(10):
            screen.blit(allBombs[i], ((bombProp[i][4]), (bombProp[i][5])))
            screen.blit(textSurface[i], ((bombProp[i][4]) + 16, (bombProp[i][5]) + 16))
            screen.blit(counterFont.render(counterText[i], True, (0, 229, 255)), ((bombProp[i][4]), (bombProp[i][5])))

        pygame.display.flip()
        clock.tick(FPS)
