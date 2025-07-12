# hud/widgets/notification_widget.py
# Widget notifikasi WhatsApp (simulasi)

import pygame

def draw_notification(screen):
    font = pygame.font.SysFont('Arial', 14)
    notif = "WhatsApp: 2 new messages"
    text = font.render(notif, True, (0, 180, 255))
    screen.blit(text, (10, 70))
