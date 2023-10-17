import pygame

# FONT = pygame.font.Font(None, 20)
# WHITE = pygame.Color("#FFFFFF")
# GRAY = pygame.Color("#CCCCCC")
# BLACK = pygame.Color("#000000")

class Button:
    def __init__(self, menu, position, image, text=None):
        # Attributes
        self.menu = menu
        self.window = menu.menu_window
        self.position = position
        self.text = text
        self.image = image
        self.width = menu.button_width_main
        self.height = menu.button_height_main
        self.margin = 5
        self.window_height = menu.screen_height
        self.window_width = menu.screen_height
        self.image_rect = pygame.Rect((self.window_width - 2 * self.margin - 2 * self.width, self.window_height // 2 - self.height // 2, self.width, self.height))
        self.image_rect.topleft = position
        self.clicked = False
    
    def draw(self):
        action = False
        
        # Get mouse position
        pos = pygame.mouse.get_pos()
        
        # Check mouseover and clicked conditions
        if self.image_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                # self.is_hovered = True
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        # Draw button on window
        self.window.blit(self.image, self.image_rect)
        
        return action