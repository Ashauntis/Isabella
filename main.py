import pygame
import sys
import config.settings as settings
from Scenes.game import Game

# Initialize the game
pygame.init()
clock = pygame.time.Clock()

# Set the screen size
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Isabella's Escape")

# Run the program
if __name__ == "__main__":
    game = Game(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
    game.run()