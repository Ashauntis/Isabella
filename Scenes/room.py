# from ..utility.functions import *
import config.colors as colors

from Scenes.tile import Tile
import Scenes.scene as scene
import utility.functions as f


class Room(scene.Scene):
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

        self.pickups = []
        self.enemies = []

    def build_room(self, spritesheet):
        self.tile_images = spritesheet.load_grid_images(17, 6)
        self.tileset = {
            0: Tile(self.game, self.tile_images[7], "floor").image, # basic floor

            ## walls
            1: self.tile_images[1], # wall top
            2: self.tile_images[6], # wall left
            3: self.tile_images[8], # wall right
            4: self.tile_images[13], # wall bottom
            
            # corners
            5: self.tile_images[0], # top left
            6: self.tile_images[2], # top right
            7: self.tile_images[12], # bottom left
            8: self.tile_images[14], # bottom right
            9: self.tile_images[3], # outer corner bottom right
            10: self.tile_images[4], # outer corner bottom left
            11: self.tile_images[10], # outer corner top right
            12: self.tile_images[11], # outer corner top left

            # doors
            13: self.tile_images[18], # door top 1
            14: self.tile_images[19], # door top 2
            15: self.tile_images[20], # door top 3
            16: self.tile_images[15], # door left 1
            17: self.tile_images[21], # door left 2
            18: self.tile_images[27], # door left 3
            19: self.tile_images[16], # door right 1
            20: self.tile_images[22], # door right 2
            21: self.tile_images[28], # door right 3
            22: self.tile_images[24], # door bottom 1
            23: self.tile_images[25], # door bottom 2
            24: self.tile_images[26], # door bottom 3
        }

        # 40x22 allows for a 16x16 tileset with a 4 pixel top and bottom margin
        # leaving a value at 0 defaults to a basic floor tile
        tilemap = []
        for i in range(40):
            tilemap.append([0]*22)
                

        # draw the walls on all four sides
        for i in range(40):
            tilemap[i][0] = Tile(self.game, self.tileset[1], "wall", position=(i*16, 0+4))
            tilemap[i][21] = Tile(self.game, self.tileset[4], "wall", position=(i*16, 21*16+4))
        for i in range(22):
            tilemap[0][i] = Tile(self.game, self.tileset[2], "wall", position=(0, i*16+4))
            tilemap[39][i] = Tile(self.game, self.tileset[3], "wall", position=(39*16, i*16+4))

        # set our corners to the appropriate corner tiles
        tilemap[0][0] = Tile(self.game, self.tileset[5], "wall", position=(0, 0+4))
        tilemap[39][0] = Tile(self.game, self.tileset[6], "wall", position=(39*16, 0+4))
        tilemap[0][21] = Tile(self.game, self.tileset[7], "wall", position=(0, 21*16+4))
        tilemap[39][21] = Tile(self.game, self.tileset[8], "wall", position=(39*16, 21*16+4))


        # set a floor tile in the middle of each door along the wall
        # where a door exists
        if "north" in self.flags:
            tilemap[19][0] = Tile(self.game, self.tileset[0], "door", position=(19*16, 0+4))
        if "south" in self.flags:
            tilemap[19][21] = Tile(self.game, self.tileset[0], "door", position=(19*16, 21*16+4))
        if "east" in self.flags:
            tilemap[39][11] = Tile(self.game, self.tileset[0], "door", position=(39*16, 11*16+4))
        if "west" in self.flags:
            tilemap[0][11] = Tile(self.game, self.tileset[0], "door", position=(0, 11*16+4))

        # iterate through the tilemap and draw the appropriate tile with a 4 pixel margin on the top and bottom
        for x in range(40):
            for y in range(22):
                if type(tilemap[x][y]) == int:
                    tilemap[x][y] = Tile(self.game, self.tileset[tilemap[x][y]], "floor", position=(x*16, y*16+4))

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
        
        # This return statement isn't currently being used, but I'm leaving it in for now
        return self.room_surface