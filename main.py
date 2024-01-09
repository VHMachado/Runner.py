import pygame
from enemies import snail
from player import player
from texts import display_score, display_lose_screen
from sys import exit

pygame.init()

# Set a timer, that is used to calculate the score
timer = pygame.time.get_ticks()

# Set game title
pygame.display.set_caption("Runner")

# Create game window
resolution = (800, 400)
screen = pygame.display.set_mode(resolution)

# Activates the game
game_active = True

# Create the Sky image "Surface"(a content that is going to be displayed on the window)
sky_surface = pygame.image.load("./Assets/graphics/Sky.png").convert()
sky_position = (0, 0)

# Create the ground Surface
ground_surface = pygame.image.load("./Assets/graphics/ground.png").convert()
ground_position = (0, 232)

# Create the clock object, which is called inside the While loop in order to set the framerate
clock = pygame.time.Clock()

# Creates the enemies in the game
snail_surface, snail_rectangle = snail()

# Creates the player in the game
player_suface, player_rectangle = player()

# Set initial variables
gravity = 0
jump_cooldown = True

while True:
    for event in pygame.event.get():
        # Close the game when the "X" button is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Detects mouse movement
        if event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos
        # Checks if the player has clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the mouse button has been pressed, the player will jump
            if player_rectangle.collidepoint(mouse_position):
                if jump_cooldown == True:
                    gravity = -20
                    jump_cooldown = False
                    ground_collision = False
        # Checks if any key has been pressed on the keyboard
        if event.type == pygame.KEYDOWN:
            # Checks if the pressed button is the SPACE key
            if event.key == pygame.K_SPACE:
                # If the SPACE key has been pressed, the player will jump
                if game_active:
                    if jump_cooldown == True:
                        gravity = -20
                        jump_cooldown = False
                        ground_collision = False
                else:
                    game_active = True
                    snail_rectangle = snail()[1]

    if game_active:
        # Puts the scenario and the enemy on the screen
        screen.blit(sky_surface, sky_position)
        screen.blit(ground_surface, ground_position)
        screen.blit(snail_surface, snail_rectangle)
        display_score(screen)

        # Makes the player fall after it jumps
        gravity += 1
        player_rectangle.y += gravity

        if jump_cooldown == False:
            if ground_collision == True:
                jump_cooldown = True

        # Checks if there is collision between the plauer and the ground, making him stand above it
        if player_rectangle.bottom >= ground_position[1]:
            player_rectangle.bottom = ground_position[1]
            ground_collision = True

        # Puts the player on the screen
        screen.blit(player_suface, player_rectangle)

        # Moves the player and the enemies
        # player_rectangle.right += 5
        snail_rectangle.left -= 5

        # Teleports the enemy back to it's initial position if it passes the screen limit
        if snail_rectangle.left <= -80:
            snail_rectangle = snail()[1]

        # Makes the player lose if the snail collide with the player
        if player_rectangle.colliderect(snail_rectangle):
            game_active = False
    else:
        screen.blit(sky_surface, sky_position)
        screen.blit(ground_surface, ground_position)
        display_score(screen)
        display_lose_screen(screen)

    # Updates the screen so it doesn't close after the code runs
    pygame.display.update()

    # Set the framerate cap to 60 frames per second
    clock.tick(60)
