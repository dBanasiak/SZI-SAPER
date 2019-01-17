import pygame

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
done = False
clock = pygame.time.Clock()
FPS = 15

# mapMatrix = printBombAndPos()[1]

# allBombs = []
# i = 0
# for i in range(10):
#     allBombs.append(pygame.image.load(bombProp[i][3]))

neuralNetworkStop = False

# Główna pętla
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             done = True
    screen.fill(WHITE)

    # for row in mapMatrix:
    #     for col in row:
    #         if col == 1:
    #             screen.blit(saper, (x * 64, y * 64))
    #             x += 1
    #         if x == 10:
    #             y += 1
    #             x = 0
    #     if y == 10 and x == 9:
    #         x = 0
    #         y = 0
    #
    # i = 0
    # for i in range(10):
    #     screen.blit(allBombs[i], ((bombProp[i][4]), (bombProp[i][5])))

    pygame.display.flip()
    clock.tick(FPS)
