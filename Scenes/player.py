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
        self.spritesheet = SpriteSheet("assets/Character/Girl-Sheet.png").load_grid_images(1, 44)
        # Load our Player Animations
        self.sprite = AnimatedSprite(animations={
            "idle": Animation(images = self.spritesheet[0:2], dur = 60),
            "walk": Animation(images = [self.spritesheet[2], self.spritesheet[3], self.spritesheet[4], self.spritesheet[5]], dur = 60),
            "hurt": Animation(images = SpriteSheet("assets/player/player_hurt.png").load_grid_images(1, 4), dur = 6, loop=False)
        }, default_animation="idle")

        self.position = Vector2(position[0], position[1])
        self.velocity = Vector2(0, 0)
        self.speed = 3.0
        
        # track the sprites horizontal facing direction
        # false = right, true = left
        self.flip = False


    def handle_movement(self):
        self.velocity = Vector2(0, 0)

        # update velocity based on joystick input
        if self.game.joysticks:
            for joystick in self.game.joysticks:
                self.velocity.x = self.game.joysticks[joystick].get_axis(0) * self.speed
                self.velocity.y = self.game.joysticks[joystick].get_axis(1) * self.speed

        if self.game.pressed[pygame.K_LEFT]:
            self.flip = True
            self.velocity.x = -self.speed
        if self.game.pressed[pygame.K_RIGHT]:
            self.flip = False
            self.velocity.x = self.speed
        if self.game.pressed[pygame.K_UP]:
            self.velocity.y = -self.speed
        if self.game.pressed[pygame.K_DOWN]:
            self.velocity.y = self.speed

        if pygame.K_SPACE in self.game.just_pressed:
            if self.sprite.current_animation == "walk":
                self.sprite.switch_animation("hurt")
            else:
                self.sprite.switch_animation("walk")

        self.velocity.scale_velocity()
        self.position += self.velocity


    def update(self):
        self.handle_movement()

    def render(self):
        self.sprite.update()
        self.screen.blit(self.sprite.image, self.position.pos())