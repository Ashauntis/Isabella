import pygame
import sys
import settings 
from Scenes.scene import Scene
from Scenes.main_menu import MainMenu

class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))

        self.clock = pygame.time.Clock()
        self.scene_stack = []

        self.pressed = []
        self.just_pressed = []

    def add_scene(self, scene):
        self.scene_stack.append(scene)

    def remove_scene(self, scene):
        if scene in self.scene_stack:
            self.scene_stack.remove(scene)
        else:
            raise ValueError("Scene not in stack")

    def load_scene(self, scene):
        print(f"Loading scene: {scene}")
        if scene in settings.SCENE_LIST:
            return eval(settings.SCENE_LIST[scene] +"(self)")
        else: 
            return MainMenu(self)

    def get_input(self):
        self.pressed = pygame.key.get_pressed()
        self.just_pressed = []

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.just_pressed.append(event.key)

        # Toggle our Debug Setting
        if pygame.K_F11 in self.just_pressed:
            print(f"Toggling Debug Mode: {settings.DEBUG}")
            settings.DEBUG = not settings.DEBUG

    def make_transparent_surface(self, size: tuple):
        return pygame.Surface(size, pygame.SRCALPHA, 32).convert_alpha()

    def run(self):
        self.scene_stack.append(self.load_scene(settings.START_SCENE))
        if self.scene_stack == []:
            raise ValueError("No scene set for the game")

        while True:
            self.get_input()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for scene in self.scene_stack:
                scene.update()
                scene.render()
            
            pygame.display.flip()
            self.clock.tick(settings.FRAME_LIMIT)  # Cap the frame rate

        pygame.quit()
        sys.exit()