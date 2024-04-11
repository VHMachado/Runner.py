from pygame import image, time
from texts import display_menu_text


def display_scenario(screen):
    sky_surface = image.load("./Assets/graphics/Sky.png").convert()
    screen.blit(sky_surface, get_sky_position())

    ground_surface = image.load("./Assets/graphics/ground.png").convert()
    screen.blit(ground_surface, get_ground_position())


def get_ground_position():
    return (0, 232)


def get_sky_position():
    return (0, 0)


def display_menu(
    screen,
    player_stand_surface,
    player_stand_rectangle,
):
    screen.fill((94, 129, 162))
    screen.blit(player_stand_surface, player_stand_rectangle)
    display_menu_text(screen)
    timer = time.get_ticks()
    return timer
