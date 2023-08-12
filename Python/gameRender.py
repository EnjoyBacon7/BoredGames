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

    # WIP
    # map_view = pygame.Rect(game.cameraX, game.cameraY, 1/cs.zoom * 16, 1/cs.zoom * 16)
    # sub_img = game.map.subsurface(map_view)
    # scaled_view = pygame.transform.scale(sub_img, (cs.resolution_width, cs.resolution_height))

    # window.blit(scaled_view, coordsToPixels(0, 0))

    if(game.map_cache_factor != cs.zoom):
        game.map_cache = pygame.transform.scale(game.map, (cs.zoom * 50 * 16, cs.zoom * 50 * 16))
        game.map_cache_factor = cs.zoom
    scaled_map = game.map_cache
    screen_position = coordsToPixels(0 - game.cameraX, 0 - game.cameraY)
    screen_position = (screen_position[0] + (cs.resolution_width/2), screen_position[1] + (cs.resolution_height/2))
    window.blit(scaled_map, (screen_position))


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