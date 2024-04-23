# from ..utility.functions import *
import config.colors as colors
import numpy as np

from utility.spritesheet import SpriteSheet
import utility.functions as f


class Room:
    def __init__(self, game=None, flags=0):
        self.game = game
        self.room_type = None

        room_bits = {
            0b0000_0001: "north",
            0b0000_0010: "east",
            0b0000_0100: "south",
            0b0000_1000: "west",
            0b0001_0000: "start",
            0b0010_0000: "boss",
        }

        self.flags = f.binary_key(flags, room_bits)

        for flag in self.flags:
            if flag == "start":
                self.room_type = "start"
            elif flag == "boss":
                self.room_type = "boss"
            else:
                self.room_type = "basic"

        self.room_surface = f.make_transparent_surface(
            (self.game.screen_width, self.game.screen_height))
        self.room_surface.fill((colors.BLACK))
        # self.build_room(SpriteSheet("assets/DungeonStarter/DungeonStarter.png"))

        self.pickups = []
        self.enemies = []

    def build_room(self, spritesheet):
        self.tiles = spritesheet.load_grid_images(17, 6)
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

        # 40x22 allows for a 16x16 tileset with a 4 pixel top and bottom margin
        # leaving a value at 0 defaults to a basic floor tile
        tilemap = tilemap = np.zeros((40, 22))

        # draw the walls on all four sides
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
        if "north" in self.flags:
            tilemap[19, 0] = 0
        if "south" in self.flags:
            tilemap[19, 21] = 0
        if "east" in self.flags:
            tilemap[39, 11] = 0
        if "west" in self.flags:
            tilemap[0, 11] = 0

        # iterate through the tilemap and draw the appropriate tile with a 4 pixel margin on the top and bottom
        for x in range(tilemap.shape[0]):
            for y in range(tilemap.shape[1]):
                self.room_surface.blit(self.tileset[tilemap[x, y]], (x*16, y*16+4)) 

        # now that the floor has been rendered, render the doors
        # on top of the floor
        for j in range(3):
            if "north" in self.flags:
                self.room_surface.blit(self.tileset[13+j], ((18+j)*16,0+4)) 
            if "east" in self.flags:
                self.room_surface.blit(self.tileset[19+j], (39*16,(10+j)*16+4))
            if "south" in self.flags:
                self.room_surface.blit(self.tileset[22+j], ((18+j)*16,21*16+4))
            if "west" in self.flags:
                self.room_surface.blit(self.tileset[16+j], (0,(10+j)*16+4))
        
        return self.room_surface