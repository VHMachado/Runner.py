# Create the Text surface with the Score
def display_score(game_font):
    text = "Score = "
    text_antialising = False
    text_color = "Black"
    text_position = (400, 30)
    text_surface = game_font.render(text, text_antialising, text_color)
    text_rectangle = text_surface.get_rect(center=(text_position))
    return text_surface, text_rectangle
