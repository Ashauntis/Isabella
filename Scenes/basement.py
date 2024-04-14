import pygame
import Scenes.scene as scene
import config.colors as colors
import utility.mapmaker as mapmaker
from Scenes.room import Room
from utility.functions import *

class Basement(scene.Scene):
    def __init__(self, game, map_size = (20, 20)):
        super().__init__(game)
        self.game = game
        self.map_size = map_size
        self.layer = "background"

        self.background = make_transparent_surface((self.game.screen_width, self.game.screen_height))
        self.background.fill((colors.BLACK))
        self.background_image = load_asset("basement.png")
        # ensure the background image is the same size as the screen
        self.background_image = scale_asset(self.background_image, (self.game.screen_width, self.game.screen_height))
        # blit the background image to the background surface once to avoid doing it every frame
        blit_centered(self.background_image, self.background, (0.5, 0.5))

        # create our floor
        self.level_map = mapmaker.make_floor()
        print(self.level_map)


        # for x in range(self.level_map.shape[0]):
        #     for y in range(self.level_map.shape[1]):
        #         if self.level_map[x, y]["room"] != None:
        #             room = Room(game, self.level_map[x, y]["flags"])
        #             self.level_map[x, y]["room"] = room
        #             print(self.level_map[x, y]["room"].room_type)
            


        # track what room we're in
        self.current_location = (map_size[0]//2, map_size[1]//2)

        # Manage our surroundings
        self.north = self.level_map[map_size[0]//2][map_size[1]//2-1]
        self.east = self.level_map[map_size[0]//2+1][map_size[1]//2]
        self.south = self.level_map[map_size[0]//2][map_size[1]//2+1]
        self.west = self.level_map[map_size[0]//2-1][map_size[1]//2]
        
    def update(self):
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))