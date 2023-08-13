import pygame
import csv
import config as cfg

from dataclasses import dataclass

@dataclass
class Game:

    posX: int
    posY: int

    level: list
    
    playerWidth: int
    playerHeight: int

    fpsClock:float

    # Debug variables
    frame_time: float = 0.0
    player_collisions: list = None
    frame_rate: int = 0

@dataclass
class CameraData:

    cameraX: int
    cameraY: int

    tileSet: list
    tileSet_scaled: list
    tileSet_scaled_zoom: list

    sprites: dict

    zoom_level: int



def gameInit():

    # Creating a game instance

    level = []
    tmpRow = []
    i = 0
    with open("Content/world/level.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if(row[len(row) - 1] == ''): row.pop()
            for value in row:
                tmpRow.append(int(value))
            level.append(tmpRow)
            tmpRow = []
    

    # Creating a camera instance

    sprites = {
        "floorTile": pygame.image.load("Content/Images/floorTile.png").convert_alpha(),
        "player": pygame.image.load("Content/Images/player1.png").convert_alpha(),
    }

    tileSet = loadTileSet()
    tileSet_scaled = tileSet.copy()
    tileSet_scaled_zoom = []
    for tile in range(len(tileSet)):
        tileSet_scaled_zoom.append(tile)


    game = Game(0, 0, level, sprites["player"].get_width()/cfg.unit, sprites["player"].get_height()/cfg.unit,pygame.time.Clock())
    camera = CameraData(0, 0, tileSet, tileSet_scaled, tileSet_scaled_zoom, sprites, 0)
    return game, camera

def loadTileSet():
    tileMap = pygame.image.load("Content/world/tileSet.png").convert_alpha()
    tileSet = []
    tileDim = cfg.unit
    for y in range(0, tileMap.get_height(), tileDim + 1):
        for x in range(0, tileMap.get_width(), tileDim + 1):
            tileSet.append(tileMap.subsurface(x, y, tileDim, tileDim))
    return tileSet