import pygame
import config as cfg


def mainMenu(window):

    # Load images for main menu
    images = {
        "play_Up": pygame.image.load("gameSprites/play_Up.png"),
        "play_Down": pygame.image.load("gameSprites/play_Down.png"),
        "option_Up": pygame.image.load("gameSprites/option_Up.png"),
        "option_Down": pygame.image.load("gameSprites/option_Down.png"),
        "quit_Up": pygame.image.load("gameSprites/quit_Up.png"),
        "quit_Down": pygame.image.load("gameSprites/quit_Down.png"),
    }

    # initialize button states
    btn_states = {
        "play": 0,
        "option": 0,
        "quit": 0
    }

    # Scale and transform images
    for image in images:
        images[image] = scaleImage(images[image], cfg.menu_scale)

    # Handle input and render main menu
    while True:
        handleMainMenuInput(images, btn_states)
        renderMainMenu(window, images, btn_states)
        pygame.display.flip()


def handleMainMenuInput(images, btn_states):

    if (mouseInBounds(images["play_Up"], cfg.play_x, cfg.play_y)):
        if (pygame.mouse.get_pressed()[0] == 0 and btn_states["play"] == 1):
            # Here to do stuff

            btn_states["play"] = 0
        elif (pygame.mouse.get_pressed()[0] == 1):
            btn_states["play"] = 1
        else:
            btn_states["play"] = 0
    
    if (mouseInBounds(images["option_Up"], cfg.option_x, cfg.option_y)):
        if (pygame.mouse.get_pressed()[0] == 0 and btn_states["option"] == 1):
            # Here to do stuff

            btn_states["option"] = 0
        elif (pygame.mouse.get_pressed()[0] == 1):
            btn_states["option"] = 1
        else:
            btn_states["option"] = 0

    if (mouseInBounds(images["quit_Up"], cfg.quit_x, cfg.quit_y)):
        if (pygame.mouse.get_pressed()[0] == 0 and btn_states["quit"] == 1):
            # Here to do stuff
            pygame.quit()
            exit()
            btn_states["quit"] = 0
        elif (pygame.mouse.get_pressed()[0] == 1):
            btn_states["quit"] = 1
        else:
            btn_states["quit"] = 0

def renderMainMenu(window, images, btn_states):
    pygame.event.pump()
    window.fill((255, 97, 91))

    if (btn_states["play"] == 1):
        window.blit(images["play_Down"], ((cfg.play_x/100)*cfg.resolution_width - images["play_Down"].get_width() /
                    2, (cfg.play_y/100)*cfg.resolution_height - images["play_Down"].get_height()/2))
    else:
        window.blit(images["play_Up"], ((cfg.play_x/100)*cfg.resolution_width - images["play_Up"].get_width() /
                    2, (cfg.play_y/100)*cfg.resolution_height - images["play_Up"].get_height()/2))

    if (btn_states["option"] == 1):
        window.blit(images["option_Down"], ((cfg.option_x/100)*cfg.resolution_width - images["option_Down"].get_width() /
                    2, (cfg.option_y/100)*cfg.resolution_height - images["option_Down"].get_height()/2))
    else:
        window.blit(images["option_Up"], ((cfg.option_x/100)*cfg.resolution_width - images["option_Up"].get_width() /
                    2, (cfg.option_y/100)*cfg.resolution_height - images["option_Up"].get_height()/2))

    if (btn_states["quit"] == 1):
        window.blit(images["quit_Down"], ((cfg.quit_x/100)*cfg.resolution_width - images["quit_Down"].get_width() /
                    2, (cfg.quit_y/100)*cfg.resolution_height - images["quit_Down"].get_height()/2))
    else:
        window.blit(images["quit_Up"], ((cfg.quit_x/100)*cfg.resolution_width - images["quit_Up"].get_width() /
                    2, (cfg.quit_y/100)*cfg.resolution_height - images["quit_Up"].get_height()/2))

# ---------------------------------------------------------------------
# Option Menu

# ---------------------------------------------------------------------
# Functions useful to all menus


def scaleImage(image, scale):
    return pygame.transform.scale(image, (int(image.get_width()*scale), int(image.get_height()*scale)))


# checks if mouse is in bounds of image at x, y position
def mouseInBounds(image, x, y):
    mouse_pos = pygame.mouse.get_pos()

    if (mouse_pos[0] > (x/100)*cfg.resolution_width - image.get_width()/2 and mouse_pos[0] < (x/100)*cfg.resolution_width + image.get_width()/2):
        if (mouse_pos[1] > (y/100)*cfg.resolution_height - image.get_height()/2 and mouse_pos[1] < (y/100)*cfg.resolution_height + image.get_height()/2):
            return True
    return False
