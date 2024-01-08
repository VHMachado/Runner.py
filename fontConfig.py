from pygame import font


# Set the font that is going to be used to display text
def font_config():
    font_type = "./Assets/font/Pixeltype.ttf"
    font_size = 50
    game_font = font.Font(font_type, font_size)
    return game_font
