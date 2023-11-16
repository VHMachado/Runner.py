import pygame
from sys import exit

pygame.init()
# Set game title
pygame.display.set_caption("Runner")

# Create game window
window_width = 800
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))

# Create the Sky image "Surface"(a content that is going to be displayed on the window)
sky_surface = pygame.image.load("./Assets/graphics/Sky.png")
sky_position = (0, 0)

# Create the ground Surface
ground_surface = pygame.image.load("./Assets/graphics/ground.png")
ground_position = (0, 232)

# Create the clock object, which is called inside the While loop in order to set the framerate
clock = pygame.time.Clock()

# Set the font that is going to be used to display text
font_type = "./Assets/font/Pixeltype.ttf"
font_size = 50
game_font = pygame.font.Font(font_type, font_size)

# Create the Text surface with the Score
text = "Score = "
text_antialising = False
text_color = "Black"
text_surface = game_font.render(text, text_antialising, text_color)
text_position = (10, 10)

while True:
    # Close the game when the "X" button is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, sky_position)
    screen.blit(ground_surface, ground_position)
    screen.blit(text_surface, text_position)

    # Updates the screen so it doesn't close after the code runs
    pygame.display.update()

    # Set the framerate cap to 60 fps
    clock.tick(60)
