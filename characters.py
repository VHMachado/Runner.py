from pygame import image, transform
from random import randint


def player_stand():
    surface = image.load("./Assets/graphics/Player/player_stand.png").convert_alpha()
    surface = transform.scale2x(surface)
    position = [400, 200]
    rectangle = surface.get_rect(center=position)
    return surface, rectangle


def player_walk_1_sprite():
    surface = image.load("./Assets/graphics/Player/player_walk_1.png").convert_alpha()
    return surface


def player_walk_2_sprite():
    surface = image.load("./Assets/graphics/Player/player_walk_2.png").convert_alpha()
    return surface


def player_jumping_sprite():
    surface = image.load("./Assets/graphics/Player/jump.png").convert_alpha()
    return surface


def create_player_rectangle():
    surface = player_walk_1_sprite()
    position = [80, 232]
    rectangle = surface.get_rect(midbottom=(position))
    return rectangle


def player_animation(
    can_jump,
    player_index,
    screen,
    player_walk,
    player_jump_surface,
    player_rectangle,
):
    if can_jump == True:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        screen.blit(player_walk[int(player_index)], player_rectangle)
    else:
        screen.blit(player_jump_surface, player_rectangle)
    return player_index


def snail():
    surface = image.load("./Assets/graphics/snail/snail1.png").convert_alpha()
    position = [randint(900, 1000), 232]
    rectangle = surface.get_rect(midbottom=(position))
    return surface, rectangle


def fly():
    surface = image.load("./Assets/graphics/Fly/Fly1.png").convert_alpha()
    position = [randint(900, 1000), 140]
    rectangle = surface.get_rect(midbottom=(position))
    return surface, rectangle
