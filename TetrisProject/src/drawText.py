
import pygame

def drawText(text, size, color, surface):
    return pygame.font.SysFont('comicsans', size).render(text, 1, color)