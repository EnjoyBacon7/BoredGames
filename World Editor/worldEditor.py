# pygame for rendering
import pygame
# classes for world struct
from dataclasses import dataclass

def initPygame():
    
    pygame.init()
    pygame.display.set_caption("World Editor")
    pygame.display.set_mode((800,600))
    window = pygame.display.get_surface()
    return window

@dataclass
class World:
    width: int
    height: int
    map: list
    collisions: list

@dataclass
class tileMap:
    width: int
    height: int
    tileWidth: int
    tileHeight: int
    tileSpacing: int
    sprites: list

def initWorldEditor():
    world = World(0,0, [[0]], [[0]])

    # Set a tilemap's values here
    myTileMap = tileMap(37, 28, 16, 16, 1, [])
    tileMapImage = pygame.image.load("Content/world/tileMap.png")
    for y in range(0, myTileMap.height):
        for x in range(0, myTileMap.width):
            tileX = x * myTileMap.tileWidth + x * myTileMap.tileSpacing
            tileY = y * myTileMap.tileHeight + y * myTileMap.tileSpacing
            tile = tileMapImage.subsurface((tileX, tileY, myTileMap.tileWidth, myTileMap.tileHeight))
            myTileMap.sprites.append(tile)

    return world, myTileMap

def worldEditor(window, world, tileMap):

    editTile(world, 0, 0, 1)
    editTile(world, 1, 0, 2)
    editTile(world, 2, 0, 3)
    editTile(world, 0, 1, 4)
    editTile(world, 1, 1, 5)
    editTile(world, 2, 1, 6)
    editTile(world, 0, 2, 7)
    editTile(world, 1, 2, 8)
    editTile(world, 2, 2, 9)

    window.fill((255, 255, 255))
    renderWorld(window, world, tileMap)
    renderMenu(window, world, tileMap)
    pygame.display.flip()

def editTile(world, x, y, tile):
    change = False
    if(x >= world.width):
        world.width = x + 1
        change = True
    if(y >= world.height):
        world.height = y + 1
        change = True
    
    if(change):
        for y in range(0, world.height - len(world.map)):
            world.map.append([])
        for y in range(0, world.height):
            for x in range(0, world.width - len(world.map[y])):
                world.map[y].append(0)
    
    world.map[y][x] = tile

def renderWorld(window, world, tileMap):
    for y in range(0, world.height):
        for x in range(0, world.width):
            tile = tileMap.sprites[world.map[y][x]]
            window.blit(tile, (x * tileMap.tileWidth + x*10, y * tileMap.tileHeight + y*10))


def renderMenu(window, world, tileMap):
    pass

def main():
    window = initPygame()
    world, tileMap = initWorldEditor()

    worldEditor(window, world, tileMap)

    while True:
        if(pygame.event.get(pygame.QUIT)):
            pygame.quit()

main()