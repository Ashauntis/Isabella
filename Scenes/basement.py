import pygame
import numpy as np
import Scenes.scene as scene
import config.colors as colors
import utility.mapmaker as mapmaker
from Scenes.room import Room
from utility.spritesheet import SpriteSheet
from utility.functions import *

class Basement(scene.Scene):
    def __init__(self, game, map_size = (20, 20)):
        super().__init__(game)
        self.game = game
        self.map_size = map_size
        self.layer = "background"

        # track what room we're in
        self.current_location = (map_size[0]//2, map_size[1]//2)

        # create our floor
        self.level_map = mapmaker.make_floor()

        for x in range(self.level_map.shape[0]):
            for y in range(self.level_map.shape[1]):
                if self.level_map[x, y]["flags"] > 0:
                    room = Room(game, self.level_map[x, y]["flags"])
                    self.level_map[x, y]["room"] = room

        # create our room surface
        self.room_surface = make_transparent_surface((self.game.screen_width, self.game.screen_height))
        self.room_surface.fill((colors.BLACK))

        # Manage our surroundings
        self.north = self.level_map[map_size[0]//2][map_size[1]//2-1]
        self.east = self.level_map[map_size[0]//2+1][map_size[1]//2]
        self.south = self.level_map[map_size[0]//2][map_size[1]//2+1]
        self.west = self.level_map[map_size[0]//2-1][map_size[1]//2]

        self.tiles = SpriteSheet("assets/DungeonStarter/DungeonStarter.png").load_grid_images(17, 6)
        self.tileset = {
            0: self.tiles[8], # basic floor
            1: self.tiles[1], # wall top
            2: self.tiles[2], # corner top right
            3: self.tiles[0], # corner top left
            4: self.tiles[3], # outer corner bottom right
            5: self.tiles[4], # outer corner bottom left
            6: self.tiles[5]  # water
        }

        # create a tilemap filled with zeroes which defaults to basic floor
        tilemap = np.zeros((40, 22)) 

        # tilemap[0, 0] = 0
        # for x in range(1, 38):
        #     tilemap[x, 0] = 1
        # tilemap[39, 0] = 2
        
        # iterate through the tilemap and draw the appropriate tile with a 4 pixel margin on the top and bottom
        for x in range(tilemap.shape[0]):
            for y in range(tilemap.shape[1]):
                self.room_surface.blit(self.tileset[tilemap[x, y]], (x*16+4, y*16)) 

    def update(self):
        pass

    def render(self):
        self.screen.blit(self.room_surface, (0, 0))