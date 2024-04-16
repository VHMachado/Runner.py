from pygame import image, transform
from random import randint


def player_stand():
    surface = image.load("./Assets/graphics/Player/player_stand.png").convert_alpha()
    surface = transform.scale2x(surface)
    position = [400, 200]
    rectangle = surface.get_rect(center=position)
    return surface, rectangle


def player_walk_frame_1():
    surface = image.load("./Assets/graphics/Player/player_walk_1.png").convert_alpha()
    return surface


def player_walk_frame_2():
    surface = image.load("./Assets/graphics/Player/player_walk_2.png").convert_alpha()
    return surface


def player_jumping_sprite():
    surface = image.load("./Assets/graphics/Player/jump.png").convert_alpha()
    return surface


def create_player_rectangle():
    surface = player_walk_frame_1()
    position = [80, 232]
    rectangle = surface.get_rect(midbottom=(position))
    return rectangle


def player_animation(
    can_jump,
    player_animation_index,
    screen,
    player_frames,
    player_jump_surface,
    player_rectangle,
):
    if can_jump == True:
        player_animation_index += 0.1
        if player_animation_index >= len(player_frames):
            player_animation_index = 0
        screen.blit(player_frames[int(player_animation_index)], player_rectangle)
    else:
        screen.blit(player_jump_surface, player_rectangle)
    return player_animation_index


def snail_frame_1():
    surface = image.load("./Assets/graphics/snail/snail1.png").convert_alpha()
    return surface


def snail_frame_2():
    surface = image.load("./Assets/graphics/snail/snail2.png").convert_alpha()
    return surface


def create_snail_rectangle():
    surface = snail_frame_1()
    position = [randint(900, 1000), 232]
    rectangle = surface.get_rect(midbottom=(position))
    return rectangle


def fly_frame_1():
    surface = image.load("./Assets/graphics/Fly/Fly1.png").convert_alpha()
    return surface


def fly_frame_2():
    surface = image.load("./Assets/graphics/Fly/Fly2.png").convert_alpha()
    return surface


def create_fly_rectangle():
    surface = fly_frame_1()
    position = [randint(900, 1000), 140]
    rectangle = surface.get_rect(midbottom=(position))
    return rectangle
