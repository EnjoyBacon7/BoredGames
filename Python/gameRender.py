import pygame

import clientSettings as cs
import config as cfg
import utilities as utils

from debug import debugRender

def renderGame(window, game, camera):

    # Camera
    updateCamera(game, camera)

    # Render Functions
    window.fill((230,255, 255))
    renderBoard(window, game, camera)
    renderPlayer(window, game, camera)

    # Debug
    if(cs.debugOverlay):
        debugRender(window, game)

    pygame.display.flip()

# ---------------------------------------------------------------------

# Camera works like so:
# get difference between player coords and camera coords: camera_offset = (x_position - x_camera, y_position - y_camera)
# apply function to camera offset: camera_padding = [f(padding) for x in camera_offset]

def updateCamera(game, camera):
    camera_offset = (game.posX - camera.cameraX, game.posY - camera.cameraY)
    camera_padding = [x/cfg.padding for x in camera_offset]
    camera.cameraX += camera_padding[0]
    camera.cameraY += camera_padding[1]


# ---------------------------------------------------------------------

# Rendering works like so :
# get screen coords using player coords and camera coords: coordsToPixels(x_position - x_camera, y_position - y_camera)
# change origin to center of screen: screen_position = (x_screen_position + (cs.resolution_width/2), y_screen_position + (cs.resolution_height/2))

def renderBoard(window, game, camera):
    screen_position = coordsToPixels(0 - camera.cameraX, 0 - camera.cameraY)
    screen_position = (screen_position[0] + (cs.resolution_width/2), screen_position[1] + (cs.resolution_height/2))
    for i in range(0, len(game.level)):
        for j in range(0, len(game.level[i])):
            curTileNumber = game.level[i][j]
            screen_x = screen_position[0] + (j * cfg.unit * cs.zoom)
            screen_y = screen_position[1] + (i * cfg.unit * cs.zoom)
            if (camera.tileSet_scaled_zoom[curTileNumber] != cs.zoom):
                camera.tileSet_scaled[curTileNumber] = utils.scaleImage(camera.tileSet[game.level[i][j]], cs.zoom)
                camera.tileSet_scaled_zoom[curTileNumber] = cs.zoom
            window.blit(camera.tileSet_scaled[curTileNumber], (screen_x, screen_y))


def renderPlayer(window, game, camera):
    scaled_player = utils.scaleImage(camera.sprites["player"], cs.zoom)
    # Get player position on screen
    screen_position = coordsToPixels(game.posX - camera.cameraX, game.posY - camera.cameraY)
    # change screen position to center of screen
    screen_position = (screen_position[0] + (cs.resolution_width/2), screen_position[1] + (cs.resolution_height/2))
    # blit player to screen
    window.blit(scaled_player, (screen_position))

def coordsToPixels(x, y):
    return (x * cfg.unit * cs.zoom, y * cfg.unit * cs.zoom)