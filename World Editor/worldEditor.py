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

def initWorldEditor():
    

def main():
    window = initPygame()
    world = initWorldEditor()