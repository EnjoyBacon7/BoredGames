import pygame

def renderGame(screen, game):
    # Handle events so the window doesn't freeze
    pygame.event.pump()
    screen.fill((0,0,0))
    for y in range(0, len(game.map)):
        for x in range(0, len(game.map[y])):
            if game.map[y][x] == 1:
                pygame.draw.rect(screen, (255,255,255), (x*20, y*20, 10, 10))
                print("Drawing tile at " + str(x*80) + ", " + str(y*80))
    pygame.display.flip()