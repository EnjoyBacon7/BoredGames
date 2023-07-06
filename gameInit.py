import pygame
from dataclasses import dataclass

@dataclass
class Game:
    cameraX: int
    cameraY: int
    posX: int
    posY: int
    players: list
    map: list
    sprites: dict = None

@dataclass
class Player:
    number: int
    posX: int
    posY: int
    score: int

def gameInit():
    map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    players = [Player(1, 0, 0, 0)]
    sprites = {
        "floorTile": pygame.image.load("gameSprites/floorTile.png"),
        "player1": pygame.image.load("gameSprites/player1.png"),
        "player2": pygame.image.load("gameSprites/player2.png"),
        "player3": pygame.image.load("gameSprites/player3.png"),
        "player4": pygame.image.load("gameSprites/player4.png")
    }

    game = Game(0, 0, 0, 0, players, map, sprites)
    return game
