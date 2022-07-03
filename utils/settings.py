import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
MAGENTA = (255,0,255)
YELLOW = (255,255,0)

FPS = 240
WIDTH, HEIGHT = 600, 700
ROWS = COLS = 100
TOOLBAR_HEIGHT = HEIGHT - WIDTH
PIXEL_SIZE = WIDTH // COLS
BACKGROUND_COLOR = WHITE
DRAW_GRID_LINES = False

def get_font(size):
    return pygame.font.SysFont("comicsans", size)