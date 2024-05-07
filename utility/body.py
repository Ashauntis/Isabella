import pygame

class Body(pygame.sprite.Sprite):
    def __init__(self, game, position):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        # variables to track location and movement
        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(0, 0)

        self.collisions = {
            "top": False,
            "bottom": False,
            "left": False,
            "right": False
        }

        # variables to track size and shape
        self.image = None
        self.rect = None

        self.visible = True

    def update(self):
        pass

    def draw(self):
        if self.visible:
            self.game.screen.blit(self.image, self.rect)

    def on_collision(self, other):
        print(f"Body collided with {other.type}")
