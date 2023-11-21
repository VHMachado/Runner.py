import pygame
from operator import sub
from enemies import snail
from player import player
from sys import exit

pygame.init()
# Set game title
pygame.display.set_caption("Runner")

# Create game window
resolution = (800, 400)
screen = pygame.display.set_mode(resolution)

# Create the Sky image "Surface"(a content that is going to be displayed on the window)
sky_surface = pygame.image.load("./Assets/graphics/Sky.png").convert()
sky_position = (0, 0)

# Create the ground Surface
ground_surface = pygame.image.load("./Assets/graphics/ground.png").convert()
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

# Creates the enemies in the game
snail_surface, snail_position = snail()

# Creates the player in the game
player_suface, player_position = player()

while True:
    # Close the game when the "X" button is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, sky_position)
    screen.blit(ground_surface, ground_position)
    screen.blit(text_surface, text_position)
    snail_position[0] -= 5
    if snail_position[0] < -75:
        snail_position = snail()[1]
    screen.blit(snail_surface, snail_position)
    screen.blit(player_suface, player_position)

    # Updates the screen so it doesn't close after the code runs
    pygame.display.update()

    # Set the framerate cap to 60 fps
    clock.tick(60)
