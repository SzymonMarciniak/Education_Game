import pygame
import pygame_gui
import time 
import subprocess

from static import *
from utils import * 
from start_screen import StartScreen
from play_screen import PlayScreen
from choose_class import ChooseClass
from levels_screen import LevelsScreen 
from game_screen import StartGame
from minigames.math_games import Mathematic

start_screen = StartScreen()
play_screen = PlayScreen()
class_screen = ChooseClass()
levels_screen = LevelsScreen()
game_screen = StartGame()
math_games = Mathematic()

pygame.init()
pygame.font.init()
pygame.display.set_caption('Education Game')

last_time = 0
queue = []
camera_setup_open = False 
def build_proper_images():
    if current_screen_dict[current_screen] == "start_screen":
        screen.blit(main_text[0], main_text[1])
        screen.blit(exit_image, exit_image_rect)
        screen.blit(settings_image, settings_image_rect)
    
    elif (current_screen_dict[current_screen] == "play_screen") or (current_screen_dict[current_screen] == "classes_screen") \
        or (current_screen_dict[current_screen] == "levels_screen"):
        screen.blit(main_text[0], main_text[1])
        screen.blit(settings_image, settings_image_rect)
        screen.blit(exit_image, exit_image_rect)
    
    elif current_screen_dict[current_screen] == "game_screen":
        global last_time, queue
        queue = math_games.refresh_digits(screen, digits_btn, screen_h, queue)

        screen.blit(question_text[0], question_text[1])
        screen.blit(points_text[0], points_text[1])
        
            

def build_start_screen(screen):
    global play_button, camera_button, leaderboard_button, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, settings_image_rect, settings_image

    play_button, camera_button, leaderboard_button, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, settings_image_rect, settings_image = start_screen.start_front(screen)
build_start_screen(screen) 

def build_play_screen(screen):
    global math_button, polish_button, english_button, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, settings_image_rect, settings_image
            
    math_button, polish_button, english_button, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, \
            settings_image_rect, settings_image = play_screen.start_front(screen)

def build_class_screen(screen):
    global class1_button, class2_button, class3_button, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, settings_image_rect, settings_image

    class1_button, class2_button, class3_button, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, settings_image_rect, settings_image = class_screen.build_front(screen)

def build_levels_screen(screen):
    global levels_buttons, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, settings_image_rect, settings_image

    levels_buttons, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, settings_image_rect, settings_image = levels_screen.build_front(screen)

def build_game_screen(screen):
    global question_text, digits_btn, points_text, first_solution
    first_question, solution = math_games.get_questions(choosen_class, choosen_lvl)[1]
    first_solution = str(solution)
    question_text, points_text, digits_btn = game_screen.build_front(screen, first_question) 
    

def build_proper_widgets(screen):
    for button in buttons:
        try:
            clear_front(button)
        except: print(button) 
    buttons.clear()

    if current_screen_dict[current_screen] == "start_screen":
        build_start_screen(screen)
    elif current_screen_dict[current_screen] == "play_screen":
        build_play_screen(screen)
    elif current_screen_dict[current_screen] == "classes_screen":
        build_class_screen(screen)
    elif current_screen_dict[current_screen] == "levels_screen":
        build_levels_screen(screen) 
    elif current_screen_dict[current_screen] == "game_screen":
        build_game_screen(screen)

running = True
while running: #Main loop
    screen.fill(BLACK)
    screen.blit(background, (0,0))

    build_proper_images()

    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN: #On key down
            if event.key == pygame.K_f:
                if is_fullscreen():
                    change_fullscreen() 
                    screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
                    build_proper_widgets(screen)
                else:
                    change_fullscreen() 
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    build_proper_widgets(screen)
                    
        if event.type == pygame.USEREVENT: #On user event
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                if event.ui_element == play_button:
                    current_screen = 11
                elif event.ui_element == camera_button:
                    if not camera_setup_open: #cso to db
                        subprocess.Popen(["python", "camera_setup/camera.py", "1"])
                        camera_setup_open = True
                    
                elif event.ui_element == leaderboard_button:
                    print('Leaderboard!')

                elif event.ui_element == math_button:
                    current_screen = 21
                    choosen_category = "math"
                elif event.ui_element == english_button:
                    current_screen = 21
                    choosen_category = "english"
                elif event.ui_element == polish_button:
                    current_screen = 21
                    choosen_category = "polish"

                elif event.ui_element == class1_button:
                    current_screen = 31
                    choosen_class = 1
                elif event.ui_element == class2_button:
                    current_screen = 31
                    choosen_class = 2
                elif event.ui_element == class3_button:
                    current_screen = 31
                    choosen_class = 3

                elif event.ui_element in levels_buttons:
                    choosen_lvl = event.ui_element.text
                    print(f"Przycisk nr: {choosen_lvl} --- kategoria: {choosen_category} --- klasa: {choosen_class}")
                    current_screen = 41
                build_proper_widgets(screen)

        if event.type == pygame.MOUSEBUTTONDOWN: #If clicked on image
            if exit_image_rect.collidepoint(event.pos):
                if current_screen_dict[current_screen] != "game_screen":
                    if current_screen_dict[current_screen] == "start_screen":
                        running = False
                    else: 
                        current_screen -= 10
                        build_proper_widgets(screen)
            if settings_image_rect.collidepoint(event.pos):
                if current_screen_dict[current_screen] != "game_screen":
                    print("Open settings")
            
            if current_screen_dict[current_screen] == "game_screen":
                if choosen_category == "math":
                    if solution == None: solution = first_solution
                    question_text, solution, points = math_games.selecting_digit(screen, event, game_screen, screen_h, question_text, solution, points)


                    vw = screen_w/100
                    points_text_size = 40 if not is_fullscreen() else 80
                    points_text = set_text(str(points), 3*vw, 3*vw, points_text_size)
    
        manager.process_events(event)
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.update()

pygame.quit()