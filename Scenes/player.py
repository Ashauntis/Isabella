import pygame
import Scenes.scene as scene
import config.colors as colors
from utility.vector import Vector2
from utility.animated_sprite import AnimatedSprite
from utility.spritesheet import SpriteSheet
from utility.animation import Animation

class Player(scene.Scene):
    def __init__(self, game, position=(0, 0)):
        super().__init__(game)
        self.game = game
        self.layer = "player"

        # Load our Player Animations
        self.sprite = AnimatedSprite(animations={
            "idle": Animation(images = SpriteSheet("assets/player_idle.png").load_grid_images(1, 10), dur = 6),
            "walk": Animation(images = SpriteSheet("assets/player_walk.png").load_grid_images(1, 10), dur = 6)
        }, default_animation="idle")

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

        if self.game.pressed[pygame.K_SPACE]:
            self.sprite.switch_animation("walk")

        self.velocity.scale_velocity()
        self.position += self.velocity


    def update(self):
        self.handle_movement()

    def render(self):
        self.sprite.update()
        # self.sprite.draw(self.screen, self.position.pos())
        self.screen.blit(self.sprite.get_frame(), self.position.pos())