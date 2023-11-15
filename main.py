import pygame
from sys import exit

pygame.init()
# Set game title
pygame.display.set_caption("Runner")

# Create game window
window_width = 1000
window_height = 700
screen = pygame.display.set_mode((window_width, window_height))

# Create the "Surface"(the content that is going to be displayed on the window)
surface_width = 1000
surface_height = 700
surface_position = (0, 0)
display_surface = pygame.Surface((surface_width, surface_height))
display_surface.fill("Blue")

# Create the clock object, which is called inside the While loop in order to set the framerate
clock = pygame.time.Clock()

while True:
    # Close the game when the "X" button is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(display_surface, surface_position)

    # Updates the screen so it doesn't close after the code runs
    pygame.display.update()

    # Set the framerate cap to 60 fps
    clock.tick(60)
