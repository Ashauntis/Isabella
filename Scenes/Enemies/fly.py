import pygame
import Scenes.scene as scene
import config.colors as colors
from utility.vector import Vector2

class Fly(scene.Scene):
    def __init__(self, game, position=(0, 0)):
        super().__init__(game)
        self.game = game
        self.layer = "enemy"

        # draw a red circle to represent the enemy
        self.sprite = game.make_transparent_surface((20, 20))
        pygame.draw.circle(self.sprite, (colors.RED), (10, 10), 10)

        self.position = Vector2(position[0], position[1])
        self.velocity = Vector2(0, 0)
        self.speed = 1.0

    def update(self):
        pass
    
    def render(self):
            self.screen.blit(self.sprite, self.position.pos())