import pygame
pygame.init()

FONT = pygame.font.SysFont("arialblack", 40)
WHITE = pygame.Color("#FFFFFF")
GRAY = pygame.Color("#CCCCCC")
BLACK = pygame.Color("#000000")

class Dropdown:
    def __init__(self, menu, position, options, text):
        # Args
        self.menu = menu
        self.position = position
        self.options = options
        self.text = text
        
        # Additional attributes
        self.selected_option = 0
        self.width = menu.button_width
        self.height = menu.button_height
        self.margin = 20
        self.window = menu.menu_window
        self.window_height = menu.screen_height
        self.window_width = menu.screen_height
        self.dropdown_rect = pygame.Rect((self.window_width - 2 * self.margin - 2 * self.width, self.window_height // 2 - self.height // 2, self.width, self.height))
        self.dropdown_rect.topleft = position
        self.is_hovered = False

    def draw(self):
        color = GRAY if self.is_hovered else WHITE
        pygame.draw.rect(self.window, color, self.dropdown_rect)
        text_surface = FONT.render(self.options[self.selected_option], True, (0, 0, 0))
        self.window.blit(text_surface, (self.position[0] + 10, self.position[1] + 10))

    def next_option(self):
        self.selected_option = (self.selected_option + 1) % len(self.options)