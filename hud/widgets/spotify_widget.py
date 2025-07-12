# hud/widgets/spotify_widget.py
# Widget Spotify (simulasi)

import pygame

def draw_spotify(screen):
    font = pygame.font.SysFont('Arial', 16)
    song = "Now Playing: Dream On - Aerosmith"
    text = font.render(song, True, (0, 255, 0))
    screen.blit(text, (10, 40))
