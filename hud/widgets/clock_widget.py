# hud/widgets/clock_widget.py
# Widget waktu dan tanggal

import pygame
import time

def draw_clock(screen):
    font = pygame.font.SysFont('Arial', 20)
    now = time.strftime("%H:%M:%S")
    text = font.render(now, True, (255, 255, 255))
    screen.blit(text, (10, 10))
