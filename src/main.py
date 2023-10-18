import sys
import pygame as pg
# import pygame_menu as pm

# Import classes
from button import Button
from patersons_worms_simulator import PatersonsWormsSimulation

pg.init()

# Constants
DEBUG = False
FONT = pg.font.SysFont("arialblack", 30)
WHITE = pg.Color("#FFFFFF")
GRAY = pg.Color("#CCCCCC")
BLACK = pg.Color("#000000")
PASTEL_BLUE = pg.Color("#B2DCEF")


class Menu:
    """
    Menu class to store menu attributes
    """
    def __init__(self):
        # Menu attributes
        self.screen_info = pg.display.Info()
        self.screen_height = int(self.screen_info.current_h * 0.75)
        self.menu_window = pg.display.set_mode((self.screen_height, self.screen_height))
        self.frame_rate = 60 # Default frame rate
        self.text = "About Paterson's Worms"
        
        # Dynamic Button Sizes:
        # Main Menu Buttons
        self.button_width_main = int(0.24 * self.screen_height)
        self.button_height_main = int(0.06 * self.screen_height)
        # Options Buttons
        # Single Digit
        self.button_width_options_s = int(0.06 * self.screen_height)
        self.button_height_options_s = int(0.06 * self.screen_height)
        # Double Digit
        self.button_width_options_d = int(0.07 * self.screen_height)
        self.button_height_options_d = int(0.06 * self.screen_height)
        # Triple Digit
        self.button_width_options_t = int(0.08 * self.screen_height)
        self.button_height_options_t = int(0.06 * self.screen_height)
        # Worm Buttons
        self.worm_height_1 = int(0.45 * self.screen_height)
        self.worm_width_1 = int(0.15 * self.screen_height)
        self.worm_height_2 = int(0.2 * self.screen_height)
        self.worm_width_2 = int(0.05 * self.screen_height)
    
    def set_text(self, text):
        self.text = text
    
    def concat_text(self, text):
        self.text += text


def draw_text(window, text, color, position):
    """
    Render the given text to the menu screen
    """
    text_surface = FONT.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    window.blit(text_surface, text_rect)


def main():
    menu = Menu()
    
    # Game variables
    menu_state = "main"
    game_running = False
    
    pg.display.set_caption("Start Menu")
    
    # Load main menu button images
    start_image = pg.image.load("assets/start-button.png").convert_alpha()
    exit_image = pg.image.load("assets/exit-button.png").convert_alpha()
    options_image = pg.image.load("assets/options-button.png").convert_alpha()
    about_image = pg.image.load("assets/about-button.png").convert_alpha()
    
    # Load sub-menu button images
    back_image = pg.image.load("assets/back-button.png").convert_alpha()
    fps_image = pg.image.load("assets/fps-button.png").convert_alpha()
    grid_image = pg.image.load("assets/grid-button.png").convert_alpha()
    pattern_image = pg.image.load("assets/pattern-button.png").convert_alpha()
    track_image = pg.image.load("assets/track-button.png").convert_alpha()
    worms_image = pg.image.load("assets/worms-button.png").convert_alpha()
    
    # Load options button images
    # FPS options
    fps_30 = pg.image.load("assets/30-fps.png").convert_alpha()
    fps_60 = pg.image.load("assets/60-fps.png").convert_alpha()
    fps_90 = pg.image.load("assets/90-fps.png").convert_alpha()
    fps_120 = pg.image.load("assets/120-fps.png").convert_alpha()
    
    # Grid options
    grid_100 = pg.image.load("assets/100-grid.png").convert_alpha()
    grid_200 = pg.image.load("assets/200-grid.png").convert_alpha()
    grid_300 = pg.image.load("assets/300-grid.png").convert_alpha()
    grid_400 = pg.image.load("assets/400-grid.png").convert_alpha()
    grid_500 = pg.image.load("assets/500-grid.png").convert_alpha()
    
    # Pattern options
    triangle_pattern = pg.image.load("assets/triangle-pattern-button.png").convert_alpha()
    square_pattern = pg.image.load("assets/square-pattern-button.png").convert_alpha()
    
    # Track options
    track_10 = pg.image.load("assets/track-10.png").convert_alpha()
    track_25 = pg.image.load("assets/track-25.png").convert_alpha()
    track_50 = pg.image.load("assets/track-50.png").convert_alpha()
    
    # Worms options
    worms_1 = pg.image.load("assets/1-worm.png").convert_alpha()
    worms_3 = pg.image.load("assets/3-worms.png").convert_alpha()
    worms_5 = pg.image.load("assets/5-worms.png").convert_alpha()
    worms_10 = pg.image.load("assets/10-worms.png").convert_alpha()
    
    # Load worm image
    worm_1 = pg.image.load("assets/worm-v3.png").convert_alpha()
    worm_2 = pg.image.load("assets/worm-v4.png").convert_alpha()
    
    # Resize main menu button images
    start_image = pg.transform.scale(start_image, (menu.button_width_main, menu.button_height_main))
    exit_image = pg.transform.scale(exit_image, (menu.button_width_main, menu.button_height_main))
    options_image = pg.transform.scale(options_image, (menu.button_width_main, menu.button_height_main))
    about_image = pg.transform.scale(about_image, (menu.button_width_main, menu.button_height_main))
    
    # Resize sub-menu button images
    back_image = pg.transform.scale(back_image, (menu.button_width_main, menu.button_height_main))
    fps_image = pg.transform.scale(fps_image, (menu.button_width_main, menu.button_height_main))
    grid_image = pg.transform.scale(grid_image, (menu.button_width_main, menu.button_height_main))
    pattern_image = pg.transform.scale(pattern_image, (menu.button_width_main, menu.button_height_main))
    track_image = pg.transform.scale(track_image, (menu.button_width_main, menu.button_height_main))
    worms_image = pg.transform.scale(worms_image, (menu.button_width_main, menu.button_height_main))
    
    # Resize options buttons images
    # FPS options
    fps_30 = pg.transform.scale(fps_30, (menu.button_width_options_d, menu.button_height_options_d))
    fps_60 = pg.transform.scale(fps_60, (menu.button_width_options_d, menu.button_height_options_d))
    fps_90 = pg.transform.scale(fps_90, (menu.button_width_options_d, menu.button_height_options_d))
    fps_120 = pg.transform.scale(fps_120, (menu.button_width_options_t, menu.button_height_options_t))
    
    # Grid options
    grid_100 = pg.transform.scale(grid_100, (menu.button_width_options_t, menu.button_height_options_t))
    grid_200 = pg.transform.scale(grid_200, (menu.button_width_options_t, menu.button_height_options_t))
    grid_300 = pg.transform.scale(grid_300, (menu.button_width_options_t, menu.button_height_options_t))
    grid_400 = pg.transform.scale(grid_400, (menu.button_width_options_t, menu.button_height_options_t))
    grid_500 = pg.transform.scale(grid_500, (menu.button_width_options_t, menu.button_height_options_t))
    
    # Pattern options
    triangle_pattern = pg.transform.scale(triangle_pattern, (menu.button_width_main, menu.button_height_main))
    square_pattern = pg.transform.scale(square_pattern, (menu.button_width_main, menu.button_height_main))
    
    # Track options
    track_10 = pg.transform.scale(track_10, (menu.button_width_options_s, menu.button_height_options_s))
    track_25 = pg.transform.scale(track_25, (menu.button_width_options_s, menu.button_height_options_s))
    track_50 = pg.transform.scale(track_50, (menu.button_width_options_s, menu.button_height_options_s))
    
    # Worms options
    worms_1 = pg.transform.scale(worms_1, (menu.button_width_options_s, menu.button_height_options_s))
    worms_3 = pg.transform.scale(worms_3, (menu.button_width_options_s, menu.button_height_options_s))
    worms_5 = pg.transform.scale(worms_5, (menu.button_width_options_s, menu.button_height_options_s))
    worms_10 = pg.transform.scale(worms_10, (menu.button_width_options_d, menu.button_height_options_d))
    
    # Resize worm image
    worm_1 = pg.transform.scale(worm_1, (menu.worm_height_1, menu.worm_width_1))
    worm_2 = pg.transform.scale(worm_2, (menu.worm_height_2, menu.worm_width_2))
    
    
    # X Positions:
    center_x = menu.screen_height // 2
    main_button_mid_x = (center_x - (menu.button_width_main // 2))
    option_button_d_mid_x = (center_x - (menu.button_width_options_d // 2))
    
    # Main Button Positions:
    pos_1 = (main_button_mid_x, (main_button_mid_x - main_button_mid_x * 0.4))                  # Top-Center
    pos_2 = (main_button_mid_x, (main_button_mid_x - main_button_mid_x * 0.2))                  # Upper-Center
    pos_3 = (main_button_mid_x, main_button_mid_x)                                              # Middle-Center
    pos_4 = (main_button_mid_x, (main_button_mid_x + main_button_mid_x * 0.2))                  # Lower-Center
    pos_5 = (main_button_mid_x, (main_button_mid_x + main_button_mid_x * 0.4))                  # Lower-Center
    pos_6 = (main_button_mid_x, (main_button_mid_x + main_button_mid_x * 0.6))                  # Lower-Center
    
    # Options Button Positions:
    pos_7 = (option_button_d_mid_x, (option_button_d_mid_x - option_button_d_mid_x * 0.2))      # Upper-Center
    pos_8 = (option_button_d_mid_x, option_button_d_mid_x)                                      # Middle-Center
    pos_9 = (option_button_d_mid_x, (option_button_d_mid_x + option_button_d_mid_x * 0.2))      # Lower-Center
    pos_10 = (option_button_d_mid_x, (option_button_d_mid_x + option_button_d_mid_x * 0.4))      # Lower-Center
    pos_11 = (option_button_d_mid_x, (option_button_d_mid_x + option_button_d_mid_x * 0.6))      # Bottom-Center
    
    
    # Main Menu Buttons:
    options_p = pos_1 
    start_p = pos_2
    about_p = pos_3
    exit_p = pos_4
    
    # Sub-menu Buttons:
    back_p = pos_1
    fps_p = pos_2       
    grid_p = pos_3
    pattern_p = pos_4
    track_p = pos_5
    worms_p = pos_6
    
    # Options Buttons:
    # FPS Options:
    fps_30_p = pos_7
    fps_60_p = pos_8
    fps_90_p = pos_9
    fps_120_p = pos_10
    
    # Grid Options:
    grid_100_p = pos_7
    grid_200_p = pos_8
    grid_300_p = pos_9
    grid_400_p = pos_10
    grid_500_p = pos_11
    
    # Pattern Options:
    triangle_pattern_p = pos_3
    square_pattern_p = pos_4
    
    # Track Options:
    track_10_p = pos_7
    track_25_p = pos_8
    track_50_p = pos_9
    
    # Worms Options:
    worms_1_p = pos_7
    worms_3_p = pos_8
    worms_5_p = pos_9
    worms_10_p = pos_10

    # Worm Position
    worm_x = ((menu.screen_height // 2) - (menu.worm_height_2 // 2))
    worm_p_1 = (worm_x, (worm_x - worm_x * 0.8))
    
    # Create Button Instances
    # Main Menu Buttons:
    options_button = Button(menu, options_p, options_image, "menu")
    start_button = Button(menu, start_p, start_image, "start")
    exit_button = Button(menu, exit_p, exit_image, "exit")
    about_button = Button(menu, about_p, about_image, "about")
    
    # Sub-menu Buttons:
    fps_button = Button(menu, fps_p, fps_image, "fps")
    grid_button = Button(menu, grid_p, grid_image, "grid")
    pattern_button = Button(menu, pattern_p, pattern_image, "pattern")
    track_button = Button(menu, track_p, track_image, "track")
    worms_button = Button(menu, worms_p, worms_image, "worms")
    back_button = Button(menu, back_p, back_image, "back")
    
    # Options Buttons:
    # FPS Options:
    fps_30_button = Button(menu, fps_30_p, fps_30, "fps_30")
    fps_60_button = Button(menu, fps_60_p, fps_60, "fps_60")
    fps_90_button = Button(menu, fps_90_p, fps_90, "fps_90")
    fps_120_button = Button(menu, fps_120_p, fps_120, "fps_120")
    
    # Grid Options:
    grid_100_button = Button(menu, grid_100_p, grid_100, "grid_100")
    grid_200_button = Button(menu, grid_200_p, grid_200, "grid_200")
    grid_300_button = Button(menu, grid_300_p, grid_300, "grid_300")
    grid_400_button = Button(menu, grid_400_p, grid_400, "grid_400")
    grid_500_button = Button(menu, grid_500_p, grid_500, "grid_500")
    
    # Pattern Options:
    triangle_pattern_button = Button(menu, triangle_pattern_p, triangle_pattern, "triangle_pattern")
    square_pattern_button = Button(menu, square_pattern_p, square_pattern, "square_pattern")
    
    # Track Options:
    track_10_button = Button(menu, track_10_p, track_10, "track_10")
    track_25_button = Button(menu, track_25_p, track_25, "track_25")
    track_50_button = Button(menu, track_50_p, track_50, "track_50")
    
    # Worms Options:
    worms_1_button = Button(menu, worms_1_p, worms_1, "worms_1")
    worms_3_button = Button(menu, worms_3_p, worms_3, "worms_3")
    worms_5_button = Button(menu, worms_5_p, worms_5, "worms_5")
    worms_10_button = Button(menu, worms_10_p, worms_10, "worms_10")
    
    # Worm Button:
    worm_button_1 = Button(menu, worm_p_1, worm_1, "worm_1")
    worm_button_2 = Button(menu, worm_p_1, worm_2, "worm_2")
    
    
    # Initialise Simulation Defaults
    frame_rate = 60
    grid_size = 200
    triangle_pattern = True
    track_recent = True
    num_track = 10
    num_worms = 5

    running = True
    while running:
        # Start menu
        menu.menu_window.fill(PASTEL_BLUE)
        
        # Display Main Menu
        if game_running == False:
            # Main Menu Buttons:
            if menu_state == "main":
                if start_button.draw():
                    print("Start button pressed. Starting simulation...")
                    print("Grid size: {}, Num worms: {}, Frame rate: {}".format(grid_size, num_worms, frame_rate))
                    sim = PatersonsWormsSimulation(grid_size, num_worms, frame_rate, triangle_pattern, track_recent, num_track)
                    sim.run_simulation()
                
                elif exit_button.draw():
                    print("Exit button pressed. Thanks for coming!")
                    running = False
                
                elif options_button.draw():
                    if DEBUG: print("Options button pressed. Opening options menu...")
                    menu_state = "sub"
                
                elif about_button.draw():
                    if DEBUG: print("About button pressed. Opening about menu...")
                    menu_state = "about"
                
                elif worm_button_2.draw():
                    print("Paterson's Worm Says Hi!")
            
            # Sub-menu Buttons:
            elif menu_state == "sub":
                if back_button.draw():
                    if DEBUG: print("Back button pressed!")
                    menu_state = "main"
                
                elif fps_button.draw():
                    if DEBUG: print("FPS button pressed!")
                    menu_state = "options-fps"
                
                elif grid_button.draw():
                    if DEBUG: print("Grid button pressed!")
                    menu_state = "options-grid"
                
                elif worms_button.draw():
                    if DEBUG: print("Worms button pressed!")
                    menu_state = "options-worms"
                
                elif worm_button_2.draw():
                    print("Paterson's Worm Says Hi!")

                elif pattern_button.draw():
                    if DEBUG: print("Pattern button pressed!")
                    menu_state = "options-pattern"
                    
                elif track_button.draw():
                    if DEBUG: print("Track button pressed!")
                    menu_state = "options-track"
            
            # Options Buttons:
            # FPS Options Buttons
            elif menu_state == "options-fps":
                if fps_30_button.draw():
                    if DEBUG: print("30 FPS button pressed!")
                    frame_rate = 30
                
                elif fps_60_button.draw():
                    if DEBUG: print("60 FPS button pressed!")
                    frame_rate = 60
                
                elif fps_90_button.draw():
                    if DEBUG: print("90 FPS button pressed!")
                    frame_rate = 90
                
                elif fps_120_button.draw():
                    if DEBUG: print("120 FPS button pressed!")
                    frame_rate = 120
                
                elif back_button.draw():
                    if DEBUG: print("Back button pressed!")
                    menu_state = "sub"
                
                elif worm_button_2.draw():
                    print("Paterson's Worm Says Hi!")
            
            # Grid Options Buttons
            elif menu_state == "options-grid":
                if grid_100_button.draw():
                    if DEBUG: print("100 grid button pressed!")
                    grid_size = 100
                
                elif grid_200_button.draw():
                    if DEBUG: print("200 grid button pressed!")
                    grid_size = 200
                
                elif grid_300_button.draw():
                    if DEBUG: print("300 grid button pressed!")
                    grid_size = 300
                
                elif grid_400_button.draw():
                    if DEBUG: print("400 grid button pressed!")
                    grid_size = 400
                
                elif grid_500_button.draw():
                    if DEBUG: print("500 grid button pressed!")
                    grid_size = 500
                
                elif back_button.draw():
                    if DEBUG: print("Back button pressed!")
                    menu_state = "sub"
                
                elif worm_button_2.draw():
                    print("Paterson's Worm Says Hi!")
            
            # Movement Pattern Options Buttons
            elif menu_state == "options-pattern":
                if triangle_pattern_button.draw():
                    if DEBUG: print("1 worm button pressed!")
                    triangle_pattern = True
                
                elif square_pattern_button.draw():
                    if DEBUG: print("3 worms button pressed!")
                    triangle_pattern = False
                
                elif back_button.draw():
                    if DEBUG: print("Back button pressed!")
                    menu_state = "sub"
                
                elif worm_button_2.draw():
                    print("Paterson's Worm Says Hi!")
            
            # Track Movements Options Buttons
            elif menu_state == "options-track":
                if track_10_button.draw():
                    if DEBUG: print("1 worm button pressed!")
                    track_recent = True
                    num_track = 10
                
                elif track_25_button.draw():
                    if DEBUG: print("3 worms button pressed!")
                    track_recent = True
                    num_track = 25
                
                elif track_50_button.draw():
                    if DEBUG: print("5 worms button pressed!")
                    track_recent = True
                    num_track = 50
            
                elif back_button.draw():
                    if DEBUG: print("Back button pressed!")
                    menu_state = "sub"
                
                elif worm_button_2.draw():
                    print("Paterson's Worm Says Hi!")
            
            # Worms Options Buttons
            elif menu_state == "options-worms":
                if worms_1_button.draw():
                    print("1 worm button pressed!")
                    num_worms = 1
                
                elif worms_3_button.draw():
                    print("3 worms button pressed!")
                    num_worms = 3
                
                elif worms_5_button.draw():
                    print("5 worms button pressed!")
                    num_worms = 5
                
                elif worms_10_button.draw():
                    print("10 worms button pressed!")
                    num_worms = 10
                
                elif back_button.draw():
                    print("Back button pressed!")
                    menu_state = "sub"
                
                elif worm_button_2.draw():
                    print("Paterson's Worm Says Hi!")
            
            # About menu buttons
            elif menu_state == "about":
                if back_button.draw():
                    print("Back button pressed!")
                    menu_state = "main"
                
                elif worm_button_2.draw():
                    print("Paterson's Worm Says Hi!")
                
                else:
                    # Display text on screen
                    draw_text(menu.menu_window, menu.text, BLACK, (menu.screen_height // 2, menu.screen_height // 2))
        
        # Event handler
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game_running = False
            
            if event.type == pg.QUIT:
                running = False
        
        # Limit menu frame rate
        pg.time.delay(menu.frame_rate)
        
        # Update the menu display
        pg.display.flip()

    # Quit the game
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
