# Creates the loose text screen
def display_lose_screen(font, screen):
    text = "You Lose! Press SPACE to play again"
    antialising = False
    color = "Black"
    position = (400, 200)
    surface = font.render(text, antialising, color)
    rectangle = surface.get_rect(midbottom=(position))
    screen.blit(surface, rectangle)
