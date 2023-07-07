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

    frame_time: float

def gameInit():

    map = pygame.image.load("Content/world/level.png").convert_alpha()


    collisions = []
    with open("Content/world/collisions.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            collisions.append(row)

    sprites = {
        "floorTile": pygame.image.load("Content/Images/floorTile.png").convert_alpha(),
        "player1": pygame.image.load("Content/Images/player1.png").convert_alpha(),
        "player2": pygame.image.load("Content/Images/player2.png").convert_alpha(),
        "player3": pygame.image.load("Content/Images/player3.png").convert_alpha(),
        "player4": pygame.image.load("Content/Images/player4.png").convert_alpha(),
    }
    
    game = Game(0, 0, 1, 1, map, collisions, sprites, 0)

    return game
