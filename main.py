import pygame
from characters import player_stand, player_walk_1, snail
from texts import display_score, display_lose_screen, display_menu_text
from scenario import display_scenario, get_ground_position
from sys import exit

pygame.init()

# Set game title
pygame.display.set_caption("Runner")

# Create game window
resolution = (800, 400)
screen = pygame.display.set_mode(resolution)

# Create the clock object, which is called inside the While loop in order to set the framerate
clock = pygame.time.Clock()

# Creates the enemies in the game
snail_surface, snail_rectangle = snail()

# Creates the player sprite that is displayed on the menu
player_stand_surface, player_stand_rectangle = player_stand()

# Creates the player in the game
player_suface, player_rectangle = player_walk_1()

# Set initial variables
timer = 0
gravity = 0
jump_cooldown = True
acess_menu = True
game_active = False
ground_position = get_ground_position()

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
                if acess_menu:
                    acess_menu = False
                    game_active = True
                    snail_rectangle = snail()[1]
                elif game_active:
                    if jump_cooldown == True:
                        gravity = -20
                        jump_cooldown = False
                        ground_collision = False
                else:
                    snail_rectangle = snail()[1]
                    game_active = True
    if acess_menu:
        screen.fill((94, 129, 162))
        screen.blit(player_stand_surface, player_stand_rectangle)
        display_menu_text(screen)
    elif game_active:
        # Puts the scenario and the enemy on the screen
        display_scenario(screen)
        display_score(screen, timer)
        screen.blit(snail_surface, snail_rectangle)

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
        display_scenario(screen)
        display_score(screen, timer)
        display_lose_screen(screen)

    # Updates the screen so it doesn't close after the code runs
    pygame.display.update()

    # Set the framerate cap to 60 frames per second
    clock.tick(60)
