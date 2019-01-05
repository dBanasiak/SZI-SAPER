import pygame
from mapGeneratorPygame.randBomb import randBomb, bombType
from ucs.ucsAlgorithm import returnBombPos

# Kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Saper
saper = pygame.image.load('saper/saper.png')
x = 0
y = 0

# Szerokość i wysokość okna aplikacji
WINDOW_SIZE = [1024, 640]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Automatyczny Saper - Mapa")
pygame.init()
done = False
clock = pygame.time.Clock()
FPS = 15

# Wylosowane 5 bomb
bombPathList = randBomb(5)
# Typy wylosowanych 5 bomb
bombTypeList = bombType(5)

#bomby
bomb1 = pygame.image.load(bombPathList[0])
bomb2 = pygame.image.load(bombPathList[1])
bomb3 = pygame.image.load(bombPathList[2])
bomb4 = pygame.image.load(bombPathList[3])
bomb5 = pygame.image.load(bombPathList[4])

bombPosList = returnBombPos()


print(bombPosList[0])

print(bombTypeList)

# Główna pętla
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             done = True
        # cofnij robota do początku po kliknięciu klawisza z
        elif event.type == pygame.KEYDOWN and event.key == 122:
            x = 0
            y = 0

    screen.fill(WHITE)
    screen.blit(saper, (x, y))

    screen.blit(bomb1, bombPosList[0])
    screen.blit(bomb2, bombPosList[1])
    screen.blit(bomb3, bombPosList[2])
    screen.blit(bomb4, bombPosList[3])
    screen.blit(bomb5, bombPosList[4])

    # Naiwne poruszanie się robota
    if y < 576:
        if x < 1024:
            x += 64
        if x == 1024:
            y += 64
            x = 0
    if y == 576:
        if x < 960:
            x += 64

    pygame.display.flip()
    clock.tick(FPS)
