import pygame
import Scenes.scene as scene
import colors

class MainMenu(scene.Scene):
    def __init__(self, game):
        super().__init__(game)
        
        self.background = self.game.make_transparent_surface((self.game.screen_width, self.game.screen_height))
        self.background.fill((colors.CREAM))

        self.title_text = self.game.make_text("Isabella's Escape", 60)
        self.game.blit_centered(self.title_text, self.background, (0.5, 0.25))

        self.press_start_text = self.game.make_text("Press Start", 30)
        self.game.blit_centered(self.press_start_text, self.background, (0.5, 0.75))

    def update(self):
        if pygame.K_RETURN in self.game.just_pressed:
            self.game.load_scene("basement", True, self)

    def render(self):
        self.screen.blit(self.background, (0, 0))