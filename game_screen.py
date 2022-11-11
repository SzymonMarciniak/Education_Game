import pygame 
import pygame_gui
import os 
import re
import random

from utils import set_text
from static import *

class StartGame:
    def __init__(self) -> None:
        self.available_place = [x for x in range(1,11)] 

    def build_front(self,screen):
        screen_w, screen_h = screen.get_width(), screen.get_height()
        digit_w, digit_h = (screen.get_width()/10) ,(screen.get_width()/10) #cube

        vw = screen_w/100
        vh = screen_h/100

        manager = pygame_gui.UIManager((screen_w, screen_h))
        
        background = pygame.image.load("images/background.png")
        background = pygame.transform.scale(background, (screen_w, screen_h))

        question_text_size = 50 if not is_fullscreen() else 100
        question_text = set_text("5 + 2", (screen_w/2), screen_h/9, question_text_size)
        solution = "7"

        path = "images"
        digits = os.listdir(path)
        digits_name = "number"
        digits = [digit for digit in digits if digits_name in digit]
        random.shuffle(digits)
        digits_btn = []
        for digit in digits:
            digit_img = pygame.image.load(f"{path}/{digit}")
            idx = re.search("\d", digit)
            ID = digit[int(idx.start())]
            digit_img = pygame.transform.scale(digit_img, (digit_w, digit_h))
            digits_id.append(ID)
            digits_btn.append(digit_img)
            digit_rect = digit_img.get_rect()
            self.set_xy_pos(digit_rect, new=True, y=screen_h+digit_h+100)
        
        return question_text, digits_btn
    
    def set_xy_pos(self, digit_rect, y=-(screen.get_width()/10), new=False):
        x_pos = random.choice(self.available_place)
        idx = self.available_place.index(x_pos)
        self.available_place.pop(idx)
        digit_rect.center = 75*x_pos, y
        if new:
            digits_rect.append(digit_rect)
        if len(self.available_place) == 0:
            self.available_place = [x for x in range(1,11)] 
 