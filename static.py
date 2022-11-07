import pygame

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()

FULLSCREEN = False

BLACK = 0,0,0
ORANGE = 255,127,0
RED = 255,0,0
GREEN = 0,255,0

def change_fullscreen():
    global FULLSCREEN
    FULLSCREEN = not FULLSCREEN

def is_fullscreen():
    return FULLSCREEN

background = pygame.image.load("images/background.png")
exit_image = pygame.image.load("images/exit_button.png")
settings_image = pygame.image.load("images/settings_button.png")

