from pygame import font, time


def font_config():
    font_type = "./Assets/font/Pixeltype.ttf"
    font_size = 50
    game_font = font.Font(font_type, font_size)
    return game_font


def display_score(screen, timer):
    score = time.get_ticks() - timer
    font = font_config()
    text = f"Score: {score}"
    color = "Black"
    antialising = False
    position = (400, 30)
    surface = font.render(text, antialising, color)
    rectangle = surface.get_rect(center=(position))
    screen.blit(surface, rectangle)


def display_lose_screen(screen):
    font = font_config()
    text = "You Lose! Press SPACE to play again"
    antialising = False
    color = "Black"
    position = (400, 200)
    surface = font.render(text, antialising, color)
    rectangle = surface.get_rect(midbottom=(position))
    screen.blit(surface, rectangle)
