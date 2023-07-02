import pygame
import config as cfg
import input as inp

def mainMenu(window):
    

    images = {
        "play_Up": pygame.image.load("gameSprites/play_Up.png"),
        "play_Down": pygame.image.load("gameSprites/play_Down.png")
    }
    images["play_Up"] = pygame.transform.scale(images["play_Up"], (int(images["play_Up"].get_width() * 8), int(images["play_Up"].get_height() * 8)))
    images["play_Down"] = pygame.transform.scale(images["play_Down"], (int(images["play_Down"].get_width() * 8), int(images["play_Down"].get_height() * 8)))

    while True:
        renderMainMenu(window, images)
        pygame.display.flip()
        inp.handleMainMenuInput()


def renderMainMenu(window, images):
    pygame.event.pump()
    window.fill((255, 97, 91))

    if(pygame.mouse.get_pressed()[0]):
        pygame.Surface.blit(window, images["play_Down"], ((cfg.play_x/100)*cfg.resolution_width - images["play_Down"].get_width()/2, (cfg.play_y/100)*cfg.resolution_height - images["play_Down"].get_height()/2))
    else:
        pygame.Surface.blit(window, images["play_Up"], ((cfg.play_x/100)*cfg.resolution_width - images["play_Down"].get_width()/2, (cfg.play_y/100)*cfg.resolution_height - images["play_Down"].get_height()/2))
