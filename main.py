import pygame
from characters import player_stand, player_walk_1, snail, fly, gravity
from texts import get_score, display_score, display_lose_screen
from scenarios import display_scenario, get_ground_position, display_menu
from random import randint
from sys import exit


pygame.init()

# Set game title
pygame.display.set_caption("Runner.py")

# Creates the game window
resolution = (800, 400)
screen = pygame.display.set_mode(resolution)

# Create the clock object, which is called inside the While loop in order to set the framerate
clock = pygame.time.Clock()

# Creates the player sprite that is displayed at the game's menu
player_stand_surface, player_stand_rectangle = player_stand()

# Creates the player
player_suface, player_rectangle = player_walk_1()

# Creates the enemies in the game
enemies_rect_list = []
snail_surface, snail_rectangle = snail()
fly_surface, fly_rectangle = fly()

# Sets initial variables
timer = 0
score = 0
gravity_value = 0
jump_cooldown = True
access_menu = True
game_active = False
ground_position = get_ground_position()

# Sets Timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1500)

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
                if access_menu:
                    # If the SPACE key is pressed in the game's menu, the game will start
                    access_menu = False
                    game_active = True
                    snail_rectangle = snail()[1]
                elif game_active:
                    # If the SPACE key is pressed during the game, the player will jump
                    if jump_cooldown == True:
                        gravity = -20
                        jump_cooldown = False
                        ground_collision = False
                else:
                    # If the SPACE key is pressed at the lose screen, the game will restart
                    timer = pygame.time.get_ticks()
                    snail_rectangle = snail()[1]
                    game_active = True

        # The actions here are  executed only when both the game is active and the timer has ended
        if event.type == enemy_timer and game_active:
            # Chooses whether a snail or a fly will be spawned
            if randint(0, 2):
                enemies_rect_list.append(snail()[1])
            else:
                enemies_rect_list.append(fly()[1])

    if access_menu:
        # Sets the menu screen that's show at the beginning
        timer = display_menu(
            screen,
            player_stand_surface,
            player_stand_rectangle,
        )
    elif game_active:
        # This is where the game actually "happens"

        # Puts the scenario and the score on the screen
        display_scenario(screen)
        display_score(screen, timer)

        # Makes the player fall after it jumps
        gravity(gravity_value, player_rectangle.y)

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
                enemy_rectangle.left -= 5

                # Checks collisions
                if player_rectangle.colliderect(enemy_rectangle):
                    final_score = get_score(timer)
                    game_active = False
                    enemies_rect_list = []

                # Deletes the enemy after it passess the screen limits
                if enemy_rectangle.left <= -100:
                    enemies_rect_list.remove(enemy_rectangle)

                # Draws enemies on the screen
                if enemy_rectangle.bottom == 232:
                    screen.blit(snail_surface, enemy_rectangle)
                else:
                    screen.blit(fly_surface, enemy_rectangle)
        else:
            enemies_rect_list = []

    else:
        # Sets the lose screen that is show when the player loses
        display_scenario(screen)
        display_lose_screen(screen, final_score)

    # Updates the screen so it doesn't close after the code runs the first time
    pygame.display.update()

    # Set the framerate cap to 60 frames per second
    clock.tick(60)
