import pygame
import random
import Scenes.room as Room

def make_transparent_surface(size: tuple):
    return pygame.Surface(size, pygame.SRCALPHA, 32).convert_alpha()

def scale_asset(asset, size: tuple):
    return pygame.transform.scale(asset, size)

def load_asset(asset_path: str):
    return pygame.image.load("assets/" + asset_path).convert_alpha()

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

