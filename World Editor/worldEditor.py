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
    selectedTile: int
    mouseX: int
    mouseY: int
    cameraX: int
    cameraY: int

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
    world = World(0, 0, 0, 0, 0, 0, 0, [], [])

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

def editTile(world, x, y, tile):
    # Enlarge map if adding a tile outside of it
    if x >= world.width:
        for i in range(world.width, x + 1):
            for row in world.map:
                row.append(-1)
        world.width = x + 1
    if y >= world.height:
        for i in range(world.height, y + 1):
            world.map.append([-1] * world.width)
        world.height = y + 1

    # Shift map if adding a tile on the left or above
    if x < 0:
        for i in range(-x):
            for row in world.map:
                row.insert(0, -1)
            world.width += 1
    if y < 0:
        for i in range(-y):
            world.map.insert(0, [-1] * world.width)
            world.height += 1

    world.map[y][x] = tile




def renderWorld(window, world, tileMap):
    for y in range(0, world.height):
        for x in range(0, world.width):
            if(world.map[y][x] == -1):
                continue
            tile = tileMap.sprites[world.map[y][x]]
            window.blit(tile, (x * tileMap.tileWidth + world.cameraX, y * tileMap.tileHeight + world.cameraY))
    highlightX = world.mouseX * tileMap.tileWidth + world.cameraX
    highlightY = world.mouseY * tileMap.tileHeight + world.cameraY
    pygame.draw.rect(window, (255, 255, 0), (highlightX, highlightY, tileMap.tileWidth, tileMap.tileHeight))

def renderMenu(window, world, tileMap):
    pass

def handleCameraInput(world):
    key_states = pygame.key.get_pressed()
    if(key_states[pygame.K_z]):
        world.cameraY -= 1
    if(key_states[pygame.K_s]):
        world.cameraY += 1
    if(key_states[pygame.K_q]):
        world.cameraX -= 1
    if(key_states[pygame.K_d]):
        world.cameraX += 1

def handleMouseInput(world, tileMap):
    # Get mouse position
    mousePos = pygame.mouse.get_pos()
    worldPosX = (mousePos[0] - world.cameraX) // tileMap.tileWidth
    worldPosY = (mousePos[1] - world.cameraY) // tileMap.tileHeight

    world.mouseX = worldPosX
    world.mouseY = worldPosY
    print(worldPosX, worldPosY)
    # Check if mouse is clicked
    if pygame.mouse.get_pressed()[0]:
        editTile(world, worldPosX, worldPosY, world.selectedTile)
        if(worldPosX < 0):
            world.cameraX -= tileMap.tileWidth
        if(worldPosY < 0):
            world.cameraY -= tileMap.tileHeight
    elif pygame.mouse.get_pressed()[2]:
        editTile(world, worldPosX, worldPosY, -1)    

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

    clock = pygame.time.Clock()

    while True:
        if(pygame.event.get(pygame.QUIT)):
            pygame.quit()

        handleCameraInput(world)
        handleMouseInput(world, tileMap)

        window.fill((255, 255, 255))
        renderWorld(window, world, tileMap)
        renderMenu(window, world, tileMap)
        pygame.display.flip()
        clock.tick(120)

def main():
    window = initPygame()
    world, tileMap = initWorldEditor()

    worldEditor(window, world, tileMap)

main()