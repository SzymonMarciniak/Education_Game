import pygame
import pygame_gui

from static import *
from utils import * 
from start_screen import start_front

pygame.init()
pygame.font.init()
pygame.display.set_caption('Education Game')

def refresh_start_screen():
    global play_button, camera_button, leaderboard_button, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, settings_image_rect, settings_image

    play_button, camera_button, leaderboard_button, manager, background, \
            screen_w, screen_h, main_text, exit_image_rect, exit_image, settings_image_rect, settings_image = start_front(screen)

refresh_start_screen() #Build start screen


running = True
while running:
    screen.fill(BLACK)
    screen.blit(background, (0,0))

    screen.blit(main_text[0], main_text[1])
    screen.blit(exit_image, exit_image_rect)
    screen.blit(settings_image, settings_image_rect)

    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN: #On key down
            if event.key == pygame.K_f:
                if is_fullscreen():
                    change_fullscreen() 
                    screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
                    refresh_start_screen()
                else:
                    change_fullscreen() 
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    refresh_start_screen()
                    
        if event.type == pygame.USEREVENT: #On user event
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    print('Play!')
                if event.ui_element == camera_button:
                    print('Camera setup!')
                if event.ui_element == leaderboard_button:
                    print('Leaderboard!')

        if event.type == pygame.MOUSEBUTTONDOWN: #If clicked on image
            if exit_image_rect.collidepoint(event.pos):
                running = False
            if settings_image_rect.collidepoint(event.pos):
                print("Open settings")
    
        manager.process_events(event)
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()