import pygame
import Scenes.scene as scene
import config.colors as colors

class Player(scene.Scene):
    def __init__(self, game, position=(0, 0)):
        super().__init__(game)
        self.game = game

        # draw a circle to represent the player
        self.sprite = game.make_transparent_surface((50, 50))
        pygame.draw.circle(self.sprite, (colors.CREAM), (25,25), 25)
        
        self.x = position[0]
        self.y = position[1]
        self.speed = 5

    def update(self):
        if self.game.pressed[pygame.K_LEFT]:
            self.x -= self.speed
        if self.game.pressed[pygame.K_RIGHT]:
            self.x += self.speed
        if self.game.pressed[pygame.K_UP]:
            self.y -= self.speed
        if self.game.pressed[pygame.K_DOWN]:
            self.y += self.speed

    def render(self):
        self.screen.blit(self.sprite, (self.x, self.y))