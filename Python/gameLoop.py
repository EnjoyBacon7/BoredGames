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
                sys.exit()

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
        print(f"Frame time (MM): {frame_time:.2f} milliseconds. FPS: {fpsClock.get_fps():.2f}")

# Handle movement and input
def checkInput(game):
    movement = 0.1 * (game.frame_time * 0.1)
    key_states = pygame.key.get_pressed()
    if(key_states[pygame.K_q]):
        game.posX -= movement
        if(handlePlayerCollisions(game)):
            game.posX += movement
    if(key_states[pygame.K_d]):
        game.posX += movement
        if(handlePlayerCollisions(game)):
            game.posX -= movement
    if(key_states[pygame.K_z]):
        game.posY -= movement
        if(handlePlayerCollisions(game)):
            game.posY += movement
    if(key_states[pygame.K_s]):
        game.posY += movement
        if(handlePlayerCollisions(game)):
            game.posY -= movement

# Handle collisions using character width and collisions map
def handlePlayerCollisions(game):
    playerCorners = [
        (game.posX, game.posY),
        (game.posX + game.sprites["player1"].get_width()/cfg.unit, game.posY),
        (game.posX, game.posY + game.sprites["player1"].get_height()/cfg.unit),
        (game.posX + game.sprites["player1"].get_width()/cfg.unit, game.posY + game.sprites["player1"].get_height()/cfg.unit)]
    for corner in playerCorners:
        if(corner[0] < 0 or corner[0] > 50 or corner[1] < 0 or corner[1] > 50):
            return True
        if(game.collisions[int(corner[1])][int(corner[0])] == "2"):
            return True
    return False