import pygame
def scale_to(object, new_size=(800,600)):
    object = pygame.transform.scale(object, new_size)
    return object

def set_text(string, coordx, coordy, fontSize, color=(0,0,0)): 
    font = pygame.font.Font('fonts/bungee-regular.ttf', fontSize) 
    text = font.render(string, True, color) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)

def clear_front(object):
    object.kill()