import pygame
import Scenes.scene as scene
import Scenes.player as player
import config.colors as colors
from utility.functions import *

class MainMenu(scene.Scene):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.layer = "ui"
        
        self.background = make_transparent_surface((self.game.screen_width, self.game.screen_height))
        self.background.fill((colors.CREAM))

        self.title_text = make_text("Isabella's Escape", 60)
        blit_centered(self.title_text, self.background, (0.5, 0.25))

        self.press_start_text = make_text("Press Start", 30)
        blit_centered(self.press_start_text, self.background, (0.5, 0.75))

    def update(self):
        print(self.game.just_pressed)
        if pygame.K_RETURN in self.game.just_pressed:
            self.game.load_scene("basement", True, self)
            # spawn the player at the center of the screen
            self.game.spawn_entity(player.Player, (self.game.screen_width / 2, self.game.screen_height / 2))

    def render(self):
        self.screen.blit(self.background, (0, 0))