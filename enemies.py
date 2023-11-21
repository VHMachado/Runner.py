import pygame


def snail():
    snail_surface = pygame.image.load(
        "./Assets/graphics/snail/snail1.png"
    ).convert_alpha()
    snail_position = [600, 200]
    return snail_surface, snail_position
