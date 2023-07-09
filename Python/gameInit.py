import pygame
import csv

from dataclasses import dataclass

@dataclass
class Game:
    cameraX: int
    cameraY: int

    posX: int
    posY: int

    map: list
    
    collisions: list
    sprites: dict

    fpsClock:float = pygame.time.Clock()

    # Debug variables
    frame_time: float = 0.0
    player_collisions: list = None
    frame_rate: int = 0


def gameInit():

    map = pygame.image.load("Content/world/level.png").convert_alpha()

    collisions = []
    with open("Content/world/collisions.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            collisions.append(row)

    sprites = {
        "floorTile": pygame.image.load("Content/Images/floorTile.png").convert_alpha(),
        "player": pygame.image.load("Content/Images/player1.png").convert_alpha(),
    }
    
    game = Game(0, 0, 1, 1, map, collisions, sprites)

    return game
