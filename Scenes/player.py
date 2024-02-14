import pygame
import Scenes.scene as scene
import config.colors as colors
from utility.vector import Vector2

class Player(scene.Scene):
    def __init__(self, game, position=(0, 0)):
        super().__init__(game)
        self.game = game
        self.layer = "player"

        # draw a circle to represent the player
        self.sprite = game.make_transparent_surface((50, 50))
        pygame.draw.circle(self.sprite, (colors.CREAM), (25,25), 25)

        self.position = Vector2(position[0], position[1])
        self.velocity = Vector2(0, 0)
        self.speed = 3.0

    def handle_movement(self):
        self.velocity = Vector2(0, 0)

        # update velocity based on joystick input
        if self.game.joysticks:
            for joystick in self.game.joysticks:
                self.velocity.x = self.game.joysticks[joystick].get_axis(0) * self.speed
                self.velocity.y = self.game.joysticks[joystick].get_axis(1) * self.speed

        if self.game.pressed[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        if self.game.pressed[pygame.K_RIGHT]:
            self.velocity.x = self.speed
        if self.game.pressed[pygame.K_UP]:
            self.velocity.y = -self.speed
        if self.game.pressed[pygame.K_DOWN]:
            self.velocity.y = self.speed

        self.velocity.scale_velocity()
        self.position += self.velocity


    def update(self):
        self.handle_movement()

    def render(self):
        self.screen.blit(self.sprite, self.position.pos())