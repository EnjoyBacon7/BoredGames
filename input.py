import pygame
import config as cfg

def handleMainMenuInput():
    if(pygame.mouse.get_pressed()[0]):
        #Play button
        if(pygame.mouse.get_pos()[0] > percentToPixel(cfg.play_x, 0) - cfg.play_width/2 and pygame.mouse.get_pos()[0] < percentToPixel(cfg.play_x, 0) + cfg.play_width/2):
            if(pygame.mouse.get_pos()[1] > percentToPixel(cfg.play_y, 1) - cfg.play_height/2 and pygame.mouse.get_pos()[1] < percentToPixel(cfg.play_y, 1) + cfg.play_height/2):
                return "play"


def handleOptionsMenuInput():
    x = 1

def percentToPixel(percent, axis):
    if(axis == 0):
        return (percent/100)*cfg.resolution_width
    elif(axis == 1):
        return (percent/100)*cfg.resolution_height
    else:
        return -1