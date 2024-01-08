from pygame import image


def snail():
    surface = image.load("./Assets/graphics/snail/snail1.png").convert_alpha()
    position = [720, 232]
    rectangle = surface.get_rect(midbottom=(position))
    return surface, rectangle
