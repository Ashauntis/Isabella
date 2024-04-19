import pygame
import sys
import config.settings as settings 
import config.colors as colors
from Scenes.debug import Debug
from Scenes.main_menu import MainMenu
from Scenes.basement import Basement
from utility.functions import get_input

class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        if settings.FULLSCREEN:
            self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((screen_width, screen_height))

        self.clock = pygame.time.Clock()
        self.scene_stack = []
        self.debug = Debug(self)

        self.pressed, self.just_pressed, self.joysticks = get_input()

    def run(self):
        self.load_scene(settings.START_SCENE)

        if self.scene_stack == []:
            raise ValueError("No scene set for the game")

        while True:
            self.pressed, self.just_pressed, self.joysticks = get_input()
            layers = ['background', 'obstacle', 'player', 'enemy', 'ui', 'debug']
            for layer in layers:
                for scene in self.scene_stack: 
                    if scene.layer == layer: 
                        scene.update()
                        scene.render()
                if scene.layer is None:
                    print('You forgot to set the layer for scene: ' + str(scene) + '! Defaulting to debug layer.')
                    scene.layer = 'debug'

            self.debug.update()
            self.debug.render()
            self.debug.clear_data()
            
            pygame.display.flip()
            self.clock.tick(settings.FRAME_LIMIT)  # Cap the frame rate

        pygame.quit()
        sys.exit()


    ######################################

    # Methods for managing scenes

    ######################################

    def add_scene(self, scene, position = None):
        if position:
            self.scene_stack.append(scene(self, position))
        else:
            self.scene_stack.append(scene(self))

    def remove_scene(self, scene):
        if scene in self.scene_stack:
            self.scene_stack.remove(scene)
        else:
            print(f"Scene {scene} not found in stack")
            print(f"Current scene stack: {self.scene_stack}")

    # optional pop parameter for easy scene cleanup when needed
    def load_scene(self, scene, pop = False, scene_pop = None):
        print(f"Loading scene: {scene}")
        if scene in settings.SCENE_LIST:
            if pop:
                # remove the scene to be popped
                print(f"Removing scene: {scene_pop}")
                self.remove_scene(scene_pop)
                print(f"New scene stack: {self.scene_stack}")
            print(str(settings.SCENE_LIST[scene] +"(self)"))
            self.scene_stack.append(eval(settings.SCENE_LIST[scene] +"(self)"))
            print(f"Loaded scene: {scene}")
            print(f"Current scene stack: {self.scene_stack}")
        else: 
            print(f"Scene {scene} not found in scene list. Defaulting to MainMenu")
            self.scene_stack.append(MainMenu(self))

    def spawn_entity(self, entity, position):
        self.scene_stack.append(entity(self, position))
        print(f"Spawned entity: {str(entity)} at position: ({position[0]}, {position[1]})")
