from gameRender import renderGame, checkPosition,checkInput

def gameLoop(window, game):
    while True:
        checkPosition(game)
        renderGame(window, game)
        checkInput(game,0)