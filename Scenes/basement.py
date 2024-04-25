import pygame
import numpy as np
import Scenes.scene as scene
import config.colors as colors
import utility.mapmaker as mapmaker
from Scenes.room import Room
from utility.spritesheet import SpriteSheet
import utility.functions as fn

class Basement(scene.Scene):
    def __init__(self, game, map_size = 20):
        super().__init__(game)
        self.game = game
        self.map_size = map_size
        self.layer = "background"
        self.flags = 0

        # track what room we're in
        self.current_location = (map_size//2, map_size//2)

        # transition utilities
        self.transition_surface = None
        self.old_room = None
        self.transition_duration = 0
        self.transition_time = 0
        self.transition_speed = 1
        self.transition_direction = "None"

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

    def transition_room(self, direction = "north", duration = 60):
        return
        print("Transition room called")
        # the number of frames it will take to complete the animation
        self.transition_duration = duration
        self.transition_time = duration

        self.transition_direction = direction
        if direction == "north":
            self.current_location = (self.current_location[0], self.current_location[1] - 1)
            print(f"Transitioning North, current location: {self.current_location}")
        elif direction == "south":
            self.current_location = (self.current_location[0], self.current_location[1] + 1)
            print(f"Transitioning South, current location: {self.current_location}")
        elif direction == "west":
            self.current_location = (self.current_location[0] - 1, self.current_location[1])
            print(f"Transitioning West, current location: {self.current_location}")
        elif direction == "east":
            self.current_location = (self.current_location[0] + 1, self.current_location[1])
            print(f"Transitioning East, current location: {self.current_location}")

        # keep a snapshot of our current room
        self.old_room = self.room_surface
        self.make_room()

        # create our surface to animate the transition
        self.transition_surface = pygame.Surface(self.room_surface.get_size())
        self.transition_surface.fill(colors.BLACK)



    def update(self):
        # transition stuff
        if self.transition_time > 0:
            self.transition_time -= self.transition_speed
            
            # transition percentage
            tp = (self.transition_duration - self.transition_time) / self.transition_duration
            
            # if we're transitioning, update the transition surface based on the direction and time
            if self.transition_direction == "north":
                self.transition_surface.blit(self.room_surface, (0, (-self.game.screen_height) * (1 - tp)))
                self.transition_surface.blit(self.old_room, (0, self.game.screen_height * tp))
            elif self.transition_direction == "south":
                self.transition_surface.blit(self.room_surface, (0, self.game.screen_height * (1-tp)))
                self.transition_surface.blit(self.old_room, (0, -self.game.screen_height * tp))
            elif self.transition_direction == "west":
                self.transition_surface.blit(self.room_surface, (-self.game.screen_width + (tp * self.game.screen_width), 0))
                self.transition_surface.blit(self.old_room, (tp * self.game.screen_width, 0))
            elif self.transition_direction == "east":
                self.transition_surface.blit(self.room_surface, (self.game.screen_width * (1 - tp), 0))
                self.transition_surface.blit(self.old_room, (-self.game.screen_width * tp, 0))
            return
    
        if pygame.K_UP in self.game.just_pressed and "north" in self.room.flags:
                self.transition_room(direction = "north")
        elif pygame.K_DOWN in self.game.just_pressed and "south" in self.room.flags:
            self.transition_room(direction = "south")
        elif pygame.K_LEFT in self.game.just_pressed and "west" in self.room.flags:
            self.transition_room(direction = "west")
        elif pygame.K_RIGHT in self.game.just_pressed and "east" in self.room.flags:
            self.transition_room(direction = "east")

    def render(self):
        if self.transition_time > 0:
            self.screen.blit(self.transition_surface, (0, 0))
        else:
            self.screen.blit(self.room_surface, (0, 0))