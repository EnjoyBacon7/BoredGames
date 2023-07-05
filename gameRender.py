import pygame

def renderGame(window, game):
    # Handle events so the window doesn't freeze
    pygame.event.pump()

    # Render Functions
    window.fill((230,255, 255))
    renderBoard(window, game)

    pygame.display.flip()

# ---------------------------------------------------------------------
def checkPosition(game):
    for player in game.players:
        game.map[player.posY][player.posX] = player.number

def checkInput(game,nplayer):
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        game.players[nplayer].posX -= 1
    if key[pygame.K_RIGHT]:
        game.players[nplayer].posX += 1
    if key[pygame.K_UP]:
        game.players[nplayer].posY -= 1
    if key[pygame.K_DOWN]:
        game.players[nplayer].posY += 1
    
    #Borner les valeurs avec la taille de la map


def renderBoard(window, game):
    for y in range(0, len(game.map)):
        for x in range(0, len(game.map[y])):

            if game.map[y][x] == 0:
                pygame.Surface.blit(window, game.sprites["floorTile"], (x*game.sprites["floorTile"].get_width(), y*game.sprites["floorTile"].get_height()))
            
            if game.map[y][x] == 1:
                pygame.Surface.blit(window, game.sprites["player1"], (x*game.sprites["player1"].get_width(), y*game.sprites["player1"].get_height()))
            
            if game.map[y][x] == 2:
                pygame.Surface.blit(window, game.sprites["player2"], (x*game.sprites["player2"].get_width(), y*game.sprites["player2"].get_height()))
            
            if game.map[y][x] == 3:
                pygame.Surface.blit(window, game.sprites["player3"], (x*game.sprites["player3"].get_width(), y*game.sprites["player3"].get_height()))
            
            if game.map[y][x] == 4:
                pygame.Surface.blit(window, game.sprites["player4"], (x*game.sprites["player4"].get_width(), y*game.sprites["player4"].get_height()))