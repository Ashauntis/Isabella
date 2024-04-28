import pygame
import config.settings as settings
import Scenes.scene as scene
import config.colors as colors
import utility.functions as fn
import config.input as input

# A panel for displaying debug information/text within the game
class Console(scene.Scene):
    def __init__(self, game):
        super().__init__(game)
        self.active = False

        self.data_changed = False

        # create a list of data to display
        self.output = []
        self.output_history = []
        self.input = []
        self.input_history = []

        # make a transparent background
        self.background = fn.make_transparent_surface(self.screen.get_size())
        self.background.fill(colors.setColorWithAlpha(colors.GRAY, 200))

        self.log("Console Initialized")

    def log(self, text: str):
        self.output_history.append(text)
        self.data_changed = True

    def update(self):
        
        if self.active:
            if self.data_changed:
                self.data_changed = False
                self.background.fill(colors.setColorWithAlpha(colors.GRAY, 200))
                for i, data in enumerate(self.output_history[-settings.CONSOLE_LINES:]):
                    text = fn.make_text(data, 8, font="monospace")
                    self.background.blit(text, (8, 2 + i * 10))

            for key in self.game.just_pressed:
                # look for terminal input keys
                if key in input.letters or key in input.numbers or key in input.special_chars:
                    self.input.append(key.name)
                if key == pygame.K_SPACE:
                    self.input.append(" ")
                if key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]

                # handle submission of input
                if key == pygame.K_RETURN:
                    if self.input:
                        self.data_changed = True
                        self.input_history.append("".join(self.input))
                        self.output_history("".join(self.input))
                        self.input = []

                        # run the command
                        self.run_command(self.output_history[-1])

    def run_command(self, command: str):
        pass

    def render(self):
        if self.active:
            self.screen.blit(self.background, (0, 0))