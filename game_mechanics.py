from pygame import quit, time


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


def enemies_movement():
    pass
