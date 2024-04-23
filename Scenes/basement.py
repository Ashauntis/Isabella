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

        self.make_room()
        

        
    def make_room(self):        
        # Manage our location and surroundings
        self.room = self.level_map[self.current_location]["room"]
        self.room.build_room(SpriteSheet("assets/DungeonStarter/DungeonStarter.png"))
        self.room_surface = self.level_map[self.current_location]["room"].room_surface

    def transition_room(self, direction = "north"):
        self.current_location = (self.current_location[0] + 1, self.current_location[1])
        old_room = self.room_surface
        new_room = self.make_room()

        # TODO finish this :)

        self.room_surface = new_room.room_surface


    def update(self):
        if pygame.K_p in self.game.just_pressed:
            self.room.transition_room()

    def render(self):
        self.screen.blit(self.room_surface, (0, 0))