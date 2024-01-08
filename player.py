import pygame


def player():
    surface = pygame.image.load(
        "./Assets/graphics/Player/player_walk_1.png"
    ).convert_alpha()
    position = [80, 232]
    rectangle = surface.get_rect(midbottom=(position))
    return surface, rectangle
