import pygame


def player():
    player_suface = pygame.image.load(
        "./Assets/graphics/Player/player_walk_1.png"
    ).convert_alpha()
    player_position = [80, 232]
    player_rectangle = player_suface.get_rect(midbottom=(player_position))
    return player_suface, player_rectangle


def jump(player_position):
    player_position.y = -20


def fall(player_position, gravity):
    gravity += 1
    player_position.y += gravity
