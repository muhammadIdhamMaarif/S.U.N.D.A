# hud/hud_renderer.py
# Modul utama untuk menampilkan data HUD ke layar AR/OLED

import pygame
import time
from hud.widgets.clock_widget import draw_clock
from hud.widgets.spotify_widget import draw_spotify
from hud.widgets.notification_widget import draw_notification

def start_hud():
    pygame.init()
    screen = pygame.display.set_mode((320, 240))
    pygame.display.set_caption("Helmet HUD")

    clock = pygame.time.Clock()

    while True:
        screen.fill((0, 0, 0))  # Layar hitam

        draw_clock(screen)
        draw_spotify(screen)
        draw_notification(screen)

        pygame.display.update()
        clock.tick(30)
