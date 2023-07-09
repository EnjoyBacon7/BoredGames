import pygame

import clientSettings as cs
import config as cfg

def renderGame(window, game):

    # Render Functions
    window.fill((230,255, 255))
    renderBoard(window, game)
    renderPlayer(window, game)

    pygame.display.flip()

# ---------------------------------------------------------------------

def renderBoard(window, game):
    scaled_map = pygame.transform.scale(game.map, (cs.zoom * 50 * 16, cs.zoom * 50 * 16))
    window.blit(scaled_map, (0, 0))

def renderPlayer(window, game):
    scaled_player = pygame.transform.scale(game.sprites["player"], (cs.zoom * 8, cs.zoom * 16))
    window.blit(scaled_player, (coordsToPixels(game.posX, game.posY)))

def coordsToPixels(x, y):
    return (x * cfg.unit * cs.zoom, y * cfg.unit * cs.zoom)