import pygame
import sys
import config.settings as settings 
import numpy as np
import config.colors as colors

def make_transparent_surface(size: tuple):
    return pygame.Surface(size, pygame.SRCALPHA, 32).convert_alpha()

def scale_asset(asset, size: tuple):
    return pygame.transform.scale(asset, size)

def load_asset(asset_path: str):
    return pygame.image.load("assets/" + asset_path).convert_alpha()

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def make_text(text:str, fontSize: int, color: tuple=colors.WHITE, font: str=None):

    if font is None:
        font = "assets/" + settings.FONT
        return pygame.font.Font(font, fontSize).render(str(text), 1, color)
    
    return pygame.font.SysFont(font, fontSize).render(str(text), 1, color)
    

def blit_centered(source, target, position = (0.5, 0.5)):

    """
    This function places a given surface at a specified position on the target surface.

    Parameters:
    source (pygame.Surface): The source surface to be placed. This is a pygame Surface object, which can be
    created using pygame.font.Font.render() method.

    target (pygame.Surface): The target surface on which the surface is to be placed. This could be
    the game screen or any other surface.

    position (tuple): A tuple of two values between 0 and 1, representing the relative position
    on the target surface where the surface should be placed. The values correspond to the horizontal
    and vertical position respectively. For example, a position of (0.5, 0.5) will place the text dead
    center on the target surface.


    """
    source_position = source.get_rect()
    source_position.centerx = target.get_rect().centerx * position[0] * 2
    source_position.centery = target.get_rect().centery * position[1] * 2
    target.blit(source, source_position)

def blit(source, target, position = (0, 0)):
    target.blit(source, position)


# This function takes a binary set of flags a key dictionary and returns a list of keys that match the flags
# 
# Example usage: 
# binary_key(0b0001_0001, {0b0001_0000: "start", 0b0000_0001: "north", 0b0010_0000: "boss"})
# Returns ["start", "north"]
# 
def binary_key(flags, key):

    matches = []

    for k, v in key.items():
        if flags & k:
            matches.append(v)
    
    return matches
