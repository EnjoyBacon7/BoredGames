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
        x = player.posX
        y = player.posY
        if 0 <= y < len(game.map) and 0 <= x < len(game.map[y]):
            game.map[y][x] = player.number

def checkInput(game, nplayer):
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            key = event.key
            player = game.players[nplayer]

            # Store previous position
            prevX = player.posX
            prevY = player.posY

            # Update current position
            if key == pygame.K_LEFT and player.posX > 0:
                player.posX -= 1
            if key == pygame.K_RIGHT and player.posX < len(game.map[0]) - 1:
                player.posX += 1
            if key == pygame.K_UP and player.posY > 0:
                player.posY -= 1
            if key == pygame.K_DOWN and player.posY < len(game.map) - 1:
                player.posY += 1

            # Set previous position to 0
            game.map[prevY][prevX] = 0

    
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