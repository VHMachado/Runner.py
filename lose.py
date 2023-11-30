# Creates the loose text screen
def lose_text(game_font):
    text = "You Lose!"
    text_antialising = False
    text_color = "Black"
    text_position = (400, 200)
    text_surface = game_font.render(text, text_antialising, text_color)
    text_rectangle = text_surface.get_rect(midbottom=(text_position))
    return text_surface, text_rectangle
