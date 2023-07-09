import pygame
import time

import config as cfg
import clientSettings as cs

from gameRender import renderGame

def gameLoop(window, game):

    fpsClock = pygame.time.Clock()

    while True:

        # Handle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Start frame timer
        start_time = time.perf_counter()

        # Menu functions
        checkInput(game)
        renderGame(window, game)
        fpsClock.tick(cs.fps)

        # End frame timer
        end_time = time.perf_counter()
        frame_time = (end_time - start_time) * 1e3
        game.frame_time = frame_time
        if(cs.debugFPS): 
            print(f"Frame time (MM): {frame_time:.2f} milliseconds. FPS: {fpsClock.get_fps():.2f}")

# Handle movement and input
def checkInput(game):
    movement = 0.1 * (game.frame_time * 0.1)
    key_states = pygame.key.get_pressed()
    collisions = getPlayerCollisions(game)
    if(key_states[pygame.K_q] and collisions[0] and collisions[2]):
        game.posX -= movement
    if(key_states[pygame.K_d] and collisions[1] and collisions[3]):
        game.posX += movement
    if(key_states[pygame.K_z] and collisions[0] and collisions[1]):
        game.posY -= movement
    if(key_states[pygame.K_s] and collisions[2] and collisions[3]):
        game.posY += movement

# Handle collisions using character width and collisions map
# It will return a list with directions where the player can go
# [topLeft, topRight, bottomLeft, bottomRight]
def getPlayerCollisions(game):
    collisions = []
    playerCorners = [
        (game.posX, game.posY),
        (game.posX + game.sprites["player"].get_width()/cfg.unit, game.posY),
        (game.posX, game.posY + game.sprites["player"].get_height()/cfg.unit),
        (game.posX + game.sprites["player"].get_width()/cfg.unit, game.posY + game.sprites["player"].get_height()/cfg.unit)]
    for corner in playerCorners:
        if(corner[0] < 0 or corner[0] > 50 or corner[1] < 0 or corner[1] > 50):
            collisions.append(False)
            pass
        if(game.collisions[int(corner[1])][int(corner[0])] == "2"):
            collisions.append(False)
            pass
        collisions.append(True)
    return collisions