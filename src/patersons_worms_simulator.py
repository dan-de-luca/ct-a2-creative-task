import pygame
import random

# Constants:
# Debugging flag
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
    def __init__(self, grid_size=200, num_worms=5, frame_rate=30, triangular=True, track=False, track_num=10):
        self.grid_size = grid_size      # Size of the simulation grid (grid_size x grid_size)
        self.num_worms = num_worms      # Number of worms to simulate
        self.frame_rate = frame_rate    # Number of frames per second to run the simulation at
        self.triangular = triangular    # Whether or not to move the worms in a triangular pattern or standard pattern
        self.track = track             # Whether or not to keep track of recently visited cells
        self.track_num = track_num    # Number of recently visited cells to keep track of
        
        # Initialise the grid with all cells as alive (1) to start with
        self.grid = [[1 for _ in range(grid_size)] for _ in range(grid_size)]
        
        # Initialise the activity array to track the activity level for each cell
        self.activity = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        
        # Initial worm positions to be in the center of the grid
        center_row, center_col = grid_size // 2, grid_size // 2
        
        # Track current worm positions
        self.worms = [(center_row, center_col) for _ in range(num_worms)]
        
        # Next position options
        self.next_position_options = [(-2, 0), (2, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)]  # Up-Left, Down-Left, Left-Left, Right-Right, Up-Right, Down-Right
        
        # Track of recently visited cells
        self.last_visited = []

    
    def initialise_screen(self):
        # Calculate window size based on screen resolution
        screen_info = pygame.display.Info()
        cell_size = min(screen_info.current_w // self.grid_size, int(screen_info.current_h // self.grid_size))
        self.window_size = (self.grid_size * cell_size, self.grid_size * cell_size)
        self.cell_size = cell_size
        
    
    def get_next_pos(self, worm):
        # Get the current position of the worm
        row, col = worm
        # col, row = worm
        
        # Get the next position of the worm
        if self.track:
            # Get the next position
            next_position = random.choice(self.next_position_options)
            next_row = row + next_position[0]
            next_col = col + next_position[1]
            
            # Check if the new position is in the last visited list
            while (next_row, next_col) in self.last_visited:
                if DEBUG: print("Position taken. Finding new position...")
                next_position = random.choice(self.next_position_options)
                next_row = row + next_position[0]
                next_col = col + next_position[1]
            if DEBUG: print("Position found: ({}, {})".format(next_col, next_row))
            
            # Update the last visited list
            self.update_last_visited((next_col, next_row))
        else:
            # Get the next position regardless of recently visited cells
            next_position = random.choice(self.next_position_options)
            next_row = row + next_position[0]
            next_col = col + next_position[1]
        
        # Ensure the worm stays within the grid boundaries
        next_row = max(0, min(next_row, self.grid_size - 1))
        next_col = max(0, min(next_col, self.grid_size - 1))
        
        return (next_row, next_col)
    
        
    def update_last_visited(self, worm):
        # Update the last visited list
        row, col = worm
        self.last_visited.append((row, col))
        
        # track the last visited list
        if len(self.last_visited) > self.num_worms * self.track_num: self.last_visited.pop(-1)


    def move_worms(self):
        """
        If the triangular flag is set to False, the worms will move in a standard pattern. This means that the worms will
        move in a standard pattern, randomly moving up, down, left, right, or diagonally.
        
        If the track flag is set to True, the worms will avoid a set number of recently visited cells. This is done by keeping 
        track of the last visited cells in a list, and ensuring that the next position of the worm is not in this list.
        If the track flag is set to False, the worms will move randomly, regardless of recently visited cells.
        """
        new_worms = []
        for worm in self.worms:
            row, col = worm
            # col, row = worm
            
            # Toggle cell state and update cell activity level
            self.grid[row][col] = 1 - self.grid[row][col]
            self.activity[row][col] += 1
            
            if self.track:
                # Move the worm randomly in one of the neighboring cells (including diagonals)
                new_row = row + random.choice([-1, 0, 1])
                new_col = col + random.choice([-1, 0, 1])
                
                # Check if the new position is in the last visited list
                while (new_row, new_col) in self.last_visited:
                    if DEBUG: print("Position taken. Finding new position...")
                    new_row = row + random.choice([-1, 0, 1])
                    new_col = col + random.choice([-1, 0, 1])
                if DEBUG: print("Position found: ({}, {})".format(new_row, new_col))
                
                # Update the last visited list
                self.update_last_visited((new_row, new_col))
            else:
                # Move the worm randomly in one of the neighboring cells (including diagonals)
                new_row = row + random.choice([-1, 0, 1])
                new_col = col + random.choice([-1, 0, 1])
            
            # Ensure the worm stays within the grid boundaries
            new_row = max(0, min(new_row, self.grid_size - 1))
            new_col = max(0, min(new_col, self.grid_size - 1))
            
            # Add the new worm position to the list
            new_worms.append((row, col))
            
        if DEBUG: print("Updated worm positions: {}".format(new_worms))
        
        # Update the worm positions
        self.worms = new_worms
        
        
    def move_worms_triangular(self):
        """
        If the triangular flag is set to True, the worms will move in a triangular pattern. This means that the worms will
        move randomly in a triangular pattern, by randomly selecting a position from the next_position_options list. This 
        movement pattern is based on the isometric grid pattern simulated by Mike Paterson in 1969, which I have adapted
        to work with a standard grid. This adaptation is less elegant than simulations run on triangular grids, but it works 
        nonetheless.
        
        If the track flag is set to True, the worms will avoid a set number of recently visited cells. This is done by keeping 
        track of the last visited cells in a list, and ensuring that the next position of the worm is not in this list.
        If the track flag is set to False, the worms will move randomly, regardless of recently visited cells.
        
        """
        new_worms = []
        for worm in self.worms:
            row, col = worm
            # col, row = worm
            
            # Toggle cell state and update cell activity level
            self.grid[row][col] = 1 - self.grid[row][col]
            self.activity[row][col] += 1
            
            # Get the next position of the worm
            next_pos = self.get_next_pos(worm)
            row, col = next_pos
            
            # Add the new worm position to the list
            new_worms.append((row, col))
            
        if DEBUG: print("Updated worm positions: {}".format(new_worms))
        
        # Update the worm positions
        self.worms = new_worms
    
    
    def interpolate_color(self, factor):
        """
        Function to interpolate between two colors based on the activity factor of a cell.
        Color gradient is defined by the HOT_COLOR_GRADIENT and COLD_COLOR_GRADIENT lists.
        Used to generate a heatmap of the activity levels of the grid cells.
        """
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
        # Display the simulation grid
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                # Check if the cell is occupied by a worm
                if (row, col) in self.worms:
                    color = pygame.Color("green") 
                else:
                    # Determine the cell color based on the cell state (1 or 0) and activity level (-10 to 10)
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
        # Initialise the pygame window (starts the simulator)
        pygame.init()
        
        # Dynamically calculate window size based on screen resolution
        self.initialise_screen()
        window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Paterson's Worms Simulation")
        
        # Create a clock to control the frame rate
        clock = pygame.time.Clock()
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Move the worms
            if self.triangular: self.move_worms_triangular()
            else: self.move_worms()
            
            # Draw the grid
            window.fill(pygame.Color("black"))
            self.display_grid(window, self.cell_size)
            
            # Update the display based on the frame rate
            pygame.display.flip()
            clock.tick(self.frame_rate)
        
        # Quit the game
        pygame.quit()