# import the pygame module, so you can use it
import pygame

import clientSettings as cs
import config as cfg

from menus import mainMenu, menuInit

# ---------------------------------------------------------------------

def initPygame():

    # initialize the pygame module
    pygame.init()
    
    # load and set the logo
    ##not set yet
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Bored Games")
    
    # create a surface on screen that has the size of 240 x 180
    pygame.display.set_mode((cs.resolution_width,cs.resolution_height))
    window = pygame.display.get_surface()
    return window

# ---------------------------------------------------------------------

# define a main function
def main():


    window = initPygame()

    menuVars = menuInit()
    mainMenu(window, menuVars)

# ---------------------------------------------------------------------

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()