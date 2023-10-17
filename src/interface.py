import pygame
import sys

# Import classes
from button import Button
from dropdown import Dropdown
from patersons_worms_simulator import PatersonsWormsSimulation

pygame.init()

WINDOW_SIZE = (400, 300)
FONT = pygame.font.Font(None, 36)
WHITE = pygame.Color("#FFFFFF")
GRAY = pygame.Color("#CCCCCC")
BLACK = pygame.Color("#000000")

def display_interface(window, num_worms, frame_rate, grid_size, buttons, dropdowns):
    window.fill(GRAY)
    for button in buttons:
        button.draw(window)
    for dropdown in dropdowns:
        dropdown.draw(window)
    pygame.display.flip()

def main():
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Settings")

    # Create buttons and dropdowns
    buttons = [Button("Increase Worms", (50, 50)), Button("Decrease Worms", (50, 110)),
            Button("Increase Frame Rate", (50, 170)), Button("Decrease Frame Rate", (50, 230))]
    dropdowns = [Dropdown(["10 Worms", "20 Worms", "30 Worms"], (250, 50)),
            Dropdown(["20 FPS", "30 FPS", "40 FPS"], (250, 110)),
            Dropdown(["10x10 Grid", "20x20 Grid", "30x30 Grid"], (250, 170))]

    # Initialise simulation
    num_worms = 10
    frame_rate = 20
    grid_size = 10

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEMOTION:
                for button in buttons + dropdowns:
                    button.is_hovered = button.rect.collidepoint(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_hovered:
                        if button.text == "Increase Worms":
                            num_worms += 10
                        elif button.text == "Decrease Worms":
                            num_worms = max(10, num_worms - 10)
                        elif button.text == "Increase Frame Rate":
                            frame_rate += 10
                        elif button.text == "Decrease Frame Rate":
                            frame_rate = max(10, frame_rate - 10)
                for dropdown in dropdowns:
                    if dropdown.is_hovered:
                        dropdown.next_option()

        # Limit frame rate
        pygame.time.delay(10)

        # Display the interface
        display_interface(window, num_worms, frame_rate, grid_size, buttons, dropdowns)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
