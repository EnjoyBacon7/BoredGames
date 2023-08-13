import pygame
import time

import config as cfg
import clientSettings as cs
import utilities as utils

from gameRender import renderGame

def gameLoop(window, game, camera):

    while True:

        # Handle events
        utils.handleEvents()

        # Start frame timer
        start_time = time.perf_counter()

        # Menu functions
        checkInput(game, camera)
        renderGame(window, game, camera)
        game.fpsClock.tick(cs.fps)

        # End frame timer
        end_time = time.perf_counter()
        game.frame_time = (end_time - start_time) * 1e3
        game.frame_rate = int(game.fpsClock.get_fps())

# Handle movement and input
def checkInput(game, camera):
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
    
    # zooming with numpad 1 and 3
    if(key_states[pygame.K_KP1]):
        camera.zoom_level -= 0.05
    if(key_states[pygame.K_KP3]):
        camera.zoom_level += 0.05
    cs.zoom = 2 ** camera.zoom_level


# Handle collisions using character width and collisions map
# It will return a list with directions where the player can go
# [topLeft, topRight, bottomLeft, bottomRight]
def getPlayerCollisions(game):
    collisions = []
    playerCorners = [
        (game.posX, game.posY),
        (game.posX + game.playerWidth, game.posY),
        (game.posX, game.posY + game.playerHeight),
        (game.posX + game.playerWidth, game.posY + game.playerHeight)]
    for corner in playerCorners:
        if(corner[0] < 0 or corner[0] > 50 or corner[1] < 0 or corner[1] > 50):
            collisions.append(False)
            continue
        elif(game.level[int(corner[1])][int(corner[0])] == 2):
            collisions.append(False)
            continue
        collisions.append(True)
    game.player_collisions = collisions
    return collisions