import pygame as pg

class Button:
    def __init__(self, menu, position, image, width, height, text=None, action=None):
        # Attributes
        # self.menu = menu
        self.window = menu.menu_window
        self.position = position
        self.image_path = image
        self.text = text
        self.action = action
        # Does this negate the need for different button sizes? Or is this just used for the button window dimensions?
        self.width = width
        self.height = height
        self.margin = 5
        self.window_height = menu.screen_height
        self.window_width = menu.screen_height
        self.image = pg.image.load(self.image_path).convert_alpha()
        self.image_rect = pg.Rect((self.window_width - 2 * self.margin - 2 * self.width, self.window_height // 2 - self.height // 2, self.width, self.height))
        self.image_rect.topleft = position
        self.clicked = False
    
    def process_image(self):
        # Process image
        # self.image = pg.image.load(self.image).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = self.position
    
    def draw(self):
        # Process button image
        self.process_image()
        
        # action = False
        
        # # Get mouse position
        # pos = pg.mouse.get_pos()
        
        # # Check mouseover and clicked conditions
        # if self.image_rect.collidepoint(pos):
        #     if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
        #         # self.is_hovered = True
        #         self.clicked = True
        #         # action = True
        
        # if pg.mouse.get_pressed()[0] == 0:
        #     self.clicked = False
        
        # Draw button on window
        self.window.blit(self.image, self.image_rect)
        
        # return action
        