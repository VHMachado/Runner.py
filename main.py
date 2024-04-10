import pygame
from characters import player_stand, player_walk_1, snail
from texts import get_score, display_score, display_lose_screen, display_menu_text
from scenario import display_scenario, get_ground_position
from sys import exit


pygame.init()

# Set game title
pygame.display.set_caption("Runner.py")

# Create game window
resolution = (800, 400)
screen = pygame.display.set_mode(resolution)

# Create the clock object, which is called inside the While loop in order to set the framerate
clock = pygame.time.Clock()

# Creates the enemies in the game
snail_surface, snail_rectangle = snail()

enemies_rect_list = []

# Creates the player sprite that is displayed on the menu
player_stand_surface, player_stand_rectangle = player_stand()

# Creates the player in the game
player_suface, player_rectangle = player_walk_1()

# Set initial variables
timer = 0
score = 0
gravity = 0
jump_cooldown = True
access_menu = True
game_active = False
ground_position = get_ground_position()

# Timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 900)

while True:
    for event in pygame.event.get():
        # Close the game when the "X" button is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Checks if any key has been pressed on the keyboard
        if event.type == pygame.KEYDOWN:
            # Checks if the pressed button is the SPACE key
            if event.key == pygame.K_SPACE:
                # If the SPACE key has been pressed, the player will jump
                if access_menu:
                    access_menu = False
                    game_active = True
                    snail_rectangle = snail()[1]
                elif game_active:
                    if jump_cooldown == True:
                        gravity = -20
                        jump_cooldown = False
                        ground_collision = False
                else:
                    timer = pygame.time.get_ticks()
                    snail_rectangle = snail()[1]
                    game_active = True

        if event.type == enemy_timer and game_active:
            enemies_rect_list.append(snail()[1])

    if access_menu:
        screen.fill((94, 129, 162))
        screen.blit(player_stand_surface, player_stand_rectangle)
        display_menu_text(screen)
        timer = pygame.time.get_ticks()
    elif game_active:
        # Puts the scenario and the enemy on the screen
        display_scenario(screen)
        display_score(screen, timer)

        # Makes the player fall after it jumps
        gravity += 1
        player_rectangle.y += gravity

        if jump_cooldown == False:
            if ground_collision == True:
                jump_cooldown = True

        # Player Movement
        if player_rectangle.bottom >= ground_position[1]:
            player_rectangle.bottom = ground_position[1]
            ground_collision = True
        screen.blit(player_suface, player_rectangle)

        # Enemy Movement
        if enemies_rect_list:
            for enemy_rectangle in enemies_rect_list:
                enemy_rectangle.x -= 5
                screen.blit(snail_surface, enemy_rectangle)
                # Makes the player lose if the snail collide with the player
                if player_rectangle.colliderect(enemy_rectangle):
                    final_score = get_score(timer)
                    game_active = False
                    enemies_rect_list = []
                # Teleports the enemy back to it's initial position if it passes the screen limit
                if enemy_rectangle.left <= -80:
                    enemy_rectangle = snail()[1]
        else:
            enemies_rect_list = []

    else:
        display_scenario(screen)
        display_lose_screen(screen, final_score)

    # Updates the screen so it doesn't close after the code runs
    pygame.display.update()

    # Set the framerate cap to 60 frames per second
    clock.tick(60)
