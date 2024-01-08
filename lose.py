# Creates the loose text screen
def lose_text(game_font):
    text = "You Lose! Press SPACE to play again"
    antialising = False
    color = "Black"
    position = (400, 200)
    surface = game_font.render(text, antialising, color)
    rectangle = surface.get_rect(midbottom=(position))
    return surface, rectangle
