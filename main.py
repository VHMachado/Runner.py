import pygame
from texts import display_score, display_lose_screen
from scenarios import display_scenario, get_ground_position, display_menu

from characters import (
    player_stand,
    player_walk_frame_1,
    player_walk_frame_2,
    player_jumping_sprite,
    player_animation,
    create_player_rectangle,
    snail_frame_1,
    snail_frame_2,
    create_snail_rectangle,
    fly_frame_1,
    fly_frame_2,
    create_fly_rectangle,
)

from game_mechanics import (
    start_game,
    play_again,
    close_game,
    gravity,
    create_enemies,
    check_ground_collision,
    player_jump,
    move_enemies,
    check_collisions,
    remove_offscreen_enemies,
    draw_enemies,
    reset_game_configurations,
)

# Initializes Pygame
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
player_walk_frame_1 = player_walk_frame_1()
player_walk_frame_2 = player_walk_frame_2()
player_frames = [player_walk_frame_1, player_walk_frame_2]
player_animation_index = 0

player_jump_surface = player_jumping_sprite()

player_rectangle = create_player_rectangle()

# Creates the enemies in the game
# Initializes the enemies list. All the enemies will be "stored" here during the gameplay
enemies_rect_list = []

# Initializes the snails frames and animation logic
snail_frame_1 = snail_frame_1()
snail_frame_2 = snail_frame_2()

snail_frames = [snail_frame_1, snail_frame_2]
snail_animation_index = 0

snail_surface = snail_frames[snail_animation_index]

# Initializes the flies frames and animation logic
fly_frame_1 = fly_frame_1()
fly_frame_2 = fly_frame_2()
fly_frames = [fly_frame_1, fly_frame_2]
fly_animation_index = 0

fly_surface = fly_frames[fly_animation_index]

# Creates a Timer for the enemy spawning
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1500)

# Creater a Timer for the Snail Animation
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

# Creater a Timer for the Snail Animation
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

# Sets initial variables
timer = 0
score = 0
final_score = 0
gravity_value = 0
can_jump = True
access_menu = True
game_active = False
ground_position = get_ground_position()

while True:
    for event in pygame.event.get():
        # Close the game when the "X" button is clicked
        if event.type == pygame.QUIT:
            close_game()
        # Checks if any key has been pressed on the keyboard
        if event.type == pygame.KEYDOWN:
            # Checks if the pressed button is the SPACE key
            if event.key == pygame.K_SPACE:
                if access_menu:
                    # If the SPACE key is pressed in the game's menu, the game will start
                    access_menu, game_active = start_game(access_menu, game_active)
                elif game_active:
                    # If the SPACE key is pressed during the game, the player will jump
                    can_jump, gravity_value, ground_collision = player_jump(
                        can_jump, gravity_value, ground_collision
                    )
                else:
                    # If the SPACE key is pressed at the lose screen, the game will restart
                    timer, game_active = play_again(timer, game_active)

        # The actions here are only executed when both the game is active and the respective timer has ended
        if game_active:
            if event.type == enemy_timer:
                # Chooses whether a snail or a fly will be spawned
                enemies_rect_list = create_enemies(
                    enemies_rect_list, create_snail_rectangle(), create_fly_rectangle()
                )

            if event.type == snail_animation_timer:
                if snail_animation_index == 0:
                    snail_animation_index = 1
                else:
                    snail_animation_index = 0
                snail_surface = snail_frames[snail_animation_index]

            if event.type == fly_animation_timer:
                if fly_animation_index == 0:
                    fly_animation_index = 1
                else:
                    fly_animation_index = 0
                fly_surface = fly_frames[fly_animation_index]

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
        gravity_value, player_rectangle.y = gravity(gravity_value, player_rectangle.y)

        # keeps the player above the ground and tells if he can jump if colliding with it
        ground_collision, can_jump, player_rectangle.bottom = check_ground_collision(
            player_rectangle.bottom, ground_position[1]
        )

        # Draws the player on the screen
        player_animation_index = player_animation(
            can_jump,
            player_animation_index,
            screen,
            player_frames,
            player_jump_surface,
            player_rectangle,
        )

        # Controls enemies movement
        if enemies_rect_list:
            # Controls enemies movement
            move_enemies(enemies_rect_list)

            # Checks collisions
            final_score, game_active = check_collisions(
                enemies_rect_list, player_rectangle, final_score, game_active, timer
            )

            # Deletes the enemy after it passess the screen limits
            remove_offscreen_enemies(enemies_rect_list)

            # Draws enemies on the screen
            draw_enemies(
                screen,
                enemies_rect_list,
                snail_surface,
                fly_surface,
                ground_position[1],
            )
        else:
            enemies_rect_list = []

    else:
        # Sets the lose screen that is show when the player loses
        enemies_rect_list, gravity_value, player_rectangle = reset_game_configurations(
            enemies_rect_list,
            gravity_value,
            player_rectangle,
            create_player_rectangle(),
        )
        display_scenario(screen)
        display_lose_screen(screen, final_score)

    # Updates the screen so it doesn't close after the code runs the first time
    pygame.display.update()

    # Set the framerate cap to 60 frames per second
    clock.tick(60)
