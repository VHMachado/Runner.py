import pygame
from operator import sub
from enemies import snail
from player import player
from fontConfig import font_config
from score import display_score
from lose import lose_text
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
font = font_config()

# Create the Text surface with the Score
score_surface, score_position = display_score(font)

# Creates the loose text screen
text_lose_surface, text_lose_position = lose_text(font)

# Creates the enemies in the game
snail_surface, snail_position = snail()

# Creates the player in the game
player_suface, player_position = player()

mouse_click = False
lose = False

while True:
    # Close the game when the "X" button is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True

    screen.blit(sky_surface, sky_position)
    screen.blit(ground_surface, ground_position)
    screen.blit(score_surface, score_position)
    screen.blit(snail_surface, snail_position)
    screen.blit(player_suface, player_position)

    player_position.right += 5
    snail_position.left -= 5

    if snail_position.left <= -80:
        snail_position = snail()[1]
    if player_position.colliderect(snail_position):
        snail_position = snail()[1]
        player_position = player()[1]
        lose = True
    if lose:
        screen.blit(text_lose_surface, text_lose_position)

    # if player_position.collidepoint(mouse_position) or snail_position.collidepoint(
    #     mouse_position
    # ):
    #     snail_position = snail()[1]
    #     player_position = player()[1]

    # if mouse_click and player_position.collidepoint(mouse_position):
    #     player_position = player()[1]
    #     mouse_click = False

    # Updates the screen so it doesn't close after the code runs
    pygame.display.update()

    # Set the framerate cap to 60 fps
    clock.tick(60)
