from pygame import image, transform
from random import randint


def player_stand():
    surface = image.load("./Assets/graphics/Player/player_stand.png").convert_alpha()
    surface = transform.scale2x(surface)
    position = [400, 200]
    rectangle = surface.get_rect(center=position)
    return surface, rectangle


def player_walk_1():
    surface = image.load("./Assets/graphics/Player/player_walk_1.png").convert_alpha()
    position = [80, 232]
    rectangle = surface.get_rect(midbottom=(position))
    return surface, rectangle


def snail():
    surface = image.load("./Assets/graphics/snail/snail1.png").convert_alpha()
    position = [randint(900, 1000), 232]
    rectangle = surface.get_rect(midbottom=(position))
    return surface, rectangle
