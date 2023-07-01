import pygame

def renderGame(window, game):
    # Handle events so the window doesn't freeze
    pygame.event.pump()

    window.fill((0,0,0))
    for y in range(0, len(game.map)):
        for x in range(0, len(game.map[y])):
            if game.map[y][x] == 1:
                pygame.Surface.blit(window, game.sprites["floorTile"], (x*100, y*100))


    pygame.display.flip()