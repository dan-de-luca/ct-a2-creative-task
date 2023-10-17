import pygame

WHITE = pygame.Color("#FFFFFF")
GRAY = pygame.Color("#CCCCCC")
BLACK = pygame.Color("#000000")

class Dropdown:
    def __init__(self, options, position):
        self.options = options
        self.selected_option = 0
        self.position = position
        self.rect = pygame.Rect(position, (200, 50))
        self.is_hovered = False

    def draw(self, surface):
        color = GRAY if self.is_hovered else WHITE
        pygame.draw.rect(surface, color, self.rect)
        text_surface = FONT.render(self.options[self.selected_option], True, (0, 0, 0))
        surface.blit(text_surface, (self.position[0] + 10, self.position[1] + 10))
    
    def next_option(self):
        self.selected_option = (self.selected_option + 1) % len(self.options)