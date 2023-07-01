import pygame

from dataclasses import dataclass

@dataclass
class Game:
    cameraX: int
    cameraY: int

    posX: int
    posY: int

    map: list

    sprites: dict = None


def gameInit():
    
    map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    game = Game(

        0,
        0,
        0,
        0,
        map,
        {
            "floorTile": pygame.image.load("gameSprites/floorTile.png"),
            "player1": pygame.image.load("gameSprites/player1.png"),
            "player2": pygame.image.load("gameSprites/player2.png"),
            "player3": pygame.image.load("gameSprites/player3.png"),
            "player4": pygame.image.load("gameSprites/player4.png")
        }

    )
    return game