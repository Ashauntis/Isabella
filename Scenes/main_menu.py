import pygame
import Scenes.scene as scene
import Scenes.player as player
import config.colors as colors
import utility.functions as f


class MainMenu(scene.Scene):
    def __init__(self, game):
        super().__init__(game)
        self.layer = "ui"
        
        self.background = f.make_transparent_surface((self.game.screen_width, self.game.screen_height))
        self.background.fill((colors.CREAM))

        self.title_text = f.make_text("Isabella's Escape", 60, color=colors.BLACK)
        f.blit_centered(self.title_text, self.background, (0.5, 0.25))

        self.press_start_text = f.make_text("Press Start", 30, color=colors.BLACK)
        f.blit_centered(self.press_start_text, self.background, (0.5, 0.75))

    def update(self):
        if 'return' in self.game.just_pressed:
            self.active = False
            self.game.load_scene("basement", main_scene = True, scene_pop = self)

    def render(self):
        if self.active:
            self.screen.blit(self.background, (0, 0))