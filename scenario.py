from pygame import image


def display_scenario(screen):
    sky_surface = image.load("./Assets/graphics/Sky.png").convert()
    sky_position = (0, 0)
    screen.blit(sky_surface, sky_position)

    ground_surface = image.load("./Assets/graphics/ground.png").convert()
    ground_position = (0, 232)
    screen.blit(ground_surface, ground_position)


def get_ground_position():
    return (0, 232)
