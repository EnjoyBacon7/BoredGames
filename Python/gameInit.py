import pygame
import csv
import config as cfg

from dataclasses import dataclass

@dataclass
class Game:
    cameraX: int
    cameraY: int

    posX: int
    posY: int

    level: list
    tileSet: list
    
    collisions: list
    sprites: dict

    fpsClock:float

    zoom_level: int

    # Debug variables
    frame_time: float = 0.0
    player_collisions: list = None
    frame_rate: int = 0


def gameInit():

    tileSet = loadTileSet()

    collisions = []
    tmpRow = []
    with open("Content/world/collisions.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            row.pop()
            for value in row:
                tmpRow.append(int(value))
            collisions.append(tmpRow)
            tmpRow = []

    sprites = {
        "floorTile": pygame.image.load("Content/Images/floorTile.png").convert_alpha(),
        "player": pygame.image.load("Content/Images/player1.png").convert_alpha(),
    }

    level = []
    tmpRow = []
    i = 0
    with open("Content/world/level.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            row.pop()
            for value in row:
                tmpRow.append(int(value))
            level.append(tmpRow)
            tmpRow = []
    
    game = Game(0, 0, 1, 1, level, tileSet, collisions, sprites,pygame.time.Clock(), 1)

    print(len(game.level[0]))
    return game

def loadTileSet():
    tileMap = pygame.image.load("Content/world/tileSet.png").convert_alpha()
    tileSet = []
    tileDim = cfg.unit
    for y in range(0, tileMap.get_height(), tileDim + 1):
        for x in range(0, tileMap.get_width(), tileDim + 1):
            tileSet.append(tileMap.subsurface(x, y, tileDim, tileDim))
    return tileSet