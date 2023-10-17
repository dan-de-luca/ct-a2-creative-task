import pygame

# Constant for worm image
WORM_IMAGE = "assets/worm-2.png"

# Constants for directions
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

class Worm:
    def __init__(self, x, y, cell_size):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.image = pygame.image.load(WORM_IMAGE)
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))

    def move(self, direction, step_size, grid_size):
        if direction == UP:
            self.y = max(self.y - step_size, 0)
        elif direction == DOWN:
            self.y = min(self.y + step_size, grid_size - 1)
        elif direction == LEFT:
            self.x = max(self.x - step_size, 0)
        elif direction == RIGHT:
            self.x = min(self.x + step_size, grid_size - 1)

    def draw(self, window):
        window.blit(self.image, (self.x * self.cell_size, self.y * self.cell_size))

