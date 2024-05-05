import pygame
import sys
import config.settings as settings 
import config.colors as colors
from Scenes.console import Console
from Scenes.main_menu import MainMenu
from Scenes.basement import Basement
from utility.input import get_input

class Game:
    def __init__(self):
        pygame.init()

        self.level = None

        self.screen_width = settings.SCREEN_WIDTH
        self.screen_height = settings.SCREEN_HEIGHT

        # desktop
        if settings.FULLSCREEN:
            self.screen: pygame.Surface = pygame.display.set_mode(
                settings.RESOLUTION, pygame.FULLSCREEN | pygame.SCALED
            )
        else:
            self.screen: pygame.Surface = pygame.display.set_mode(
                settings.RESOLUTION, pygame.SCALED
            )


        pygame.display.set_caption("Isabella's Escape")

        self.clock = pygame.time.Clock()
        self.scene_stack = []
        self.console = Console(self)

        self.update_input()

    def run(self):
        self.load_scene(settings.START_SCENE)

        if self.scene_stack == []:
            raise ValueError("No scene set for the game")

        while True:
            self.update_input()
            if "console" in self.just_pressed:
                self.console.active = not self.console.active
            layers = ['background', 'obstacle', 'player', 'enemy', 'ui', 'console']
            for layer in layers:
                for scene in self.scene_stack: 
                    if scene.layer == layer and scene.active: 
                        scene.update()
                        scene.render()
                if scene.layer is None:
                    self.console.log('You forgot to set the layer for scene: ' + str(scene) + '! Defaulting to ui layer.')
                    scene.layer = 'ui'

            self.console.update()
            self.console.render()

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
            self.console.log("Scene {scene} not found in stack")
            self.console.log(f"Current scene stack: {self.scene_stack}")

    # optional pop parameter for easy scene cleanup when needed
    def load_scene(self, scene, main_scene = False, scene_pop = None):
        self.console.log(f"Loading scene: {scene}")
        if scene in settings.SCENE_LIST:
            if main_scene:
                self.main_scene = scene
            if scene_pop:
                # remove the scene to be popped
                self.console.log(f"Removing scene: {scene_pop}")
                self.remove_scene(scene_pop)
                self.console.log(f"New scene stack: {self.scene_stack}")
            self.console.log(str(settings.SCENE_LIST[scene] +"(self)"))
            self.scene_stack.append(eval(settings.SCENE_LIST[scene] +"(self)"))
        else: 
            self.console.log(f"Scene {scene} not found in scene list. Defaulting to MainMenu")
            self.scene_stack.append(MainMenu(self))

    def spawn_player_entity(self, entity, position):
        self.player = entity(self, position)
        self.scene_stack.append(self.player)
        self.console.log(f"Spawned player entity: {str(entity)} at position: ({position[0]}, {position[1]})")

    def spawn_entity(self, entity, position):
        self.scene_stack.append(entity(self, position))
        self.console.log(f"Spawned entity: {str(entity)} at position: ({position[0]}, {position[1]})")

    def update_input(self):
        self.pressed, self.just_pressed, self.joysticks = get_input(self)
