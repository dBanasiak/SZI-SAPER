import pygame
from mapGeneratorPygame.randBomb import randBomb, bombType

# Kolory
WHITE = (255, 255, 255)

# Saper
saper = pygame.image.load('saper/saper.png')
x = 0
y = 0

# Bomby
# timerBomb = pygame.image.load(timerPath)
# dynamiteBomb = pygame.image.load(dynamitePath)
# thBomb = pygame.image.load(thPath)
# bioBomb = pygame.image.load(bioPath)
# mineBomb = pygame.image.load(minePath)
# grenadeBomb = pygame.image.load(granadePath)

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

# Sieć neuronowa - Stwórz próbki do rozpoznania obrazów i sprawdź przykładowy obraz

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

    for i in range(0, 5):
        screen.blit(pygame.image.load(bombPathList[0]), (640, 0))
        screen.blit(pygame.image.load(bombPathList[1]), (128, 64))
        screen.blit(pygame.image.load(bombPathList[2]), (256, 128))
        screen.blit(pygame.image.load(bombPathList[3]), (64, 320))
        screen.blit(pygame.image.load(bombPathList[4]), (384, 320))

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

    pygame.display.update()
    clock.tick(FPS)
