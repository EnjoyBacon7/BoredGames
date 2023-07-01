import pygame

def renderGame(window, game):
    # Handle events so the window doesn't freeze
    pygame.event.pump()

    # Render Functions
    window.fill((230,255, 255))
    renderBoard(window, game)

    pygame.display.flip()

# ---------------------------------------------------------------------

def renderBoard(window, game):
    for y in range(0, len(game.map)):
        for x in range(0, len(game.map[y])):
            if game.map[y][x] == 1:
                pygame.Surface.blit(window, game.sprites["floorTile"], (x*game.sprites["floorTile"].get_width(), y*game.sprites["floorTile"].get_height()))