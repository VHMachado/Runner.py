from pygame import quit, time
from texts import get_score


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
            enemies_rect_list = []
    return enemies_rect_list, final_score, game_active


def remove_offscreen_enemies(enemies_rect_list):
    for enemy_rectangle in enemies_rect_list[:]:
        if enemy_rectangle.left <= -100:
            enemies_rect_list.remove(enemy_rectangle)


def draw_enemies(screen, enemies_rect_list, snail_surface, fly_surface):
    for enemy_rectangle in enemies_rect_list:
        if enemy_rectangle.bottom == 232:
            screen.blit(snail_surface, enemy_rectangle)
        else:
            screen.blit(fly_surface, enemy_rectangle)
