import pygame

import clientSettings as cs
import config as cfg

from debug import debugRender

def renderGame(window, game):

    # Camera
    updateCamera(game)

    # Render Functions
    window.fill((230,255, 255))
    renderBoard(window, game)
    renderPlayer(window, game)

    # Debug
    if(cs.debugOverlay):
        debugRender(window, game)

    pygame.display.flip()

# ---------------------------------------------------------------------

# Camera works like so:
# get difference between player coords and camera coords: camera_offset = (x_position - x_camera, y_position - y_camera)
# apply function to camera offset: camera_padding = [f(padding) for x in camera_offset]

def updateCamera(game):
    camera_offset = (game.posX - game.cameraX, game.posY - game.cameraY)
    camera_padding = [x/cfg.padding for x in camera_offset]
    game.cameraX += camera_padding[0]
    game.cameraY += camera_padding[1]


# ---------------------------------------------------------------------

# Rendering works like so :
# get screen coords using player coords and camera coords: coordsToPixels(x_position - x_camera, y_position - y_camera)
# change origin to center of screen: screen_position = (x_screen_position + (cs.resolution_width/2), y_screen_position + (cs.resolution_height/2))

def renderBoard(window, game):
    screen_position = coordsToPixels(0 - game.cameraX, 0 - game.cameraY)
    screen_position = (screen_position[0] + (cs.resolution_width/2), screen_position[1] + (cs.resolution_height/2))
    for i in range(0, len(game.level)):
        for j in range(0, len(game.level[i])):
            if(game.level[i][j] == 1):
                scaled_tile = pygame.transform.scale(game.tileSet[game.level[i][j]], (cs.zoom * cfg.unit, cs.zoom * cfg.unit))
                window.blit(scaled_tile, (screen_position[0] + (j * cfg.unit * cs.zoom), screen_position[1] + (i * cfg.unit * cs.zoom)))

def renderPlayer(window, game):
    scaled_player = pygame.transform.scale(game.sprites["player"], (cs.zoom * 8, cs.zoom * 16))
    # Get player position on screen
    screen_position = coordsToPixels(game.posX - game.cameraX, game.posY - game.cameraY)
    # change screen position to center of screen
    screen_position = (screen_position[0] + (cs.resolution_width/2), screen_position[1] + (cs.resolution_height/2))
    # blit player to screen
    window.blit(scaled_player, (screen_position))

def coordsToPixels(x, y):
    return (x * cfg.unit * cs.zoom, y * cfg.unit * cs.zoom)