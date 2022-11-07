import pygame
import pygame_gui

from utils import set_text
from static import *

class PlayScreen:
    def __init__(self) -> None:
        pass 

    def start_front(self,screen):
        screen_w, screen_h = screen.get_width(), screen.get_height()
        button_w, button_h = (screen.get_width()/3) ,(screen.get_height()/11)

        vw = screen_w/100
        
        background = pygame.image.load("images/background.png")
        background = pygame.transform.scale(background, (screen_w, screen_h))

        main_text_size = 50 if not is_fullscreen() else 100
        main_text = set_text("Education Game", (screen_w/2), screen_h/9, main_text_size)

        manager = pygame_gui.UIManager((screen_w, screen_h))
        math_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((screen_w/2)-(button_w/2), (screen_h/2)-(button_h)), (button_w, button_h)),
                                                    text='Matematyka',manager=manager)

        polish_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((screen_w/2)-(button_w/2), (screen_h/2)+(button_h/2)), (button_w, button_h)),
                                                    text='Polski',manager=manager)

        english_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((screen_w/2)-(button_w/2), (screen_h/2)+(button_h*2)), (button_w, button_h)),
                                                    text='Angielski', manager=manager) 
                                                    
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

        return math_button, polish_button, english_button, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, settings_image_rect, settings_image
    
    def clear_front(self, *objects):
        for object in objects:
            object.kill()