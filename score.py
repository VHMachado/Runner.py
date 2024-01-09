def display_score(font, screen):
    text = "Score:"
    color = "Black"
    antialising = False
    position = (400, 30)
    surface = font.render(text, antialising, color)
    rectangle = surface.get_rect(center=(position))
    screen.blit(surface, rectangle)
