import Scenes.scene as scene
import colors

class MainMenu(scene.Scene):
    def __init__(self, game):
        super().__init__(game)
        
        self.background = self.game.make_transparent_surface((self.game.screen_width, self.game.screen_height))
        self.background.fill((colors.CREAM))

    def update(self):
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))