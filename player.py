import pygame


def player():
    player_suface = pygame.image.load(
        "./Assets/graphics/Player/player_walk_1.png"
    ).convert_alpha()
    player_position = [80, 148]
    player_rectangle = player_suface.get_rect()
    return player_suface, player_position
