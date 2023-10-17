import pygame
import random

DEBUG = False

# Define heatmap colors
HOT_COLOR_GRADIENT = [
    pygame.Color("#FF0000"),  # Red
    pygame.Color("#FF3300"),  # Orange
    pygame.Color("#FF6600"),  # Light orange
    pygame.Color("#FF9900"),  # Yellow-orange
    pygame.Color("#FFCC00"),  # Yellow
]

COLD_COLOR_GRADIENT = [
    pygame.Color("#0000FF"),  # Dark blue
    pygame.Color("#3333FF"),  # Blue
    pygame.Color("#6666FF"),  # Light blue
    pygame.Color("#9999FF"),  # Very light blue
    pygame.Color("#CCCCCC"),  # Extremely light blue
]

# Define heatmap gradient colors
DEAD_COLOR = pygame.Color("#0000FF") # Blue
ALIVE_COLOR = pygame.Color("#FF0000") # Red
INTERACTION_COLOR = pygame.Color("#800080") # Purple
MAX_ACTIVITY_LEVEL = 10
MIN_ACTIVITY_LEVEL = -10

class PatersonsWormsSimulation:
    def __init__(self, grid_size=250, num_worms=5, frame_rate=30):
        self.grid_size = grid_size
        self.num_worms = num_worms
        self.frame_rate = frame_rate
        
        # Initialise the grid with all cells as alive (1) to start with
        self.grid = [[1 for _ in range(grid_size)] for _ in range(grid_size)]
        
        # Initialise the activity array to track the activity level for each cell
        self.activity = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        
        # Set initial worm positions to be in the center of the grid
        center_row, center_col = grid_size // 2, grid_size // 2
        self.worms = [(center_row, center_col) for _ in range(num_worms)]

    
    def initialise_screen(self):
        # Calculate window size based on screen resolution
        screen_info = pygame.display.Info()
        cell_size = min(screen_info.current_w // self.grid_size, int(0.8 * screen_info.current_h // self.grid_size))
        self.window_size = (self.grid_size * cell_size, self.grid_size * cell_size)
        self.cell_size = cell_size


    def move_worms(self):
        new_worms = []
        for worm in self.worms:
            col, row = worm
            
            # Toggle cell state and update cell activity level
            if DEBUG: print("Before toggle - Grid at ({}, {}) = {}".format(col, row, self.grid[row][col]))
            self.grid[row][col] = 1 - self.grid[row][col]
            self.activity[row][col] += 1
            if DEBUG: print("After toggle - Grid at ({}, {}) = {}".format(col, row, self.grid[row][col]))
            
            # Move the worm randomly in one of the neighboring cells (including diagonals)
            row += random.choice([-1, 0, 1])
            col += random.choice([-1, 0, 1])
            
            # Ensure the worm stays within the grid boundaries
            row = max(0, min(row, self.grid_size - 1))
            col = max(0, min(col, self.grid_size - 1))
            
            new_worms.append((col, row))
            
        if DEBUG: print("Updated worm positions: {}".format(new_worms))
        self.worms = new_worms
    
    
    def interpolate_color(self, factor):
        factor = max(-1, min(factor, 1))  # Limit factor between -1 and 1
        if factor < 0:  # Negative activity (switches to dead state 0)
            color_gradient = COLD_COLOR_GRADIENT
        else:  # Positive activity (switches to alive state 1)
            color_gradient = HOT_COLOR_GRADIENT

        index = int(abs(factor) * (len(color_gradient) - 1))
        index = max(0, min(index, len(color_gradient) - 2))
        start_color = color_gradient[index]
        end_color = color_gradient[index + 1]
        fraction = abs(factor) * (len(color_gradient) - 1) - index
        r = int(start_color.r + fraction * (end_color.r - start_color.r))
        g = int(start_color.g + fraction * (end_color.g - start_color.g))
        b = int(start_color.b + fraction * (end_color.b - start_color.b))
        return pygame.Color(r, g, b)

    
    def display_grid(self, window, cell_size):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                # Check if the cell is occupied by a worm
                if (col, row) in self.worms:
                    color = pygame.Color("green") 
                else:
                    # Determine the color based on the cell stand and activity level
                    cell_state = self.grid[row][col]
                    activity_level = self.activity[row][col]
                    if activity_level == 0: # Cell has not been toggled
                        color = pygame.Color("black")
                    else: # Cell has been toggled
                        if cell_state == 1: # Alive to Dead (cold colors)
                            color = self.interpolate_color(activity_level / MIN_ACTIVITY_LEVEL)
                        else: # Dead to Alive (hot colors)
                            color = self.interpolate_color(activity_level / MAX_ACTIVITY_LEVEL)
                
                # Draw the cell
                pygame.draw.rect(window, color, (col * cell_size, row * cell_size, cell_size, cell_size))

    
    def run_simulation(self):
        pygame.init()
        self.initialise_screen() # Dynamically calculate window size based on screen resolution
        window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Paterson's Worms Simulation")
        clock = pygame.time.Clock() # Create a clock to control the frame rate
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Move the worms
            self.move_worms()
            window.fill(pygame.Color("black"))
            self.display_grid(window, self.cell_size)
            pygame.display.flip() # Update the display
            clock.tick(60) # Limit the frame rate to 60 fps
        # Quit the game
        pygame.quit()