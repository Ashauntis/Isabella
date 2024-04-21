import pygame
import numpy as np
import Scenes.scene as scene
import config.colors as colors
import utility.mapmaker as mapmaker
from Scenes.room import Room
from utility.spritesheet import SpriteSheet
from utility.functions import *

class Basement(scene.Scene):
    def __init__(self, game, map_size = 20):
        super().__init__(game)
        self.game = game
        self.map_size = map_size
        self.layer = "background"
        self.flags = 0

        # track what room we're in
        self.current_location = (map_size//2, map_size//2)

        # create our floor
        self.level_map = mapmaker.make_floor(size=map_size)

        for x in range(self.level_map.shape[0]):
            for y in range(self.level_map.shape[1]):
                if self.level_map[x, y]["flags"] > 0:
                    room = Room(game, self.level_map[x, y]["flags"])
                    self.level_map[x, y]["room"] = room

        # Manage our surroundings
        self.north = False
        self.east = False
        self.south = False
        self.west = False        

        if "north" in self.level_map[self.current_location]["room"].flags:
            self.north = True
        if "east" in self.level_map[self.current_location]["room"].flags:
            self.east = True
        if "south" in self.level_map[self.current_location]["room"].flags:
            self.south = True
        if "west" in self.level_map[self.current_location]["room"].flags:
            self.west = True

        # create our room surface
        self.room_surface = make_transparent_surface((self.game.screen_width, self.game.screen_height))
        self.room_surface.fill((colors.BLACK))

        self.tiles = SpriteSheet("assets/DungeonStarter/DungeonStarter.png").load_grid_images(17, 6)
        self.tileset = {
            0: self.tiles[7], # basic floor

            ## walls
            1: self.tiles[1], # wall top
            2: self.tiles[6], # wall left
            3: self.tiles[8], # wall right
            4: self.tiles[13], # wall bottom
            
            # corners
            5: self.tiles[0], # top left
            6: self.tiles[2], # top right
            7: self.tiles[12], # bottom left
            8: self.tiles[14], # bottom right
            9: self.tiles[3], # outer corner bottom right
            10: self.tiles[4], # outer corner bottom left
            11: self.tiles[10], # outer corner top right
            12: self.tiles[11], # outer corner top left

            # doors
            13: self.tiles[18], # door top 1
            14: self.tiles[19], # door top 2
            15: self.tiles[20], # door top 3
            16: self.tiles[15], # door left 1
            17: self.tiles[21], # door left 2
            18: self.tiles[27], # door left 3
            19: self.tiles[16], # door right 1
            20: self.tiles[22], # door right 2
            21: self.tiles[28], # door right 3
            22: self.tiles[24], # door bottom 1
            23: self.tiles[25], # door bottom 2
            24: self.tiles[26], # door bottom 3


        }

        # create a tilemap filled with zeroes which defaults to basic floor
        tilemap = np.zeros((40, 22)) 

        # set our walls on all sides
        tilemap[1:39, 0] = 1
        tilemap[0, 1:21] = 2
        tilemap[39, 1:21] = 3
        tilemap[1:39, 21] = 4

        # set our corners to the appropriate corner tiles
        tilemap[0, 0] = 5
        tilemap[39, 0] = 6
        tilemap[0, 21] = 7
        tilemap[39, 21] = 8

        # set a floor tile in the middle of each door along the wall
        # where a door exists
        if self.north:
            tilemap[19, 0] = 0
        if self.south:
            tilemap[19, 21] = 0
        if self.east:
            tilemap[39, 11] = 0
        if self.west:
            tilemap[0, 11] = 0

        print(f"Current room flags: {self.level_map[self.current_location]['room'].flags}")

        
        # iterate through the tilemap and draw the appropriate tile with a 4 pixel margin on the top and bottom
        for x in range(tilemap.shape[0]):
            for y in range(tilemap.shape[1]):
                self.room_surface.blit(self.tileset[tilemap[x, y]], (x*16, y*16+4)) 



        # now that the floor has been rendered, render the doors
        # on top of the floor
        for j in range(3):
            if self.north:
                self.room_surface.blit(self.tileset[13+j], ((18+j)*16,0+4)) 
            if self.east:
                self.room_surface.blit(self.tileset[19+j], (39*16,(10+j)*16+4))
            if self.south:
                self.room_surface.blit(self.tileset[22+j], ((18+j)*16,21*16+4))
            if self.west:
                self.room_surface.blit(self.tileset[16+j], (0,(10+j)*16+4))
        

    def update(self):
        pass

    def render(self):
        self.screen.blit(self.room_surface, (0, 0))