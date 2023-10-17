import pygame
from grid import Grid
from worm import Worm
from ant import Ant

DEBUG = False

# Initialise pygame
pygame.init()

# Constants for grid size and cell size
GRID_SIZE = 30
CELL_SIZE = 30

# Calculate window size based on grid and cell size
WINDOW_SIZE = (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE)

# Constants for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED  = (255, 0, 0)
GREEN = (0, 255, 0)

# Constants for directions
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

# Constant for step size
STEP_SIZE = 1

# Create a window
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Ants vs. Worms Game")

# Create a Grid instance
grid = Grid(GRID_SIZE, CELL_SIZE)

# Create worm and ant instances
worm = Worm(15, 15, CELL_SIZE)
ant = Ant(15, 15, CELL_SIZE)

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle user input for worm and ant movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        worm.move(UP, STEP_SIZE, GRID_SIZE)
    if keys[pygame.K_s]:
        worm.move(DOWN, STEP_SIZE, GRID_SIZE)
    if keys[pygame.K_a]:
        worm.move(LEFT, STEP_SIZE, GRID_SIZE)
    if keys[pygame.K_d]:
        worm.move(RIGHT, STEP_SIZE, GRID_SIZE)

    if keys[pygame.K_UP]:
        ant.move(UP, STEP_SIZE, GRID_SIZE)
    if keys[pygame.K_DOWN]:
        ant.move(DOWN, STEP_SIZE, GRID_SIZE)
    if keys[pygame.K_LEFT]:
        ant.move(LEFT, STEP_SIZE, GRID_SIZE)
    if keys[pygame.K_RIGHT]:
        ant.move(RIGHT, STEP_SIZE, GRID_SIZE)

    # Clear the screen and fill with white color
    window.fill(WHITE)
    
    # Draw grid lines
    grid.draw_grid(window)
    
    # Draw worms and ants on the grid
    worm.draw(window)
    if DEBUG: print(f"Worm Position: ({worm.x}, {worm.y})")
    ant.draw(window)
    if DEBUG: print(f"Ant Position: ({ant.x}, {ant.y})")
    
    # Update the display
    pygame.display.flip()
    
    # Limit the frame rate to 30 frames per second
    clock.tick(30)

pygame.quit()
