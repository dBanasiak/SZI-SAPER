import pygame
from mapGeneratorPygame.randBomb import randBomb, bombType

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
bombPathList = randBomb(10)
# Typy wylosowanych 5 bomb
bombTypeList = bombType(10)

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

    screen.blit(pygame.image.load(bombPathList[0]), (128, 0))
    screen.blit(pygame.image.load(bombPathList[1]), (320, 0))
    screen.blit(pygame.image.load(bombPathList[2]), (512, 64))
    screen.blit(pygame.image.load(bombPathList[3]), (512, 64))
    screen.blit(pygame.image.load(bombPathList[4]), (128, 128))
    screen.blit(pygame.image.load(bombPathList[5]), (320, 128))
    screen.blit(pygame.image.load(bombPathList[6]), (512, 192))
    screen.blit(pygame.image.load(bombPathList[7]), (512, 192))
    screen.blit(pygame.image.load(bombPathList[8]), (128, 256))
    screen.blit(pygame.image.load(bombPathList[9]), (320, 256))

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
