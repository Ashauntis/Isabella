import config.colors as colors
import numpy as np
import pygame

from utility.spritesheet import SpriteSheet
from utility.body import Body
import utility.functions as fn


class Tile(Body):
    def __init__(self, game, image, type, position = (0, 0), tile_size = (16, 16)):
        super().__init__(game, position)

        if not hasattr(game.level_scene, "tiles"): 
            raise AttributeError("The game object must have a level_scene attribute with a tiles attribute to add tiles to the scene.")
        
        game.level_scene.tiles.add(self)

        self.image = image
        self.solid = False
        target_surface = game.level_scene.room_surface

        image_surface = fn.make_transparent_surface((tile_size[0], tile_size[1]))
        image_surface.blit(image, (0, 0))
        target_surface.blit(image_surface, position)

        self.type = type
        if self.type == "wall":
            self.solid = True

        self.rect = self.image.get_rect(topleft = position)