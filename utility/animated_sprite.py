import pygame

class AnimatedSprite:
    def __init__(self, animations, default_animation = "idle", start_frame = 0):
        self.animations = animations
        self.current_animation = default_animation
        self.animations[self.current_animation].current_frame = start_frame
        self.image = self.animations[self.current_animation].get_current_image()

    def update(self):
        self.animations[self.current_animation].update()
        self.image = self.animations[self.current_animation].get_current_image()
        # print(f"Current Animation: {self.current_animation}, Current frame: {self.current_animation['animation'].current_frame}")

    # Returns the png image of the current frame
    def get_frame(self):
        return self.animations[self.current_animation].get_current_image()
    
    # Switch to a different animation
    def switch_animation(self, key, frame = 0):
        # check if the animations dict has a key of the given key
        if key in self.animations:
            self.current_animation = key
            self.animations[self.current_animation].current_frame = frame   
            self.image = self.animations[self.current_animation].get_current_image()
        else:
            print(f"Could not find animation with key: {key}")
