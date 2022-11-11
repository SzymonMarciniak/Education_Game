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

current_screen = 1
current_screen_dict ={ #if you substract key-10 you go to the previous page
    1: "start_screen",
    11: "play_screen",
    12: "camera_setup_screen",
    13: "leaderboard_screen",
    21: "classes_screen",
    31: "levels_screen",
    41: "game_screen",
    100: "settings_screen" #exception
}

choosen_category = None
choosen_class = None
buttons = []
digits_rect = []
digits_id = []


