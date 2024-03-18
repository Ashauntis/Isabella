import pygame 

class AnimatedSprite:
    def __init__(self, sprites: list, fps: int):
        
        self.sprites = sprites
        self.fps = fps

        self.animations = {}
        self.current_animation = None
        self.current_frame = 0
        self.current_time = 0
        