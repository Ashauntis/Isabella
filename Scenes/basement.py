import pygame
import Scenes.scene as scene
import config.colors as colors
import utility.mapmaker as mapmaker
# import Scenes.room as Room
from Scenes.room import Room

class Basement(scene.Scene):
    def __init__(self, game, map_size = (20, 20)):
        super().__init__(game)
        self.game = game
        self.map_size = map_size
        self.layer = "background"

        self.background = self.game.make_transparent_surface((self.game.screen_width, self.game.screen_height))
        self.background.fill((colors.BLACK))
        self.background_image = game.load_asset("basement.png")
        # ensure the background image is the same size as the screen
        self.background_image = game.scale_asset(self.background_image, (self.game.screen_width, self.game.screen_height))
        # blit the background image to the background surface once to avoid doing it every frame
        self.game.blit_centered(self.background_image, self.background, (0.5, 0.5))

        # create our floor
        self.level_map = mapmaker.make_floor()


        for x in range(self.level_map.shape[0]):
            for y in range(self.level_map.shape[1]):
                if self.level_map[x, y] != None:
                    room = Room(game, self.level_map[x, y])
                    self.level_map[x, y] = room
                    self.level_map[x, y].display_info()
                else:
                    pass
                    # self.level_map[x, y] = None # ummmm ? 
                


        # track what room we're in
        self.current_location = (map_size/2, map_size/2)

        # Manage our surroundings
        self.north = self.level_map[map_size/2, map_size/2-1]
        self.east = self.level_map[map_size/2+1, map_size/2]
        self.south = self.level_map[map_size/2, map_size/2+1]
        self.west = self.level_map[map_size/2-1, map_size/2]
        
    def update(self):
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))