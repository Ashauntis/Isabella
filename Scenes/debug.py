import config.settings as settings
import Scenes.scene as scene
import config.colors as colors
from utility.functions import *

# A panel for displaying debug information/text within the game
class Debug(scene.Scene):
    def __init__(self, game):
        super().__init__(game)
        
        # create a list of data to display
        self.data = ["Debug:",]

        # make a transparent background
        self.background = make_transparent_surface(self.screen.get_size())
        self.background.fill(colors.setAlpha(colors.GRAY, 200))

    def clear_data(self):
        self.data = ["Debug:"]

    def add_data(self, data):
        self.data.append(data)
        
    def update(self):
        pass
    
    def render(self):
        # clear the previous text
        self.background.fill((0, 0, 0, 0))

        for i, element in enumerate(self.data):
            # update with the new text
            text_element = make_text(element, 8, (255, 255, 255))
            # draw the text to the top left of the background
            self.background.blit(text_element, (10, (i * 30) + 10))

        # draw the background to the screen
        if settings.DEBUG:
            self.screen.blit(self.background, (0, 0))