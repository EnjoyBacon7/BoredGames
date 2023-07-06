import pygame
import time

import clientSettings as cs
import config as cfg

from gameInit import gameInit
from gameLoop import gameLoop

# ---------------------------------------------------------------------
# Menus Initialization
# ---------------------------------------------------------------------

def menuInit():

    # Get absolute position from percentage
    def percentToPos(percent, axis):
        if axis == "x":
            return int(percent * cs.resolution_width / 100)
        elif axis == "y":
            return int(percent * cs.resolution_height / 100)

    # Button data is stored like this: [up image, down image, state, x, y]
    menuVars = {
        "btnsMM": [
            { 
                "images" : (scaleImage(pygame.image.load("Content/Images/play_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("Content/Images/play_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.play_x, "x"), percentToPos(cfg.play_y, "y")),
                "active" : True,
            },
            {
                "images" : (scaleImage(pygame.image.load("Content/Images/option_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("Content/Images/option_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.option_x, "x"), percentToPos(cfg.option_y, "y")),
                "active" : True,
            },
            {
                "images" : (scaleImage(pygame.image.load("Content/Images/quit_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("Content/Images/quit_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.quit_x, "x"), percentToPos(cfg.quit_y, "y")),
                "active" : True,
            },
        ],

        "btnsOM": [
            {
                "images" : (scaleImage(pygame.image.load("Content/Images/back_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("Content/Images/back_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.back_x, "x"), percentToPos(cfg.back_y, "y")),
                "active" : True,
            },
            # Mute button is toggle. It has two states, one for muted and one for unmuted.
            {
                "images" : (scaleImage(pygame.image.load("Content/Images/mute_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("Content/Images/mute_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.mute_x, "x"), percentToPos(cfg.mute_y, "y")),
                "active" : True,
            },
            {
                "images" : (scaleImage(pygame.image.load("Content/Images/unmute_Up.png"), cfg.menu_scale), scaleImage(pygame.image.load("Content/Images/unMute_Down.png"), cfg.menu_scale)),
                "state"  : 0,
                "pos"    : (percentToPos(cfg.mute_x, "x"), percentToPos(cfg.mute_y, "y")),
                "active" : False,
            },
        ],
        # Clock is used to set fps
        "clock" : pygame.time.Clock(),
    }
    return menuVars


# ---------------------------------------------------------------------
# Main Menu
# ---------------------------------------------------------------------

# Main Menu loop
def mainMenu(window, menuVars):
    # Handle input and render main menu
    while True:

        # Start frame timer
        start_time = time.perf_counter()

        # Menu functions
        handleMainMenuInput(window, menuVars)
        renderMainMenu(window, menuVars)
        pygame.display.flip()
        menuVars["clock"].tick(cs.fps)

        # End frame timer and print frame time
        end_time = time.perf_counter()
        frame_time = (end_time - start_time) * 1e3
        print(f"Frame time (MM): {frame_time:.2f} milliseconds")

# Handle clicks and button states
def handleMainMenuInput(window, menuVars):
    # Play Button
    handleBtnState(menuVars["btnsMM"][0], lambda: (gameLoop(window, gameInit())))
    # Option Button
    handleBtnState(menuVars["btnsMM"][1], lambda: optionMenu(window, menuVars))
    # Quit Button
    handleBtnState(menuVars["btnsMM"][2], lambda: (pygame.quit(), exit()))

# Render the menu using the button data
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

# Option Menu loop
def optionMenu(window, menuVars):
    # Handle input and render main menu
    while True:

        # Start frame timer
        start_time = time.perf_counter()

        # Menu functions
        handleOptionMenuInput(window, menuVars)
        renderOptionMenu(window, menuVars)
        pygame.display.flip()
        menuVars["clock"].tick(cs.fps)

        # End frame timer and print frame time
        end_time = time.perf_counter()
        frame_time = (end_time - start_time) * 1e3
        print(f"Frame time (OM): {frame_time:.2f} milliseconds")

# Handle clicks and button states
def handleOptionMenuInput(window, menuVars):
    handleBtnState(menuVars["btnsOM"][0], lambda: (mainMenu(window, menuVars)))
    handleBtnState(menuVars["btnsOM"][1], lambda: (switchMuteBtnStates(menuVars)))
    handleBtnState(menuVars["btnsOM"][2], lambda: (switchMuteBtnStates(menuVars)))

# Render the menu using the button data
def renderOptionMenu(window, menuVars):
    # Pump events for windows
    pygame.event.pump()
    window.fill((255, 97, 91))
    
    # Back Button
    renderButton(window, menuVars["btnsOM"][0])
    # Mute Button
    renderButton(window, menuVars["btnsOM"][1])
    renderButton(window, menuVars["btnsOM"][2])

# Toggle mute button states
def switchMuteBtnStates(menuVars):
    if (menuVars["btnsOM"][1]["active"]):
        menuVars["btnsOM"][1]["active"] = False
        menuVars["btnsOM"][2]["active"] = True
    else:
        menuVars["btnsOM"][1]["active"] = True
        menuVars["btnsOM"][2]["active"] = False


# ---------------------------------------------------------------------
# Functions useful to all menus

# Scales pygame image by multiplying width and height by scale
def scaleImage(image, scale):
    return pygame.transform.scale(image, (int(image.get_width()*scale), int(image.get_height()*scale)))

# checks if mouse is in bounds of image at x, y position (origin is center of image)
def mouseInBounds(image, pos):
    mouse_pos = pygame.mouse.get_pos()

    if (mouse_pos[0] > pos[0] - image.get_width()/2 and mouse_pos[0] < pos[0] + image.get_width()/2):
        if (mouse_pos[1] > pos[1] - image.get_height()/2 and mouse_pos[1] < pos[1] + image.get_height()/2):
            return True
    return False

# Handles button state (action on mouse up)
def handleBtnState(btnInfo, function = None):
    if (mouseInBounds(btnInfo["images"][0], btnInfo["pos"]) and btnInfo["active"]):
        if (pygame.mouse.get_pressed()[0] == 0 and btnInfo["state"] == 1):
            # Here to do stuff
            if function:
                function()
            btnInfo["state"] = 0
        elif (pygame.mouse.get_pressed()[0] == 1):
            btnInfo["state"] = 1
    else:
        btnInfo["state"] = 0

# Renders individual button based on state
def renderButton(window, btnInfo):
    if(btnInfo["active"] == False):
        pass
    else:
        image = btnInfo["images"][btnInfo["state"]]
        window.blit(image, (btnInfo["pos"][0] - image.get_width()/2, btnInfo["pos"][1] - image.get_height()/2))