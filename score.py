# Create the Text surface with the Score
def display_score(game_font):
    # Display the score
    text = "Score:"
    color = "Black"
    antialising = False
    position = (400, 30)
    surface = game_font.render(text, antialising, color)
    rectangle = surface.get_rect(center=(position))
    return surface, rectangle
