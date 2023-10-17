import pygame

# Constant for color
BLACK = (0, 0, 0)

class Grid:
    def __init__(self, grid_size, cell_size):
        self.grid_size = grid_size
        self.cell_size = cell_size

    def draw_grid(self, window):
        for i in range(self.grid_size + 1):
            pygame.draw.line(window, BLACK, (i * self.cell_size, 0), (i * self.cell_size, self.grid_size * self.cell_size))
            pygame.draw.line(window, BLACK, (0, i * self.cell_size), (self.grid_size * self.cell_size, i * self.cell_size))

    def get_cell_coordinates(self, x, y):
        cell_x = x // self.cell_size
        cell_y = y // self.cell_size
        return cell_x, cell_y
