import json 
import time
import random

from static import *
from utils import set_text
from game_screen import StartGame

game_screen = StartGame()




class Mathematic:
    def __init__(self) -> None:
        self.last_time = 0 

        choosen_class = 1
        with open(f"questions/class{choosen_class}_math.json") as f:
            self.class_1_db = json.load(f)

        self.questions = {}
        self.actual_question = 0

        

    def selecting_digit(self, screen, event, game_screen, screen_h, question_text, solution, points):
        for nr, digit in enumerate(digits_rect):
            if digit.collidepoint(event.pos): 
                print(f"You clicked digit: {digits_id[nr]}")
                digit.center = 0, screen_h + (screen.get_width()/10) + 100
                if str(digits_id[nr]) == solution:
                    points += 1
                    new_question_text, solution = self.new_question()
                    return new_question_text, solution,  points
                else:
                    if points != -9:
                        points -= 1
        return question_text, solution, points
    
    def refresh_digits(self, screen, digits_btn, screen_h, queue):
        now = time.time()
        for nr, digit in enumerate(digits_btn):
            digict_rect = digits_rect[nr-1]
            previous_x, previous_y = digict_rect.center
            if previous_y > screen_h+screen.get_width()/16:
                if abs(self.last_time-now) > 1:
                    if digit not in queue:
                        previous_y = 0
                        game_screen.set_xy_pos(digict_rect)
                        self.last_time = time.time()
                        queue.append(digit)
                        if len(queue) == 10:
                            queue = []
            else:
                digict_rect.center = previous_x, previous_y+2
            screen.blit(digit, digits_rect[nr])
        return queue
    
    def get_questions(self, choosen_class, choosen_lvl):
        section = "sum" # substract / multiplication / less_more_the_same / days_weak1
        
        level_db = self.class_1_db["math"][f"class_{choosen_class}"][section][f"level_{choosen_lvl}"]["settings"]
        max_num = level_db["max_num"]
        min_num = level_db["min_num"]
        max_equal = level_db["max_equal"]

        self.questions.clear()
        self.actual_question = 0
        for i in range(1, 11):
            equal = random.randint(min_num, max_equal)
            print(min_num, equal)
            digit_a = random.randint(min_num, equal)
            digit_b = equal - digit_a
            self.questions.update({i: [f"{digit_a} + {digit_b}", equal]})
            print(self.questions)
        return self.questions

    
    def new_question(self):
        self.actual_question += 1
        my_set = self.questions[self.actual_question]
        quest, answer = my_set[0], my_set[1]
        solution = str(answer)
        screen_w, screen_h = screen.get_width(), screen.get_height()
        question_text_size = 50 if not is_fullscreen() else 100
        question_text = set_text(str(quest), (screen_w/2), screen_h/9, question_text_size)
        return question_text, solution
            