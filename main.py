import pygame
from utils.settings import *
from utils.functions import *
from utils.buttons import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint - WhiteRoseX")

run = True
clock = pygame.time.Clock()
grid = init_grids(ROWS, COLS, BACKGROUND_COLOR)
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, MAGENTA),
    Button(250, button_y, 50, 50, YELLOW),
    Button(310, button_y, 50, 50, BLUE),
    Button(370, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(430, button_y, 50, 50, WHITE, "Clear", BLACK)
]


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_raw_cols_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    drawing_color = button.color
                    if  button.text == "Clear":
                        grid = init_grids(ROWS, COLS, BACKGROUND_COLOR)

    draw(WIN, grid, buttons)


pygame.quit()
