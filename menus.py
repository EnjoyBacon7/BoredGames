import pygame
import config as cfg


def mainMenu(window):

    # Load images for main menu
    images = {
        "play": [pygame.image.load("gameSprites/play_Up.png"), pygame.image.load("gameSprites/play_Down.png")],
        "option": [pygame.image.load("gameSprites/option_Up.png"), pygame.image.load("gameSprites/option_Down.png")],
        "quit": [pygame.image.load("gameSprites/quit_Up.png"), pygame.image.load("gameSprites/quit_Down.png")]
    }

    # initialize button states
    btn_states = {
        "play": 0,
        "option": 0,
        "quit": 0
    }

    # Scale and transform images
    for image in images:
        images[image][0] = scaleImage(images[image][0], cfg.menu_scale)
        images[image][1] = scaleImage(images[image][1], cfg.menu_scale)

    # Handle input and render main menu
    while True:
        handleMainMenuInput(window, images, btn_states)
        renderMainMenu(window, images, btn_states)
        pygame.display.flip()


def handleMainMenuInput(window, images, btn_states):

    if (mouseInBounds(images["play"][0], cfg.play_x, cfg.play_y)):
        if (pygame.mouse.get_pressed()[0] == 0 and btn_states["play"] == 1):
            # Here to do stuff

            btn_states["play"] = 0
        elif (pygame.mouse.get_pressed()[0] == 1):
            btn_states["play"] = 1
    else:
        btn_states["play"] = 0
    
    if (mouseInBounds(images["option"][0], cfg.option_x, cfg.option_y)):
        if (pygame.mouse.get_pressed()[0] == 0 and btn_states["option"] == 1):
            # Here to do stuff
            optionMenu(window)

            btn_states["option"] = 0
        elif (pygame.mouse.get_pressed()[0] == 1):
            btn_states["option"] = 1
    else:
        btn_states["option"] = 0

    if (mouseInBounds(images["quit"][0], cfg.quit_x, cfg.quit_y)):
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
    # Pump events for windows
    pygame.event.pump()
    window.fill((255, 97, 91))
    
    playImg = images["play"][btn_states["play"]]
    optionImg = images["option"][btn_states["option"]]
    quitImg = images["quit"][btn_states["quit"]]

    window.blit(playImg, (cfg.play_x - playImg.get_width()/2, cfg.play_y - playImg.get_height()/2))
    window.blit(optionImg, (cfg.option_x - optionImg.get_width()/2, cfg.option_y - optionImg.get_height()/2))
    window.blit(quitImg, (cfg.quit_x - quitImg.get_width()/2, cfg.quit_y - quitImg.get_height()/2))

# ---------------------------------------------------------------------
# Option Menu

def optionMenu(window):

    # Load images for main menu
    images = {
        "back": [pygame.image.load("gameSprites/back_Up.png"), pygame.image.load("gameSprites/back_Down.png")],
    }

    # initialize button states
    btn_states = {
        "back": 0
    }

    # Scale and transform images
    for image in images:
        images[image][0] = scaleImage(images[image][0], cfg.menu_scale)
        images[image][1] = scaleImage(images[image][1], cfg.menu_scale)

    # Handle input and render main menu
    back = False
    while not back:
        back = handleOptionMenuInput(images, btn_states)
        renderOptionMenu(window, images, btn_states)
        pygame.display.flip()


def handleOptionMenuInput(images, btn_states):

    if (mouseInBounds(images["back"][0], cfg.back_x, cfg.back_y)):
        if (pygame.mouse.get_pressed()[0] == 0 and btn_states["back"] == 1):
            # Here to do stuff
            return True
            btn_states["back"] = 0
        elif (pygame.mouse.get_pressed()[0] == 1):
            btn_states["back"] = 1
    else:
        btn_states["back"] = 0

def renderOptionMenu(window, images, btn_states):
    # Pump events for windows
    pygame.event.pump()
    window.fill((255, 97, 91))
    
    backImg = images["back"][btn_states["back"]]

    window.blit(backImg, (cfg.back_x - backImg.get_width() /2, cfg.back_y - backImg.get_height()/2))

# ---------------------------------------------------------------------
# Functions useful to all menus


def scaleImage(image, scale):
    return pygame.transform.scale(image, (int(image.get_width()*scale), int(image.get_height()*scale)))


# checks if mouse is in bounds of image at x, y position
def mouseInBounds(image, x, y):
    mouse_pos = pygame.mouse.get_pos()

    if (mouse_pos[0] > x - image.get_width()/2 and mouse_pos[0] < x + image.get_width()/2):
        if (mouse_pos[1] > y - image.get_height()/2 and mouse_pos[1] < y + image.get_height()/2):
            return True
    return False
