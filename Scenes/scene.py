import pygame

class Scene:
    def __init__(self, game = None):
        self.game = game
        self.screen = game.screen
        self.time = game.clock.get_time()
        self.layer = None
        self.active = True

    def update(self):
        pass

    def render(self):
        pass

