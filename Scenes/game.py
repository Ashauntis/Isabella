import pygame
import sys
import settings 
import colors
from Scenes.scene import Scene
from Scenes.main_menu import MainMenu
from Scenes.basement import Basement

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
            self.scene_stack.append(eval(settings.SCENE_LIST[scene] +"(self)"))
            print(f"Loaded scene: {scene}")
            print(f"Current scene stack: {self.scene_stack}")
        else: 
            print(f"Scene {scene} not found in scene list. Defaulting to MainMenu")
            self.scene_stack.append(MainMenu(self))

    def load_asset(self, asset_path: str):
        return pygame.image.load("assets/" + asset_path).convert_alpha()

    def scale_asset(self, asset, size: tuple):
        return pygame.transform.scale(asset, size)

    def get_input(self):
        self.pressed = pygame.key.get_pressed()
        self.just_pressed = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                self.just_pressed.append(event.key)

        # Toggle our Debug Setting
        if pygame.K_F11 in self.just_pressed:
            print(f"Toggling Debug Mode: {settings.DEBUG}")
            settings.DEBUG = not settings.DEBUG

    def make_transparent_surface(self, size: tuple):
        return pygame.Surface(size, pygame.SRCALPHA, 32).convert_alpha()

    def make_text(self, text, fontSize, color=colors.GRAY, font=None):
        if font is None:
            font = "assets/" + settings.FONT

        return pygame.font.Font(font, fontSize).render(text, 1, color)

    def blit_centered(self, source, target, position = (0.5, 0.5)):

        """
        This function places a given surface at a specified position on the target surface.

        Parameters:
        source (pygame.Surface): The source surface to be placed. This is a pygame Surface object, which can be
        created using pygame.font.Font.render() method.

        target (pygame.Surface): The target surface on which the surface is to be placed. This could be
        the game screen or any other surface.

        position (tuple): A tuple of two values between 0 and 1, representing the relative position
        on the target surface where the surface should be placed. The values correspond to the horizontal
        and vertical position respectively. For example, a position of (0.5, 0.5) will place the text dead
        center on the target surface.


        """
        source_position = source.get_rect()
        source_position.centerx = target.get_rect().centerx * position[0] * 2
        source_position.centery = target.get_rect().centery * position[1] * 2
        target.blit(source, source_position)

    def run(self):
        self.load_scene(settings.START_SCENE)
        if self.scene_stack == []:
            raise ValueError("No scene set for the game")

        while True:
            self.get_input()
            for scene in self.scene_stack:
                scene.update()
                scene.render()
            
            pygame.display.flip()
            self.clock.tick(settings.FRAME_LIMIT)  # Cap the frame rate

        pygame.quit()
        sys.exit()