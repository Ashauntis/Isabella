import pygame
import Scenes.scene as scene
import Scenes.player as player
import config.colors as colors
import Scenes.Enemies.fly as fly

class Basement(scene.Scene):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.layer = "background"

        self.background = self.game.make_transparent_surface((self.game.screen_width, self.game.screen_height))
        self.background.fill((colors.BLACK))
        self.map = game.load_asset("basement.png")
        self.map = game.scale_asset(self.map, (self.game.screen_width, self.game.screen_height))
        print(self.map.get_size())
        self.game.blit_centered(self.map, self.background, (0.5, 0.5))
        self.enemies = [self.game.spawn_entity(fly.Fly, (100, 100)), self.game.spawn_entity(fly.Fly, (200, 200))]
        
    def update(self):
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))