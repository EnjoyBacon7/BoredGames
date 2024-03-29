import pygame
import config as cfg
import clientSettings as cs

def debugRender(window, game):
    
    # Change font
    font = pygame.font.SysFont('monospace', 24)

    # Create text
    frame_time = font.render(f"Frametime: {game.frame_time:.2f}", True, (255, 255, 255))
    frame_rate = font.render(f"FPS: {game.frame_rate}", True, (255, 255, 255))
    zoom = font.render(f"Zoom: {cs.zoom}", True, (255, 255, 255))
    collisions = font.render(f"Collisions: {game.player_collisions}", True, (255, 255, 255))

    # map collisions bouding box

    if(cs.debugOverlayCollisions):
        collisions_surface = pygame.Surface((len(game.level[0]) * cfg.unit * cs.zoom, len(game.level) * cfg.unit * cs.zoom), pygame.SRCALPHA)
        collisions_surface.set_alpha(128)
        for y in range(len(game.level)):
            for x in range(len(game.level[y])):
                if(game.level[y][x] == "1"):
                    pygame.draw.rect(collisions_surface, (0, 255, 0), (x * cfg.unit * cs.zoom, y * cfg.unit * cs.zoom, cfg.unit * cs.zoom, cfg.unit * cs.zoom))
                else:
                    pygame.draw.rect(collisions_surface, (255, 0, 0), (x * cfg.unit * cs.zoom, y * cfg.unit * cs.zoom, cfg.unit * cs.zoom, cfg.unit * cs.zoom))
    # Blit to screen
    if(cs.debugOverlayCollisions):
        window.blit(collisions_surface, (cs.resolution_width/2 - game.cameraX * cfg.unit * cs.zoom, cs.resolution_height/2 - game.cameraY * cfg.unit * cs.zoom))
    pygame.draw.rect(window, (0, 0, 0), (0, 0, 550, 200))
    window.blit(frame_time, (0, 0))
    window.blit(frame_rate, (0, 30))
    window.blit(collisions, (0, 60))
    window.blit(zoom, (0, 90))