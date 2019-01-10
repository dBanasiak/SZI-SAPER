import pygame
from mapGeneratorPygame.setBomb import printBombAndPos
from neuralNetwork.imagerec import whatBombIsThis

# Kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Saper
saper = pygame.image.load('saper/saper.png')
x = 0
y = 0

# Ścieżka do danych tekstowych dla AI
exPath = '../neuralNetwork/numArEx.txt'
# Ścieżka do bazy przykładów dla AI
bombsPath = '../neuralNetwork/images/bombs/'

# Szerokość i wysokość okna aplikacji
WINDOW_SIZE = [640, 640]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Automatyczny Saper - Mapa")
pygame.init()
done = False
clock = pygame.time.Clock()
FPS = 15

bombProp = printBombAndPos()

allBombs = []
i = 0
for i in range(10):
    allBombs.append(pygame.image.load(bombProp[i][3]))

bombType = []

i = 0
for i in range(10):
    bombType.append(whatBombIsThis(bombProp[i][3], exPath))
print('\n',bombType)

# Główna pętla
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             done = True

    screen.fill(WHITE)
    screen.blit(saper, (x, y))

    i = 0
    for i in range(10):
        screen.blit(allBombs[i], ((bombProp[i][4]), (bombProp[i][5])))

    pygame.display.flip()
    clock.tick(FPS)
