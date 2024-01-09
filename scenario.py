from pygame import image


def display_scenario(screen):
    sky_surface = image.load("./Assets/graphics/Sky.png").convert()
    screen.blit(sky_surface, get_sky_position())

    ground_surface = image.load("./Assets/graphics/ground.png").convert()
    screen.blit(ground_surface, get_ground_position())


def get_ground_position():
    return (0, 232)


def get_sky_position():
    return (0, 0)
