import pygame

class Scene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.time = game.clock.get_time()

    def update(self):
        pass

    def render(self):
        pass

