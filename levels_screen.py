import pygame 
import pygame_gui

from utils import set_text
from static import *

class LevelsScreen:
    def __init__(self) -> None:
        self.if_first_time() 

    @classmethod
    def if_first_time(self):
        self.first_time = True 

    def build_front(self, screen):
        screen_w, screen_h = screen.get_width(), screen.get_height()
        button_w, button_h = (screen.get_width()/15) ,(screen.get_width()/15) #cube

        vw = screen_w/100
        vh = screen_h/100
        
        background = pygame.image.load("images/background.png")
        background = pygame.transform.scale(background, (screen_w, screen_h))

        main_text_size = 50 if not is_fullscreen() else 100
        main_text = set_text("Education Game", (screen_w/2), screen_h/9, main_text_size)

        manager = pygame_gui.UIManager((screen_w, screen_h))

        levels_buttons = []

        entire_width = screen_w-(24*vw)
        free_width = entire_width - 8*button_w
        space_x = free_width/7

        entire_heigth = screen_h - screen_h/3 - 15*vh
        free_height = entire_heigth - 4*button_h
        space_y = free_height/3

        w = -1
        pos_y = screen_h/3
        for i in range(1,33):
            w += 1
            if ((i-1) % 8 == 0) and (i-1!=0):
                pos_y += button_h + space_y
                w = 0
            pos_x = (12*vw + w*(button_w+space_x))
            button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((pos_x, pos_y)), (button_w, button_h)),
                                                    text=str(i),manager=manager)
            levels_buttons.append(button)
                                                    
        exit_image = pygame.image.load("images/return_button.png")
        settings_image = pygame.image.load("images/settings_button.png")

        btns_pos = 4
        if not is_fullscreen():
            exit_image = pygame.transform.scale(exit_image, (8*vw, 8*vw))
            settings_image = pygame.transform.scale(settings_image, (8*vw, 8*vw))
            btns_pos = 6

        exit_image_rect = exit_image.get_rect()
        exit_image_rect.center = btns_pos*vw, screen_h - btns_pos*vw

        settings_image_rect = settings_image.get_rect()
        settings_image_rect.center = screen_w - btns_pos*vw, screen_h - btns_pos*vw

        for btn in levels_buttons:
            buttons.append(btn)

        return levels_buttons, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, settings_image_rect, settings_image
        
    def clear_front(self, *objects):
        for object in objects:
            object.kill()