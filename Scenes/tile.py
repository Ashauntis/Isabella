# from ..utility.functions import *
import config.colors as colors
import numpy as np
import pygame

from utility.spritesheet import SpriteSheet
import utility.functions as f


class Tile:
    def __init__(self, game, image, target = False, position = (0, 0), collider = False, tile_size = (16, 16)):
        # This class creates a tile object with properties for
        # collision detection. '
        
        # If you provide the target and position
        # arguments, the tile will be drawn to the target surface at the
        # specified position. 
        
        # If you provide the collider argument, the tile will be added to
        # the game's room_colliders list for collision detection.s


        self.tile_surface = f.make_transparent_surface(
            (tile_size[0], tile_size[1]))
        self.tile_surface.fill((colors.BLACK))

        self.tile_surface.blit(image, (0, 0))
        if target: 
            target.blit(image, position)

        self.collider = collider
        if self.collider:
            self.position = pygame.math.Vector2(position)
            self.velocity = pygame.math.Vector2(0, 0) 
            game.room_colliders.append(self)
            game.console.log(str(game.room_colliders))