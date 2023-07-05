import pygame
import config as cfg

# ---------------------------------------------------------------------
# Menus Initialization
# ---------------------------------------------------------------------

def menuInit():

    def percentToPos(percent, axis):
        if axis == "x":
            return int(percent * cfg.resolution_width / 100)
        elif axis == "y":
            return int(percent * cfg.resolution_height / 100)

    # Button data is stored like this: [up image, down image, state, x, y]
    menuVars = {
        "btnsMM": [
            { 
                "images" : (scaleImage(pygame.image.load("gameSprites/play_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("gameSprites/play_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.play_x, "x"), percentToPos(cfg.play_y, "y")),
                "active" : True,
            },
            {
                "images" : (scaleImage(pygame.image.load("gameSprites/option_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("gameSprites/option_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.option_x, "x"), percentToPos(cfg.option_y, "y")),
                "active" : True,
            },
            {
                "images" : (scaleImage(pygame.image.load("gameSprites/quit_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("gameSprites/quit_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.quit_x, "x"), percentToPos(cfg.quit_y, "y")),
                "active" : True,
            },
        ],

        "btnsOM": [
            {
                "images" : (scaleImage(pygame.image.load("gameSprites/back_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("gameSprites/back_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.back_x, "x"), percentToPos(cfg.back_y, "y")),
                "active" : True,
            },
            {
                "images" : (scaleImage(pygame.image.load("gameSprites/mute_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("gameSprites/mute_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.mute_x, "x"), percentToPos(cfg.mute_y, "y")),
                "active" : True,
            },
            {
                "images" : (scaleImage(pygame.image.load("gameSprites/unmute_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("gameSprites/unMute_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.mute_x, "x"), percentToPos(cfg.mute_y, "y")),
                "active" : False,
            },
        ],
    }
    return menuVars


# ---------------------------------------------------------------------
# Main Menu
# ---------------------------------------------------------------------

def mainMenu(window, menuVars):
    # Handle input and render main menu
    while True:
        handleMainMenuInput(window, menuVars)
        renderMainMenu(window, menuVars)
        pygame.display.flip()


def handleMainMenuInput(window, menuVars):
    # Play Button
    handleBtnState(menuVars["btnsMM"][0])
    # Option Button
    handleBtnState(menuVars["btnsMM"][1], lambda: optionMenu(window, menuVars))
    # Quit Button
    handleBtnState(menuVars["btnsMM"][2], lambda: (pygame.quit(), exit()))

def renderMainMenu(window, menuVars):
    # Pump events for windows
    pygame.event.pump()
    window.fill((255, 97, 91))
    
    playImg = menuVars["btnsMM"][0]["images"][menuVars["btnsMM"][0]["state"]]
    optionImg = menuVars["btnsMM"][1]["images"][menuVars["btnsMM"][1]["state"]]
    quitImg = menuVars["btnsMM"][2]["images"][menuVars["btnsMM"][2]["state"]]

    window.blit(playImg, (menuVars["btnsMM"][0]["pos"][0] - playImg.get_width()/2, menuVars["btnsMM"][0]["pos"][1] - playImg.get_height()/2))
    window.blit(optionImg, (menuVars["btnsMM"][1]["pos"][0] - optionImg.get_width()/2, menuVars["btnsMM"][1]["pos"][1] - optionImg.get_height()/2))
    window.blit(quitImg, (menuVars["btnsMM"][2]["pos"][0] - quitImg.get_width()/2, menuVars["btnsMM"][2]["pos"][1] - quitImg.get_height()/2))

# ---------------------------------------------------------------------
# Option Menu
# ---------------------------------------------------------------------

def optionMenu(window, menuVars):
    # Handle input and render main menu
    while True:
        handleOptionMenuInput(window, menuVars)
        renderOptionMenu(window, menuVars)
        pygame.display.flip()


def handleOptionMenuInput(window, menuVars):
    handleBtnState(menuVars["btnsOM"][0], lambda: mainMenu(window, menuVars))


def renderOptionMenu(window, menuVars):
    # Pump events for windows
    pygame.event.pump()
    window.fill((255, 97, 91))
    
    backImg = menuVars["btnsOM"][0]["images"][menuVars["btnsOM"][0]["state"]]

    window.blit(backImg, (menuVars["btnsOM"][0]["pos"][0] - backImg.get_width()/2, menuVars["btnsOM"][0]["pos"][1] - backImg.get_height()/2))




def switchMuteBtnStates(menuVars):
    if (menuVars["btnsOM"][1]["active"]):
        menuVars["btnsOM"][1]["active"] = False
        menuVars["btnsOM"][2]["active"] = True
    else:
        menuVars["btnsOM"][1]["active"] = True
        menuVars["btnsOM"][2]["active"] = False



# ---------------------------------------------------------------------
# Functions useful to all menus


def scaleImage(image, scale):
    return pygame.transform.scale(image, (int(image.get_width()*scale), int(image.get_height()*scale)))


# checks if mouse is in bounds of image at x, y position
def mouseInBounds(image, pos):
    mouse_pos = pygame.mouse.get_pos()

    if (mouse_pos[0] > pos[0] - image.get_width()/2 and mouse_pos[0] < pos[0] + image.get_width()/2):
        if (mouse_pos[1] > pos[1] - image.get_height()/2 and mouse_pos[1] < pos[1] + image.get_height()/2):
            return True
    return False

# Handles button state
def handleBtnState(btnInfo, function = None):
    if (mouseInBounds(btnInfo["images"][0], btnInfo["pos"])):
        if (pygame.mouse.get_pressed()[0] == 0 and btnInfo["state"] == 1):
            # Here to do stuff
            if function:
                function()
            btnInfo["state"] = 0
        elif (pygame.mouse.get_pressed()[0] == 1):
            btnInfo["state"] = 1
    else:
        btnInfo["state"] = 0    if(btnInfo["active"] == False):
        pass
    else:
        image = btnInfo["images"][btnInfo["state"]]
        window.blit(image, (btnInfo["pos"][0] - image.get_width()/2, btnInfo["pos"][1] - image.get_height()/2))