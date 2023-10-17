import pygame

FONT = pygame.font.Font(None, 20)
WHITE = pygame.Color("#FFFFFF")
GRAY = pygame.Color("#CCCCCC")
BLACK = pygame.Color("#000000")

class Button:
    def __init__(self, text, position):
        self.text = text
        self.position = position
        self.rect = pygame.Rect(position, (100, 50))
        self.is_hovered = False
    
    def draw(self, surface):
        color = GRAY if self.is_hovered else WHITE
        pygame.draw.rect(surface, color, self.rect)
        text_surface = FONT.render(self.text, True, BLACK)
        surface.blit(text_surface, (self.position[0] + 10, self.position[1] + 10))