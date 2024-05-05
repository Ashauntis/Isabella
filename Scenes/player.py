import pygame
from utility.animated_sprite import AnimatedSprite
from utility.spritesheet import SpriteSheet
from utility.animation import Animation

import utility.body as body
import config.colors as colors

class Player(body.Body):
    def __init__(self, game, position=(0, 0)):
        super().__init__(game, position)
        self.layer = "player"
        self.position = pygame.Vector2(position)

        self.active = True

        self.spritesheet = SpriteSheet("assets/Character/Girl-Sheet.png").load_grid_images(1, 44)

        self.sprite = pygame.sprite.Sprite()
        self.animations = AnimatedSprite(animations={
            "walk_down": Animation(images=self.spritesheet[0:4], dur=5),
            "walk_left": Animation(images=self.spritesheet[4:8], dur=5),
            "walk_right": Animation(images=self.spritesheet[8:12], dur=5),
            "walk_up": Animation(images=self.spritesheet[12:16], dur=5),
            "idle": Animation(images=self.spritesheet[0:2], dur=60),
            "death": Animation(images=self.spritesheet[40:44], dur=6, loop=False)
        }, default_animation="idle")
        self.image = self.animations.image
        self.rect = self.animations.image.get_rect(topleft=self.position)

        self.speed = 3.0

        # track the sprites horizontal facing direction
        # false = right, true = left
        self.flip = False

    def handle_movement(self):
        # reset velocity
        self.velocity = pygame.Vector2(0, 0)

        # update velocity based on joystick input
        if self.game.joysticks:
            for joystick in self.game.joysticks:
                self.velocity.x = self.game.joysticks[joystick].get_axis(0) * self.speed
                self.velocity.y = self.game.joysticks[joystick].get_axis(1) * self.speed

        # update velocity based on keyboard input 
        if "left" in self.game.pressed:
            self.velocity.x = -self.speed
        if "right" in self.game.pressed:
            self.velocity.x = self.speed
        if "up" in  self.game.pressed:
            self.velocity.y = -self.speed
        if "down" in self.game.pressed:
            self.velocity.y = self.speed

        if self.velocity.x == 0 and self.velocity.y == 0:
            self.animations.switch_animation("idle")
        else:
            if self.velocity.x < 0:
                self.animations.switch_animation("walk_left")
            elif self.velocity.x > 0:
                self.animations.switch_animation("walk_right")
            elif self.velocity.y < 0:
                self.animations.switch_animation("walk_up")
            elif self.velocity.y > 0:
                self.animations.switch_animation("walk_down")

        if self.velocity.length() != 0:
            self.velocity.scale_to_length(self.speed)

        self.position += self.velocity
        self.rect.topleft = self.position

    def update(self):
        self.handle_movement()
        self.animations.update()
        self.image = self.animations.image

    def render(self):
        self.game.screen.blit(self.animations.image, self.position)

    def on_collision(self, other):
        self.game.console.log(f"Player collided with {other.type}")
        pass

        # if other.type == "wall":
        #     if self.velocity.x > 0:
        #         self.position.x = other.rect.left - self.rect.width
        #     elif self.velocity.x < 0:
        #         self.position.x = other.rect.right
        #     if self.velocity.y > 0:
        #         self.position.y = other.rect.top - self.rect.height
        #     elif self.velocity.y < 0:
        #         self.position.y = other.rect.bottom
        # elif other.type == "enemy":
        #     self.animations.switch_animation("death")
        #     self.active = False
        #     self.game.remove_scene(self)
        #     self.game.load_scene("MainMenu", scene_pop=self.game.scene_stack[-1])
        #     self.game.console.log("Player died. Returning to main menu.")
        # elif other.type == "pickup":
        #     self.game.console.log(f"Player picked up {other.item}")
        #     self.game.remove_scene(other)
        #     self.game.player.inventory.append(other.item)
        #     self.game.console.log(f"Player inventory: {self.game.player.inventory}")
        # elif other.type == "door":
        #     if other.direction == "north":
        #         self.game.load_scene("Basement", scene_pop=self.game.scene_stack[-1])
        #     elif other.direction == "south":
        #         self.game.load_scene("Basement", scene_pop=self.game.scene_stack[-1])
        #     elif other.direction == "west":
        #         self.game.load_scene("Basement", scene_pop=self.game.scene_stack[-1])
        #     elif other.direction == "east":
        #         self.game.load_scene("Basement", scene_pop=self.game.scene_stack[-1])
        # else:
        #     self.game.console.log(f"Player collided with {other.type} at {other.position}")
        #     self.game.console.log(f"Player position: {self.position}")
        #     self.game.console.log(f"Player velocity: {self.velocity}")
        #     self.game.console.log(f"Player rect: {self.rect}")
        #     self.game.console.log(f"Other rect: {other.rect}")
        #     self.game.console.log(f"Other position: {other.position}")
        #     self.game.console.log(f"Other type: {other.type}")
        #     self.game.console.log(f"Other solid: {other.solid}")
        #     self.game.console.log(f"Other image: {other.image}")
        #     self.game.console.log(f"Other rect: {other.rect}")
        #     self.game.console.log(f"Other position: {other.position}")
        #     self.game.console.log(f"Other type: {other.type}")