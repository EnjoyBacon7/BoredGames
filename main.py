# import the pygame module, so you can use it
import pygame

def initPygame():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    ##not set yet
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Bored Games")
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((720,480))
    return screen


running = True
def loopPygame(screen):
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

# define a main function
def main():
     
    screen = initPygame()

    # define a variable to control the main loop
    running = True
    # main loop
    loopPygame(screen)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()