import pygame


def snail():
    snail_surface = pygame.image.load(
        "./Assets/graphics/snail/snail1.png"
    ).convert_alpha()
    snail_position = [720, 232]
    snail_rectangle = snail_surface.get_rect(midbottom=(snail_position))
    return snail_surface, snail_rectangle
