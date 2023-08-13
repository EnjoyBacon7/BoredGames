import pygame


def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# Scales pygame image by multiplying width and height by scale
def scaleImage(image, scale):
    return pygame.transform.scale(image, (int(image.get_width()*scale), int(image.get_height()*scale)))
