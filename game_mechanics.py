from pygame import quit, time
from texts import get_score
from random import randint


def close_game():
    quit()
    exit()


def start_game(access_menu, game_active):
    access_menu = False
    game_active = True
    return access_menu, game_active


def play_again(timer, game_active):
    timer = time.get_ticks()
    game_active = True
    return timer, game_active


def gravity(gravity, player_y):
    gravity += 1
    player_y += gravity
    return gravity, player_y


def create_enemies(enemies_rect_list, snail_rectangle, fly_rectangle):
    if randint(0, 2):
        enemies_rect_list.append(snail_rectangle)
    else:
        enemies_rect_list.append(fly_rectangle)
    return enemies_rect_list


def check_ground_collision(player_bottom, ground_position):
    if player_bottom >= ground_position:
        player_bottom = ground_position
        return True, True, player_bottom
    else:
        return False, False, player_bottom


def player_jump(can_jump, gravity_value, ground_collision):
    if can_jump == True:
        gravity_value = -20
        can_jump = False
        ground_collision = False
    return can_jump, gravity_value, ground_collision


def move_enemies(enemies_rect_list):
    for enemy_rectangle in enemies_rect_list:
        enemy_rectangle.left -= 5


def check_collisions(
    enemies_rect_list, player_rectangle, final_score, game_active, timer
):
    for enemy_rectangle in enemies_rect_list:
        if player_rectangle.colliderect(enemy_rectangle):
            final_score = get_score(timer)
            game_active = False
    return final_score, game_active


def remove_offscreen_enemies(enemies_rect_list):
    for enemy_rectangle in enemies_rect_list[:]:
        if enemy_rectangle.left <= -100:
            enemies_rect_list.remove(enemy_rectangle)


def draw_enemies(
    screen, enemies_rect_list, snail_surface, fly_surface, ground_position
):
    for enemy_rectangle in enemies_rect_list:
        if enemy_rectangle.bottom == ground_position:
            screen.blit(snail_surface, enemy_rectangle)
        else:
            screen.blit(fly_surface, enemy_rectangle)


def reset_game_configurations(
    enemies_rect_list, gravity_value, player_rectangle, player_initial_position
):
    enemies_rect_list.clear()
    gravity_value = 0
    player_rectangle = player_initial_position
    return enemies_rect_list, gravity_value, player_rectangle
