import config.colors as colors
import numpy as np
import pygame

from utility.spritesheet import SpriteSheet
from utility.body import Body
import utility.functions as fn


class Tile(Body):
    def __init__(self, game, image, target = False, position = (0, 0), collider = False, tile_size = (16, 16)):
        super().__init__(game, position)

        print(f'level scene: {game.level_scene}')
        print(hasattr(game.level_scene, "tiles"))

        if not hasattr(game.level_scene, "tiles"): 
            return
        
        game.level_scene.tiles.add(self)

        self.image = image
        target_surface = game.level_scene.room_surface

        image_surface = fn.make_transparent_surface((tile_size[0], tile_size[1]))
        image_surface.blit(image, (0, 0))
        target_surface.blit(image_surface, position)

        self.rect = self.image.get_rect(topleft = position)
        
















        # self.tile_surface = f.make_transparent_surface(
        #     (tile_size[0], tile_size[1]))
        # self.tile_surface.fill((colors.BLACK))

        # self.tile_surface.blit(image, (0, 0))
        # if target: 
        #     target.blit(image, position)

        # self.collider = collider
        # if self.collider:
        #     self.position = pygame.math.Vector2(position)
        #     self.rect = self.tile_surface.get_rect(topleft = self.position)
        #     self.velocity = pygame.math.Vector2(0, 0) 
        #     game.room_colliders.append(self)
        #     game.console.log(str(game.room_colliders))