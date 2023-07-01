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
            "floorTile": pygame.image.load("gameSprites/floorTile.png")
        }
        
    )
    return game