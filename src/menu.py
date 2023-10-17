import sys
import pygame as pg
import pygame_menu as pm

# Import classes
from button import Button
from dropdown import Dropdown
from patersons_worms_simulator import PatersonsWormsSimulation

pg.init()



# WINDOW_SIZE = (800, 500)
FONT = pg.font.Font(None, 36)
WHITE = pg.Color("#FFFFFF")
GRAY = pg.Color("#CCCCCC")
BLACK = pg.Color("#000000")
PASTEL_BLUE = pg.Color("#B2DCEF")


class Menu:
    def __init__(self):
        self.screen_info = pg.display.Info()
        self.screen_height = int(self.screen_info.current_h * 0.5)
        self.menu_window = pg.display.set_mode((self.screen_height, self.screen_height))
        # self.menu_size = (500, 500)
        self.frame_rate = 60
        self.button_width = int(0.2 * self.screen_height)
        self.button_height = int(0.04 * self.screen_height)
        self.buttons = []
        # self.dropdowns = []


def display_menu(window, buttons, dropdowns):
    window.fill(PASTEL_BLUE)
    for button in buttons:
        button.draw()
    for dropdown in dropdowns:
        dropdown.draw()
    pg.display.flip()


def print_settings(main_menu):
    settings = main_menu.get_input_data()
    for key in settings.keys():
        print(f"{key}: {settings[key]}")


def update_variables(selected_menu, value=None):
    num_worms = int(selected_menu.get_input_data()[0])
    frame_rate = int(selected_menu.get_input_data()[1])
    grid_size = int(selected_menu.get_input_data()[2])
    print(f"Number of worms: {num_worms}")
    print(f"Frame rate: {frame_rate}")
    print(f"Grid size: {grid_size}")


def main():
    menu = Menu()
    
    # # Create main menu lists
    # num_worms_options = [str(i) for i in range(1, 11)]
    # frame_rate_options = [str(i) for i in range(30, 120, 30)]
    # grid_size_options = [str(i) for i in range(100, 500, 50)]
    
    # # Create main menu
    # main_menu = pm.Menu(
    #     title="Paterson's Worms Simulation",
    #     width=menu.screen_height,
    #     height=menu.screen_height,
    #     center_content=True,
    #     theme=pm.themes.THEME_BLUE
    # )
    
    # # Adjust main menu defaults
    # main_menu._theme.widget_font_size = 25
    # main_menu._theme.widget_font_color = BLACK
    # main_menu._theme.widget_alignment = pm.locals.ALIGN_CENTER
    
    # main_menu.add.label("Welcome to my Paterson's Worms Simulation!")
    
    # # Add dropdowns / range sliders
    # main_menu.add.dropselect("Number of worms: ", num_worms_options, default=5)
    # # main_menu.add.range_slider("Frame rate: ", default=30, range_values=[30, 120])
    # main_menu.add.dropselect("Frame rate: ", frame_rate_options, default=0)
    # main_menu.add.dropselect("Grid size: ", grid_size_options, default=1)
    
    
    # main_menu.add.button("Confirm Selections", update_variables)
    # main_menu.add.button("Exit", pm.events.EXIT)
    
    
    
    # main_menu.mainloop(menu.menu_window)
    
    
    pg.display.set_caption("Start Menu")
    
    # Load button images
    start_image = pg.image.load("assets/start-button.png").convert_alpha()
    exit_image = pg.image.load("assets/exit-button.png").convert_alpha()
    menu_image = pg.image.load("assets/menu-button.png").convert_alpha()
    
    # Resize button images
    start_image = pg.transform.scale(start_image, (menu.button_width, menu.button_height))
    exit_image = pg.transform.scale(exit_image, (menu.button_width, menu.button_height))
    menu_image = pg.transform.scale(menu_image, (menu.button_width, menu.button_height))

    # Create button image positions within menu window
    start_image_position = (((menu.screen_height // 2) - (menu.button_width // 2)), ((menu.screen_height // 2) - (menu.button_width // 2)))
    exit_image_position = (((menu.screen_height // 2) - (menu.button_width // 2)), (((menu.screen_height // 2) - (menu.button_width // 2)) + ((menu.screen_height // 2) - (menu.button_width // 2)) * 0.3))
    menu_image_position = (((menu.screen_height // 2) - (menu.button_width // 2)), (((menu.screen_height // 2) - (menu.button_width // 2)) - ((menu.screen_height // 2) - (menu.button_width // 2)) * 0.3))
    
    # Create dropdown positions (dp) within menu window
    num_worms_dp = (((menu.screen_height // 2) + (menu.button_width)), ((menu.screen_height // 2) - (menu.button_width // 2)))
    frame_rate_dp = (((menu.screen_height // 2) + (menu.button_width)), (((menu.screen_height // 2) - (menu.button_width // 2)) + ((menu.screen_height // 2) - (menu.button_width // 2)) * 0.3))
    grid_size_dp = (((menu.screen_height // 2) + (menu.button_width)), (((menu.screen_height // 2) - (menu.button_width // 2)) - ((menu.screen_height // 2) - (menu.button_width // 2)) * 0.3))
    
    # Create buttons and dropdowns
    buttons = [
        Button(menu, menu_image_position, menu_image, "menu"), 
        Button(menu, start_image_position, start_image, "start"), 
        Button(menu, exit_image_position, exit_image, "exit")
    ]
    dropdowns = [
        Dropdown(menu, grid_size_dp, ["100", "150", "200", "250", "300", "350", "400", "450", "500"], "grid"),
        Dropdown(menu, frame_rate_dp, ["30", "60", "90", "120"], "fps"),
        Dropdown(menu, num_worms_dp, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], "worms")
    ]
    
    # Initialise simulation
    num_worms = 5
    frame_rate = 40
    grid_size = 10

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            elif event.type == pg.MOUSEMOTION:
                # for button in buttons + dropdowns:
                for button in buttons:
                    button.is_hovered = button.image_rect.collidepoint(event.pos)
                    print("Button hovered!")
            elif event.type == pg.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_hovered:
                        if button.text == "start":
                            print("Start button pressed!")
                            sim = PatersonsWormsSimulation(grid_size, num_worms, frame_rate)
                            sim.run_simulation()
                        elif button.text == "exit":
                            print("Exit button pressed!")
                            running = False
                        elif button.text == "menu":
                            print("Menu button pressed!")
                            # TODO: Display menu
                            # main_menu.mainloop(menu.menu_window)
                        # elif button.text == "worms+":
                        #     print("Increase frame rate button pressed!!")
                        #     num_worms += 1
                        # elif button.text == "worms-":
                        #     print("Increase frame rate button pressed!")
                        #     num_worms = max(1, num_worms + 1)
                        # elif button.text == "fps+":
                        #     print("Increase frame rate button pressed!")
                        #     frame_rate += 10
                        # elif button.text == "fps-":
                        #     print("Decrease frame rate button pressed!")
                        #     frame_rate = max(10, frame_rate - 10)
                        # elif button.text == "grid+":
                        #     print("Increase grid size button pressed!")
                        #     grid_size += 10
                        # elif button.text == "grid-":
                        #     print("Decrease grid size button pressed!")
                        #     frame_rate = max(10, grid_size - 10)
                
                for dropdown in dropdowns:
                    if dropdown.is_hovered:
                        print("Dropdown hovered!")
                        dropdown.next_option()
                        print(dropdown.options[dropdown.selected_option])
                        if dropdown.text == "worms":
                            print("Worms dropdown pressed!")
                            num_worms = int(dropdown.options[dropdown.selected_option])
                        elif dropdown.text == "fps":
                            print("Frame rate dropdown pressed!")
                            frame_rate = int(dropdown.options[dropdown.selected_option])
                        elif dropdown.text == "grid":
                            print("Grid size dropdown pressed!")
                            grid_size = int(dropdown.options[dropdown.selected_option])
                
        # mouse = pg.mouse.get_pos() # Get mouse position (x, y) tuple

        # Limit frame rate
        pg.time.delay(30)

        # Display the menu
        display_menu(menu.menu_window, buttons, dropdowns)
        # display_menu(window, num_worms, frame_rate, grid_size, buttons, dropdowns)

    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main() # Calling main function
