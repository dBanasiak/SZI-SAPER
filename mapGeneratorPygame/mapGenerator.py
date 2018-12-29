import pygame

# Kolory - Ale trzeba będzie zdefiniować bomby zamiast nich raczej
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
TEAL = (0, 255, 255)
YELLOW = (255, 255, 0)
GREY = (100, 100, 100)

# Szerokość i wysokość punktu
WIDTH = 20
HEIGHT = 20

# Odległość między kwadracikami
MARGIN = 1

# Dwuwymiarowa tablica
grid = []
for row in range(20):
    grid.append([])
    for column in range(20):
        grid[row].append(0)

#Ustawiam punkty początkowe
grid[1][3] = 1
grid[10][15] = 2
grid[18][5] = 3
grid[2][7] = 4
grid[9][5] = 5
grid[14][15] = 6
grid[0][0] = 7

# Inicjalizacja Pygame
pygame.init()

# Szerokość i wysokość okna aplikacji
WINDOW_SIZE = [420, 420]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Tytuł aplikacji
pygame.display.set_caption("Generator map")

# Fallback wyłączania apki
done = False

# Szybkość odświeżania aplikacji
clock = pygame.time.Clock()

# -------- Główna pętla -----------
while not done:
    for event in pygame.event.get():  # Listener
        if event.type == pygame.QUIT:  # Zamknij program
            done = True  # Flaga zamykanie apki
        elif event.type == pygame.KEYDOWN and event.key == 122: #Klawisz z
            pos = pygame.mouse.get_pos()
            column = pos[0]
            row = pos[1]
            grid[row][column] = 1
            print("Zielony ", pos, "Wybrales pozycje: ", row, column)
        elif event.type == pygame.KEYDOWN and event.key == 120: #Klawisz x
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1]
            grid[row][column] = 2
            print("Czerwony ", pos, "Wybrales pozycje: ", row, column)
        elif event.type == pygame.KEYDOWN and event.key == 99: #Klawisz c
            pos = pygame.mouse.get_pos()
            column = pos[0]
            row = pos[1]
            grid[row][column] = 3
            print("NIEBIESKI ", pos, "Wybrales pozycje: ", row, column)
        elif event.type == pygame.KEYDOWN and event.key == 118: #Klawisz v
            pos = pygame.mouse.get_pos()
            column = pos[0]
            row = pos[1]
            grid[row][column] = 4
            print("ROZOWY ", pos, "Wybrales pozycje: ", row, column)
        elif event.type == pygame.KEYDOWN and event.key == 98: #Klawisz b
            pos = pygame.mouse.get_pos()
            column = pos[0]
            row = pos[1]
            grid[row][column] = 5
            print("TURKUSOWY ", pos, "Wybrales pozycje: ", row, column)
        elif event.type == pygame.KEYDOWN and event.key == 110: #Klawisz n
            pos = pygame.mouse.get_pos()
            column = pos[0]
            row = pos[1]
            grid[row][column] = 6
            print("ZOLTY ", pos, "Wybrales pozycje: ", row, column)
        elif event.type == pygame.KEYDOWN and event.key == 27: # klawisz esc
            pos = pygame.mouse.get_pos()
            column = pos[0]
            row = pos[1]
            grid[row][column] = 0
            print("Bialy ", pos, "Wybrales pozycje: ", row, column)
        elif event.type == pygame.KEYDOWN:
            print(event.key)

    # Tło aplikacji
    screen.fill(BLACK)

    # Narysuj mape
    for row in range(20):
        for column in range(20):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = RED
            elif grid[row][column] == 3:
                color = BLUE
            elif grid[row][column] == 4:
                color = PINK
            elif grid[row][column] == 5:
                color = TEAL
            elif grid[row][column] == 6:
                color = YELLOW
            elif grid[row][column] == 7:
                color = GREY
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
