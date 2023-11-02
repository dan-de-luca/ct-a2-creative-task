import sys
import os
import pygame as pg
from functools import partial
# import pygame_menu as pm

# Import classes
from button import Button
from patersons_worms_simulator import PatersonsWormsSimulation

pg.init()

# Constants
DEBUG = False
HEADING_FONT_SIZE = 30
NORMAL_FONT_SIZE = 20
HEADING_FONT = pg.font.SysFont("arialblack", HEADING_FONT_SIZE)
NORMAL_FONT = pg.font.SysFont("arialblack", NORMAL_FONT_SIZE)
WHITE = pg.Color("#FFFFFF")
GRAY = pg.Color("#CCCCCC")
BLACK = pg.Color("#000000")
PASTEL_BLUE = pg.Color("#B2DCEF")
DARK_BLUE = pg.Color("#0000A0")


#######################################################################################################################
class Menu:
    """
    Menu class to store menu attributes
    """
    def __init__(self):
        # Menu Attributes
        self.screen_info = pg.display.Info()
        self.screen_height = int(self.screen_info.current_h * 0.75)
        self.menu_window = pg.display.set_mode((self.screen_height, self.screen_height))
        self.window_center = (self.screen_height // 2, self.screen_height // 2)
        self.frame_rate = 60 # Default frame rate
        self.about_text_file_path = os.path.join('assets', 'about.txt')
        self.about_text = self.load_text()
        # self.about_text_length = len(self.about_text)
        # self.about_text_box_max_y = self.window_center[1] // 2
        # self.about_text_box_min_y = self.about_text_box_max_y + self.window_center[1]
        
        # Add any additional attributes here
        
        # Dynamic Button Sizes:
        # Main Menu Button Size
        self.button_width_main = int(0.24 * self.screen_height)
        self.button_height_main = int(0.06 * self.screen_height)
        # Options Buttons
        # Single Digit Button Size
        self.button_width_options_s = int(0.06 * self.screen_height)
        self.button_height_options_s = int(0.06 * self.screen_height)
        # Double Digit Button Size
        self.button_width_options_d = int(0.07 * self.screen_height)
        self.button_height_options_d = int(0.06 * self.screen_height)
        # Triple Digit Button Size
        self.button_width_options_t = int(0.08 * self.screen_height)
        self.button_height_options_t = int(0.06 * self.screen_height)
        # Worm Button Sizes (worm images - 2 versions)
        self.worm_height_1 = int(0.45 * self.screen_height)
        self.worm_width_1 = int(0.15 * self.screen_height)
        self.worm_height_2 = int(0.2 * self.screen_height)
        self.worm_width_2 = int(0.05 * self.screen_height)
    
    # def get_about_text_height(self):
    #     return sum(item[1].get_height() + 10 for item in self.about_text)

    def draw_text(self, y_position, scroll_y):
        """
        Render the given text to the menu screen with scrolling
        """
        # Calculate total text height
        scroll_box_height = self.screen_height // 2
        total_text_height = len(self.about_text) * (NORMAL_FONT.size("a")[1] + 10)
        
        # Implement scrolling logic within the text area
        if total_text_height > scroll_box_height:
            if scroll_y > 0:
                scroll_y = 0
            elif scroll_y < -(total_text_height - scroll_box_height):
                scroll_y = -(total_text_height - scroll_box_height)
        else:
            scroll_y = 0 # If the total text height doesn't exceed the window height, no scrolling necessary
        
        rendered_text_height = 0
        for text_surface in self.about_text:
            text_rect = text_surface.get_rect(center=(scroll_box_height, y_position + scroll_y))
            if 0 <= text_rect.centery < scroll_box_height:
                self.menu_window.blit(text_surface, text_rect)
                rendered_text_height += text_rect.height + 10
                y_position += text_rect.height + 10 # Adjust vertical (line) spacing
            else:
                break # Stop rendering if text is outside the scrolling area
        
        return scroll_y
    
    
    def load_file(self, file_path):
        """
        Load file from file path
        """
        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                file_contents = file.read()
                if DEBUG: print("File read successfully!")
        except FileNotFoundError:
            print(f"ERROR: File '{file_path}' not found!")
        
        return file_contents
    
    
    def wrap_text(self, text):
        """
        Wrap text to the given max line length
        """
        avg_char_width = NORMAL_FONT.size("a")[0]
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        for word in words:
            if (((current_length + len(word) + 1) * avg_char_width ) <= (self.window_center[0])):
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)
        lines.append(" ".join(current_line))
        
        return lines
    
    
    def load_text(self):
        """
        Load formatted text ready to be rendered to the screen
        """
        file_contents = self.load_file(self.about_text_file_path)
        wrapped_lines = self.wrap_text(file_contents)
        text_list = []
        
        for line in wrapped_lines:
            line = line.strip()
            if line.startswith("# "): # Check for headings
                text_surface = HEADING_FONT.render(line[2:], True, DARK_BLUE)
                text_list.append(text_surface)
            else:
                text_surface = NORMAL_FONT.render(line, True, BLACK)
                text_list.append(text_surface)
        
        return text_list
    
    
    def load_image(self, file_path):
        """
        Load image from file
        """
        try:
            image = pg.image.load(file_path).convert_alpha()
        except FileNotFoundError:
            print(f"ERROR: File '{file_path}' not found!")
        return image


#######################################################################################################################

def handle_button_click(buttons, click_position):
    for button in buttons.items():
        button_rect = button[1].image_rect
        if button_rect.collidepoint(click_position):
            button[1].action()
            # return button.text()
    
    # # Return None if no button was clicked
    # return None
    # pass


#######################################################################################################################
# Menu Functions

def start_game(simulation_settings):
    print("Starting simulation...")
    print("Grid size: {}, Num worms: {}, Frame rate: {}".format(simulation_settings.get("grid_size"), simulation_settings.get("num_worms"), simulation_settings.get("frame_rate")))
    sim = PatersonsWormsSimulation(
        simulation_settings.get("grid_size"), 
        simulation_settings.get("num_worms"), 
        simulation_settings.get("frame_rate"), 
        simulation_settings.get("triangle_pattern"), 
        simulation_settings.get("track_recent"), 
        simulation_settings.get("num_track")
        )
    sim.run_simulation()
    # pass

def worm_says_hi():
    print("Paterson's Worm Says Hi!")
    # pass


#######################################################################################################################
# Game / Menu Loop
def main():
    # Menu instance
    menu = Menu()
    # scroll_y = menu.window_center[1] - (menu.window_center[1] // 2)
    scroll_y = 0
    pg.display.set_caption("Start Menu")
    
    
    # Button Positions:
    
    # X Positions:
    center_x = menu.screen_height // 2
    main_button_mid_x = (center_x - (menu.button_width_main // 2))
    option_button_d_mid_x = (center_x - (menu.button_width_options_d // 2))
    
    # Main Button Positions:
    worm_pos = (main_button_mid_x, (main_button_mid_x - main_button_mid_x * 0.6)) # Top-Top-Center
    pos_1 = (main_button_mid_x, (main_button_mid_x - main_button_mid_x * 0.4)) # Top-Center
    pos_2 = (main_button_mid_x, (main_button_mid_x - main_button_mid_x * 0.2)) # Upper-Center
    pos_3 = (main_button_mid_x, main_button_mid_x) # Middle-Center
    pos_4 = (main_button_mid_x, (main_button_mid_x + main_button_mid_x * 0.2)) # Lower-Center
    pos_5 = (main_button_mid_x, (main_button_mid_x + main_button_mid_x * 0.4)) # Lower-Center
    pos_6 = (main_button_mid_x, (main_button_mid_x + main_button_mid_x * 0.6)) # Lower-Center
    
    # Options Button Positions:
    pos_7 = (option_button_d_mid_x, (option_button_d_mid_x - option_button_d_mid_x * 0.2)) # Upper-Center
    pos_8 = (option_button_d_mid_x, option_button_d_mid_x) # Middle-Center
    pos_9 = (option_button_d_mid_x, (option_button_d_mid_x + option_button_d_mid_x * 0.2)) # Lower-Center
    pos_10 = (option_button_d_mid_x, (option_button_d_mid_x + option_button_d_mid_x * 0.4)) # Lower-Center
    pos_11 = (option_button_d_mid_x, (option_button_d_mid_x + option_button_d_mid_x * 0.6)) # Bottom-Center
    
    
    # Initialise Simulation Defaults:
    simulation_settings = {
        "menu_state": "main",
        "game_running": False,
        "menu_running": True,
        "frame_rate": 60,
        "grid_size": 200,
        "triangle_pattern": True,
        "track_recent": True,
        "num_track": 10,
        "num_worms": 5
    }
    # default_frame_rate = 60
    # default_grid_size = 200
    # default_triangle_pattern = True
    # default_track_recent = True
    # default_num_track = 10
    # default_num_worms = 5
    
    
    # Define Button Functions:
    
    # Partial functions with pre-defined arguments
    start_game_partial = partial(start_game, simulation_settings)
    worm_greeting_partial = partial(worm_says_hi)
    
    # Functions to update game variables
    update_menu_state = lambda state: simulation_settings.update({"menu_state": state})
    exit_game = lambda state: simulation_settings.update({"game_running": state}) # TODO: Implement functionality
    exit_menu = lambda state: simulation_settings.update({"menu_running": state})
    
    # Functions to update simulation default variables
    update_frame_rate = lambda rate: simulation_settings.update({"frame_rate": rate})
    update_grid_size = lambda size: simulation_settings.update({"grid_size": size})
    update_triangle_pattern = lambda pattern: simulation_settings.update({"triangle_pattern": pattern})
    update_track_recent = lambda track: simulation_settings.update({"track_recent": track})
    update_num_track = lambda num: simulation_settings.update({"num_track": num})
    update_num_worms = lambda num: simulation_settings.update({"num_worms": num})
    
    
    # Define Buttons:
    
    # Main Menu Buttons:
    start_button = Button(menu, pos_2, "assets/start-button.png", menu.button_width_main, menu.button_height_main, "start", start_game_partial)
    exit_button = Button(menu, pos_4, "assets/exit-button.png", menu.button_width_main, menu.button_height_main, "exit", lambda: exit_menu(False))
    options_button = Button(menu, pos_1, "assets/options-button.png", menu.button_width_main, menu.button_height_main, "options", lambda: update_menu_state("sub"))
    about_button = Button(menu, pos_3, "assets/about-button.png", menu.button_width_main, menu.button_height_main, "about", lambda: update_menu_state("about"))
    worm_button = Button(menu, worm_pos, "assets/worm-v4.png", menu.worm_width_2, menu.worm_height_2, "worm_greeting", worm_greeting_partial)
    
    # Sub-Menu Buttons:
    main_back_button = Button(menu, pos_1, "assets/back-button.png", menu.button_width_main, menu.button_height_main, "back", lambda: update_menu_state("main"))
    fps_button = Button(menu, pos_2, "assets/fps-button.png", menu.button_width_main, menu.button_height_main, "fps", lambda: update_menu_state("options-fps"))
    grid_button = Button(menu, pos_3, "assets/grid-button.png", menu.button_width_main, menu.button_height_main, "grid", lambda: update_menu_state("options-grid"))
    worms_button = Button(menu, pos_6, "assets/worms-button.png", menu.button_width_main, menu.button_height_main, "worms", lambda: update_menu_state("options-worms"))
    pattern_button = Button(menu, pos_4, "assets/pattern-button.png", menu.button_width_main, menu.button_height_main, "pattern", lambda: update_menu_state("options-pattern"))
    track_button = Button(menu, pos_5, "assets/track-button.png", menu.button_width_main, menu.button_height_main, "track", lambda: update_menu_state("options-track"))
    
    # Options Menu Buttons:
    # Shared Back Button
    sub_back_button = Button(menu, pos_1, "assets/back-button.png", menu.button_width_main, menu.button_height_main, "back", lambda: update_menu_state("sub"))
    
    # FPS Options Buttons
    fps_30_button = Button(menu, pos_7, "assets/30-fps.png", menu.button_width_options_d, menu.button_height_options_d, "fps_30", lambda: update_frame_rate(30))
    fps_60_button = Button(menu, pos_8, "assets/60-fps.png", menu.button_width_options_d, menu.button_height_options_d, "fps_60", lambda: update_frame_rate(60))
    fps_90_button = Button(menu, pos_9, "assets/90-fps.png", menu.button_width_options_d, menu.button_height_options_d, "fps_90", lambda: update_frame_rate(90))
    fps_120_button = Button(menu, pos_10, "assets/120-fps.png", menu.button_width_options_t, menu.button_height_options_t, "fps_120", lambda: update_frame_rate(120))
    
    # Grid Options Buttons
    grid_100_button = Button(menu, pos_7, "assets/100-grid.png", menu.button_width_options_t, menu.button_height_options_t, "grid_100", lambda: update_grid_size(100))
    grid_200_button = Button(menu, pos_8, "assets/200-grid.png", menu.button_width_options_t, menu.button_height_options_t, "grid_200", lambda: update_grid_size(200))
    grid_300_button = Button(menu, pos_9, "assets/300-grid.png", menu.button_width_options_t, menu.button_height_options_t, "grid_300", lambda: update_grid_size(300))
    grid_400_button = Button(menu, pos_10, "assets/400-grid.png", menu.button_width_options_t, menu.button_height_options_t, "grid_400", lambda: update_grid_size(400))
    grid_500_button = Button(menu, pos_11, "assets/500-grid.png", menu.button_width_options_t, menu.button_height_options_t, "grid_500", lambda: update_grid_size(500))
    
    # Movement Pattern Options Buttons
    triangle_pattern_button = Button(menu, pos_3, "assets/triangle-pattern-button.png", menu.button_width_main, menu.button_height_main, "triangle_pattern", lambda: update_triangle_pattern(True))
    square_pattern_button = Button(menu, pos_4, "assets/square-pattern-button.png", menu.button_width_main, menu.button_height_main, "square_pattern", lambda: update_triangle_pattern(False))
    
    # Track Movements Options Buttons
    track_10_button = Button(menu, pos_7, "assets/track-10.png", menu.button_width_options_s, menu.button_height_options_s, "track_10", lambda: update_track_recent(True) and update_num_track(10))
    track_25_button = Button(menu, pos_8, "assets/track-25.png", menu.button_width_options_s, menu.button_height_options_s, "track_25", lambda: update_track_recent(True) and update_num_track(25))
    track_50_button = Button(menu, pos_9, "assets/track-50.png", menu.button_width_options_s, menu.button_height_options_s, "track_50", lambda: update_track_recent(True) and update_num_track(50))
    
    # Worms Options Buttons
    worms_1_button = Button(menu, pos_7, "assets/1-worm.png", menu.button_width_options_s, menu.button_height_options_s, "worms_1", lambda: update_num_worms(1))
    worms_3_button = Button(menu, pos_8, "assets/3-worms.png", menu.button_width_options_s, menu.button_height_options_s, "worms_3", lambda: update_num_worms(3))
    worms_5_button = Button(menu, pos_9, "assets/5-worms.png", menu.button_width_options_s, menu.button_height_options_s, "worms_5", lambda: update_num_worms(5))
    worms_10_button = Button(menu, pos_10, "assets/10-worms.png", menu.button_width_options_d, menu.button_height_options_d, "worms_10", lambda: update_num_worms(10))
    
    
    # Create Button Dictionaries:
    main_menu_buttons = {
        "start_button": start_button,
        "exit_button": exit_button,
        "options_button": options_button,
        "about_button": about_button,
        "worm_button": worm_button
    }
    
    sub_menu_buttons = {
        "back_button": main_back_button,
        "fps_button": fps_button,
        "grid_button": grid_button,
        "worms_button": worms_button,
        "pattern_button": pattern_button,
        "track_button": track_button,
        "worm_button": worm_button
    }
    
    about_section_buttons = {
        "back_button": main_back_button,
        "worm_button": worm_button
    }
    
    fps_options_menu_buttons = {
        "back_button": sub_back_button,
        "fps_30_button": fps_30_button,
        "fps_60_button": fps_60_button,
        "fps_90_button": fps_90_button,
        "fps_120_button": fps_120_button,
        "worm_button": worm_button
    }
    
    grid_options_menu_buttons = {
        "back_button": sub_back_button,
        "grid_100_button": grid_100_button,
        "grid_200_button": grid_200_button,
        "grid_300_button": grid_300_button,
        "grid_400_button": grid_400_button,
        "grid_500_button": grid_500_button,
        "worm_button": worm_button
    }
    
    worms_options_menu_buttons = {
        "back_button": sub_back_button,
        "worms_1_button": worms_1_button,
        "worms_3_button": worms_3_button,
        "worms_5_button": worms_5_button,
        "worms_10_button": worms_10_button,
        "worm_button": worm_button
    }
    
    track_options_menu_buttons = {
        "back_button": sub_back_button,
        "track_10_button": track_10_button,
        "track_25_button": track_25_button,
        "track_50_button": track_50_button,
        "worm_button": worm_button
    }
    
    movement_pattern_options_menu_buttons = {
        "back_button": sub_back_button,
        "triangle_pattern_button": triangle_pattern_button,
        "square_pattern_button": square_pattern_button,
        "worm_button": worm_button
    }

    # Main Menu Loop
    while simulation_settings.get("menu_running"):
        # Start menu
        menu.menu_window.fill(PASTEL_BLUE)
        
        # Calculate visible text content
        # visible_text_content = []
        y_position = menu.screen_height // 2
        # for item in menu.about_text:
        #     visible_text_content.append(item)
        
        # Get mouse position
        click_position = pg.mouse.get_pos()
        
        # Display Game Menu/s
        if not simulation_settings.get("game_running"):
            # Display Main Menu Buttons:
            if simulation_settings.get("menu_state") == "main":
                for button in main_menu_buttons.items():
                    button[1].draw()
            
            # Display Sub-menu Buttons:
            elif simulation_settings.get("menu_state") == "sub":
                for button in sub_menu_buttons.items():
                    button[1].draw()
            
            # Display Options Buttons:
            # Display FPS Options Buttons:
            elif simulation_settings.get("menu_state") == "options-fps":
                for button in fps_options_menu_buttons.items():
                    button[1].draw()
            
            # Display Grid Options Buttons:
            elif simulation_settings.get("menu_state") == "options-grid":
                for button in grid_options_menu_buttons.items():
                    button[1].draw()
            
            # Display Movement Pattern Options Buttons:
            elif simulation_settings.get("menu_state") == "options-pattern":
                for button in movement_pattern_options_menu_buttons.items():
                    button[1].draw()
            
            # Display Track Movements Options Buttons:
            elif simulation_settings.get("menu_state") == "options-track":
                for button in track_options_menu_buttons.items():
                    button[1].draw()
            
            # Display Worms Options Buttons:
            elif simulation_settings.get("menu_state") == "options-worms":
                for button in worms_options_menu_buttons.items():
                    button[1].draw()
            
            # Display About Section:
            elif simulation_settings.get("menu_state") == "about":
                for button in about_section_buttons.items():
                    button[1].draw()
                
                # Draw about section text
                scroll_y = menu.draw_text(y_position, scroll_y)
                # pg.display.flip()
        
        # Event handler
        for event in pg.event.get():
            # TODO: Check what this does... & remove if not needed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    simulation_settings.update({"game_running": False})
            
            elif event.type == pg.QUIT:
                simulation_settings.update({"menu_running": False})
            
            # Handle Button Clicks
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # Left click
                    # Check menu state
                    if simulation_settings.get("menu_state") == "main":
                        handle_button_click(main_menu_buttons, click_position)
                    elif simulation_settings.get("menu_state") == "sub":
                        handle_button_click(sub_menu_buttons, click_position)
                    elif simulation_settings.get("menu_state") == "options-fps":
                        handle_button_click(fps_options_menu_buttons, click_position)
                    elif simulation_settings.get("menu_state") == "options-grid":
                        handle_button_click(grid_options_menu_buttons, click_position)
                    elif simulation_settings.get("menu_state") == "options-worms":
                        handle_button_click(worms_options_menu_buttons, click_position)
                    elif simulation_settings.get("menu_state") == "options-track":
                        handle_button_click(track_options_menu_buttons, click_position)
                    elif simulation_settings.get("menu_state") == "options-pattern":
                        handle_button_click(movement_pattern_options_menu_buttons, click_position)
                    elif simulation_settings.get("menu_state") == "about":
                        handle_button_click(about_section_buttons, click_position)
            
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 4: # Scroll up
                print("Scrolling up...")
                scroll_y += 10
            
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 5: # Scroll down
                print("Scrolling down...")
                scroll_y -= 10
        
        # Limit menu frame rate
        pg.time.delay(menu.frame_rate)
        
        # Update the menu display
        pg.display.flip()

    # Quit the game
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
