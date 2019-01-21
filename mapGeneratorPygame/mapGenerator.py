import pygame
from ucs.allPriorityData import returnPriorityData

bombType = returnPriorityData()[0]
graphNodes = returnPriorityData()[1]
posList = returnPriorityData()[2]
priority = returnPriorityData()[3]
bombProp = returnPriorityData()[4]
mapMatrix = returnPriorityData()[5]
allBombs = []

bomb1Path = '../neuralNetwork/images/test1.png'
bomb2Path = '../neuralNetwork/images/test2.png'
bomb3Path = '../neuralNetwork/images/test3.png'
bomb4Path = '../neuralNetwork/images/test4.png'
bomb5Path = '../neuralNetwork/images/test5.png'
bomb6Path = '../neuralNetwork/images/test6.png'

bomb1 = pygame.image.load(bomb1Path)
bomb2 = pygame.image.load(bomb2Path)
bomb3 = pygame.image.load(bomb3Path)
bomb4 = pygame.image.load(bomb4Path)
bomb5 = pygame.image.load(bomb5Path)
bomb6 = pygame.image.load(bomb6Path)

def app():
    # Kolory
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Saper
    saper = pygame.image.load('saper/saper.png')
    escape = pygame.image.load('saper/escape.png')

    # Szerokość i wysokość okna aplikacji
    WINDOW_SIZE = [640, 640]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Automatyczny Saper - Mapa")
    pygame.init()
    pygame.font.init()
    done = False
    clock = pygame.time.Clock()
    FPS = 1
    myFont = pygame.font.SysFont('Comic Sans MS', 30)
    textSurface = []

    # Główna pętla
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)

        for i in range(10):
            for j in range(10):
                if mapMatrix[i][j] == 1:
                    screen.blit(saper, (i * 64, j * 64))
                if mapMatrix[i][j] == 15:
                    screen.blit(escape, (i * 64, j * 64))
                if mapMatrix[i][j] == 2:
                    screen.blit(bomb1, (i * 64, j * 64))
                if mapMatrix[i][j] == 3:
                    screen.blit(bomb2, (i * 64, j * 64))
                if mapMatrix[i][j] == 4:
                    screen.blit(bomb3, (i * 64, j * 64))
                if mapMatrix[i][j] == 5:
                    screen.blit(bomb4, (i * 64, j * 64))
                if mapMatrix[i][j] == 6:
                    screen.blit(bomb5, (i * 64, j * 64))
                if mapMatrix[i][j] == 7:
                    screen.blit(bomb6, (i * 64, j * 64))

        for i in range(10):
            textSurface.append(myFont.render(str(priority[i]), False, (0, 255, 17)))

        for i in range(10):
            screen.blit(textSurface[i], ((bombProp[i][4]) + 16, (bombProp[i][5]) + 16))

        pygame.display.flip()
        clock.tick(FPS)
