import pygame
import pygame_gui

from static import *
from utils import * 
from start_screen import StartScreen
from play_screen import PlayScreen

start_screen = StartScreen()
play_screen = PlayScreen()

pygame.init()
pygame.font.init()
pygame.display.set_caption('Education Game')

def build_proper_images():
    if current_screen_dict[current_screen] == "start_screen":
        screen.blit(main_text[0], main_text[1])
        screen.blit(exit_image, exit_image_rect)
        screen.blit(settings_image, settings_image_rect)

    elif current_screen_dict[current_screen] == "play_screen":
        screen.blit(main_text[0], main_text[1])
        screen.blit(settings_image, settings_image_rect)
        screen.blit(exit_image, exit_image_rect)

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

def build_proper_widgets(screen):
    start_screen.clear_front(camera_button, leaderboard_button, play_button)
    try:
        play_screen.clear_front(math_button, polish_button, english_button)
    except: pass
    if current_screen_dict[current_screen] == "start_screen":
        build_start_screen(screen)
    elif current_screen_dict[current_screen] == "play_screen":
        build_play_screen(screen)

running = True
while running:
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
                    current_screen = 2
                    build_play_screen(screen)
                if event.ui_element == camera_button:
                    print('Camera setup!')
                if event.ui_element == leaderboard_button:
                    print('Leaderboard!')
                if event.ui_element == math_button:
                    print('Math!')
                if event.ui_element == english_button:
                    print('English!')
                if event.ui_element == polish_button:
                    print('Polish!')

        if event.type == pygame.MOUSEBUTTONDOWN: #If clicked on image
            if exit_image_rect.collidepoint(event.pos):
                if current_screen_dict[current_screen] == "start_screen":
                    running = False
                else: 
                    current_screen -= 1
                    build_proper_widgets(screen)
            if settings_image_rect.collidepoint(event.pos):
                print("Open settings")
    
        manager.process_events(event)
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.update()

pygame.quit()